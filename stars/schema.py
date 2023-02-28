import graphene

import estrellas.schema


class Query(estrellas.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
