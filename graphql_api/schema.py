import strawberry
from graphql_api.resolvers import UserQuery, ProjectQuery, CommentQuery, TaskQuery
from graphql_api.resolvers import UserMutation, ProjectMutation, CommentMutation, TaskMutation

@strawberry.type
class Query(UserQuery, ProjectQuery, CommentQuery, TaskQuery):
    pass

@strawberry.type
class Mutation(UserMutation, ProjectMutation, CommentMutation, TaskMutation):
    pass 

schema = strawberry.Schema(query=Query, mutation=Mutation)
