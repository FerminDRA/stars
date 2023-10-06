import graphene

import estrellas.schema
import users.schema


class Query(estrellas.schema.Query,users.schema.Query, graphene.ObjectType):
    pass

class Mutation(estrellas.schema.Mutation,users.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
