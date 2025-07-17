from datetime import datetime
from typing import Optional, List

from sqlalchemy import Column, UniqueConstraint, String, Text, Boolean, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import JSON
from sqlmodel import Field, SQLModel, Relationship

from enum import Enum

from pydantic import ConfigDict
class ContentStatus(str, Enum):
    """内容状态枚举（适用于博客、照片等）"""
    DRAFT = "draft"  # 草稿
    PUBLISHED = "published"  # 已发布
    PRIVATE = "private"  # 私密
    ARCHIVED = "archived"  # 已归档
    DELETED = "deleted"  # 已删除

class Visibility(str, Enum):
    """可见性枚举"""
    PUBLIC = "public"  # 公开
    FRIENDS = "friends"  # 仅好友可见
    PRIVATE = "private"  # 仅自己可见

from bluenote.mixins import BaseModelMixin
from bluenote.schemas.common import PaginatedList, UTCDateTime, BlogCategory

class BlogBase(SQLModel):
    title: str
    content: str = Field(sa_column=Column(Text))  # 博客内容
    summary: Optional[str] = Field(default=None, max_length=500)  # 博客摘要
    status: ContentStatus = Field(default=ContentStatus.DRAFT)  # 博客状态
    visibility: Visibility = Field(default=Visibility.PUBLIC)  # 可见性
    tags: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))  # 博客标签列表
    category: Optional[BlogCategory] = Field(default=None)  # 分类
    
    # 互动数据
    like_count: int = Field(default=0)  # 点赞数
    comment_count: int = Field(default=0)  # 评论数
    share_count: int = Field(default=0)  # 分享数
    view_count: int = Field(default=0)  # 浏览数
    



class Blog(BlogBase, BaseModelMixin, table=True):
    __tablename__ = 'blogs'
    id: Optional[int] = Field(default=None, primary_key=True)
    model_config = ConfigDict(protected_namespaces=())

class BlogCreate(BlogBase):
    """创建博客请求模型"""
    pass


class BlogUpdate(SQLModel):
    """更新博客请求模型"""
    title: Optional[str] = None
    content: Optional[str] = None
    summary: Optional[str] = None
    status: Optional[ContentStatus] = None
    visibility: Optional[Visibility] = None
    tags: Optional[List[str]] = None
    category: Optional[BlogCategory] = None
    


class BlogPublic(BlogBase):
    """公开博客响应模型"""
    id: int
    created_at: datetime
    updated_at: datetime


class BlogUpdateResponse(SQLModel):
    """更新博客响应模型"""
    id: int
    title: str
    content: str
    summary: Optional[str] = None
    status: ContentStatus
    visibility: Visibility
    tags: Optional[List[str]] = None
    category: Optional[BlogCategory] = None


class BlogStats(SQLModel):
    """博客统计信息"""
    total_blogs: int
    published_blogs: int
    draft_blogs: int
    private_blogs: int
    total_likes: int
    total_views: int
    total_comments: int


BlogsPublic = PaginatedList[BlogPublic]