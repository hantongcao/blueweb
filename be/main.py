import uvicorn
import os
import asyncio
from bluenote.config.config import settings
from bluenote.server.db import get_session
from bluenote.schemas.users import User, UserCreate
from bluenote.security import get_secret_hash
from sqlmodel import select

def main():
    """启动 FastAPI 应用"""
    # 使用配置文件中的设置
    server_config = settings.get_server_config()
    
    uvicorn.run(
        "bluenote.server.app:create_app",  # 使用导入字符串
        factory=True,  # 表示create_app是一个工厂函数
        host=server_config["host"],
        port=server_config["port"],
        reload=server_config["reload"],
        log_level=server_config["log_level"]
    )

    # 初始化管理员账号
    asyncio.run(init_admin_user())


async def init_admin_user():
    """初始化管理员账号"""
    async for session in get_session():
        # 检查是否已存在管理员账号
        statement = select(User).where(
            User.username == settings.INIT_ADMIN_USERNAME,
            User.deleted_at.is_(None)
        )
        result = await session.exec(statement)
        existing_admin = result.first()
        
        if not existing_admin:
            # 创建管理员账号
            admin_data = UserCreate(
                username=settings.INIT_ADMIN_USERNAME,
                password=settings.INIT_ADMIN_PASSWORD,
                is_admin=True,
                full_name="系统管理员"
            )
            
            hashed_password = get_secret_hash(admin_data.password)
            admin_user = User(
                username=admin_data.username,
                is_admin=admin_data.is_admin,
                full_name=admin_data.full_name,
                hashed_password=hashed_password
            )
            
            session.add(admin_user)
            await session.commit()
            print(f"管理员账号已创建: {settings.INIT_ADMIN_USERNAME}")
        else:
            print(f"管理员账号已存在: {settings.INIT_ADMIN_USERNAME}")
        
        break  # 只需要一个session


if __name__ == "__main__":
    main()