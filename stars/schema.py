import graphene

import estrellas.schema


class Query(estrellas.schema.Query, graphene.ObjectType):
    pass

class Mutation(estrellas.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
schema = graphene.Schema(query=Query, mutation=Mutation)
