from sqlalchemy import ForeignKey, String, Integer, DateTime, Boolean, Float
from sqlalchemy.orm import Mapped, mapped_column,DeclarativeBase
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    def __repr__(self) -> str:
        cols = []
        for col in self.__table__.columns.keys():
            cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String)
    bio: Mapped[str] = mapped_column(String(300))
    superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    register_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())


class Posts(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str | None] = mapped_column(String(256))
    text: Mapped[str | None] = mapped_column(String)
    file_url: Mapped[str | None] = mapped_column(String)
    user_id: Mapped[str] = mapped_column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    published_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated: Mapped[bool] = mapped_column(Boolean, default=False, onupdate=True)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())


class Comments(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('posts.id', ondelete='CASCADE'))
    reply: Mapped[int | None] = mapped_column(
        Integer, ForeignKey('comments.id', ondelete='CASCADE'), default=None)
    text: Mapped[str] = mapped_column(String(1000))
    updated: Mapped[bool] = mapped_column(Boolean, default=False, onupdate=True)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
    published_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())


class Likes(Base):
    __tablename__ = 'likes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('posts.id', ondelete='CASCADE'))
    entity: Mapped[int] = mapped_column(Integer)
    entity_id: Mapped[int] = mapped_column(Integer)

