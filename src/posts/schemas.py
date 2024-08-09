from pydantic import BaseModel


class PostsSchema(BaseModel):
    title: str
    text: str
    file_url: str

