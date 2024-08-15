from .repositories.users import UsersRepo
from .repositories.posts import PostsRepo
from .services.users import UserService
from .services.posts import PostService
from src.database.models import Users, Posts


async def create_users_service(session):
    return UserService(session, UsersRepo, Users)


async def create_posts_service(session):
    return PostService(session, PostsRepo, Posts)

