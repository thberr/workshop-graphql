import strawberry

from graphql_api.resolvers import (CommentMutation, CommentQuery,
                                   ProjectMutation, ProjectQuery, TaskMutation,
                                   TaskQuery, UserMutation, UserQuery)


@strawberry.type
class Query(UserQuery, ProjectQuery, CommentQuery, TaskQuery):
    pass

@strawberry.type
class Mutation(UserMutation, ProjectMutation, CommentMutation, TaskMutation):
    pass 

schema = strawberry.Schema(query=Query, mutation=Mutation)
