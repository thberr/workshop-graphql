import strawberry
from graphql_api.resolvers import UserQuery, ProjectQuery, CommentQuery
from graphql_api.resolvers import UserMutation, ProjectMutation, CommentMutation

@strawberry.type
class Query(UserQuery, ProjectQuery, CommentQuery):
    pass

@strawberry.type
class Mutation(UserMutation, ProjectMutation, CommentMutation):
    pass 

schema = strawberry.Schema(query=Query, mutation=Mutation)
