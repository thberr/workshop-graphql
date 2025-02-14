from typing import List
import strawberry


@strawberry.type
class Comment:
    id: int
    content: str
    author: str

   
@strawberry.type
class Post:
    id: int
    title: str
    content: str
    comments: List[Comment]

@strawberry.type
class User:
    id: int
    name: str
    email: str
    posts: List[Post]


def get_comments():
    return [
        Comment(
            id=1,
            content="First comment",
            author="Me"
        ),
        Comment(
            id=2,
            content="Second comment",
            author="Not me"
        )
    ]

@strawberry.type
class Query:
    comments: List[Comment] = strawberry.field(resolver=get_comments)

schema = strawberry.Schema(query=Query)
