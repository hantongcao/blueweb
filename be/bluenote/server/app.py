from contextlib import asynccontextmanager
import aiohttp
import os
from fastapi import FastAPI
from fastapi_cdn_host import monkey_patch_for_docs_ui

from bluenote.api import exceptions, middlewares
from bluenote.routes.routes import api_router
from bluenote.server.db import init_db
from bluenote.config.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 使用配置文件中的数据库URL
    database_url = settings.get_database_url()
    await init_db(database_url)
    
    app.state.http_client = aiohttp.ClientSession()
    yield
    await app.state.http_client.close()

def create_app() -> FastAPI:
    """创建 FastAPI 应用实例"""
    app = FastAPI(
        title=settings.APP_TITLE,
        lifespan=lifespan,
        response_model_exclude_unset=True,
        # docs_url=None,  # 禁用 /docs
        # redoc_url=None,  # 禁用 /redoc
    )
    
    monkey_patch_for_docs_ui(app)
    app.add_middleware(middlewares.RequestTimeMiddleware)
    
    app.include_router(api_router)
    exceptions.register_handlers(app)
    
    return app

# 为了向后兼容，保留这个实例
app = create_app()