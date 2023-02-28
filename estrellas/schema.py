import graphene
from graphene_django import DjangoObjectType

from .models import Estrella


class EstrellaType(DjangoObjectType):
    class Meta:
        model = Estrella


class Query(graphene.ObjectType):
    estrellas = graphene.List(EstrellaType)

    def resolve_estrellas(self, info, **kwargs):
        return Estrella.objects.all()
