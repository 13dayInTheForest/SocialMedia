from base import BaseRepo
from sqlalchemy import select
from src.schemas.posts import PostsFilter


class Posts(BaseRepo):
    async def get_posts_by_id(self, user_id: int, max_posts: int):
        posts = await self.session.execute(
            select(self.model).where(self.model.user_id == user_id).limit(max_posts)
        )
        return posts.all()

    async def get_posts(self, post_filter: PostsFilter):
        filters = post_filter.dict(exclude_unset=True)

