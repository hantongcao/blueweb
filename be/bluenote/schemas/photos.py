from typing import Optional, List
from datetime import datetime

from sqlalchemy import Column, String, Text, Integer, Float
from sqlalchemy.dialects.postgresql import JSON
from sqlmodel import Field, SQLModel

from bluenote.schemas.blogs import ContentStatus, Visibility



from bluenote.mixins import BaseModelMixin
from bluenote.schemas.common import PaginatedList, PhotoCategory


class PhotoBase(SQLModel):
    """照片基础模型"""
    title: Optional[str] = Field(default=None, max_length=100)  # 照片标题
    description: Optional[str] = Field(default=None, sa_column=Column(Text))  # 照片描述
    url_list: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))  # 照片URL列表，支持多张图片
    
    # 地理位置信息
    location_name: Optional[str] = Field(default=None, max_length=200)  # 位置名称
    
    # 状态和可见性
    status: ContentStatus = Field(default=ContentStatus.DRAFT)  # 照片状态
    visibility: Visibility = Field(default=Visibility.PUBLIC)  # 可见性
    
    # 标签和分类
    tags: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))  # 标签列表
    category: Optional[PhotoCategory] = Field(default=None)  # 分类
    
    # 互动数据
    like_count: int = Field(default=0)  # 点赞数
    comment_count: int = Field(default=0)  # 评论数
    share_count: int = Field(default=0)  # 分享数
    view_count: int = Field(default=0)  # 浏览数
    
    # 拍摄信息
    taken_at: Optional[datetime] = Field(default=None)  # 拍摄时间


class Photo(PhotoBase, BaseModelMixin, table=True):
    """照片数据库模型"""
    __tablename__ = 'photos'
    
    id: Optional[int] = Field(default=None, primary_key=True)


class PhotoCreate(PhotoBase):
    """创建照片请求模型"""
    pass


class PhotoUpdate(SQLModel):
    """更新照片请求模型"""
    title: Optional[str] = None
    description: Optional[str] = None
    url_list: Optional[List[str]] = None  # 支持更新照片URL列表
    status: Optional[ContentStatus] = None
    visibility: Optional[Visibility] = None
    tags: Optional[List[str]] = None
    category: Optional[PhotoCategory] = None
    location_name: Optional[str] = None


class PhotoPublic(PhotoBase):
    """公开照片响应模型"""
    id: int
    created_at: datetime
    updated_at: datetime
    url_list: List[str] = Field(default_factory=list)  # 确保返回空列表而不是None


class PhotoUpdateResponse(SQLModel):
    """更新照片响应模型 - 包含更新后的字段"""
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    url_list: Optional[List[str]] = None  # 返回更新后的URL列表
    location_name: Optional[str] = None
    status: Optional[ContentStatus] = None  # 返回更新后的状态
    visibility: Visibility
    tags: Optional[List[str]] = None
    category: Optional[PhotoCategory] = None




class PhotoStats(SQLModel):
    """照片统计信息"""
    total_photos: int
    published_photos: int
    draft_photos: int
    private_photos: int
    total_likes: int
    total_views: int
    total_comments: int


# 分页列表类型
PhotosPublic = PaginatedList[PhotoPublic]