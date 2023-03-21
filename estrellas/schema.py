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


class CreateEstrella(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    distancia = graphene.String()
    radio = graphene.Float()
    rotacion = graphene.Float()
    edad = graphene.Int()
    ubicacion = graphene.Int()
    masa = graphene.Int()
    temperatura = graphene.Float()
    constelacion = graphene.String()
    color = graphene.String()


    class Arguments:
        nombre = graphene.String()
        distancia = graphene.String()
        radio = graphene.Float()
        rotacion = graphene.Float()
        edad = graphene.Int()
        ubicacion = graphene.Int()
        masa = graphene.Int()
        temperatura = graphene.Float()
        constelacion = graphene.String()
        color = graphene.String()

    def mutate(self, info, nombre, distancia, radio, rotacion, edad, ubicacion, masa, temperatura, constelacion, color):
        estrella = Estrella(nombre=nombre, distancia=distancia, radio=radio, rotacion=rotacion, edad=edad, ubicacion=ubicacion,temperatura=temperatura, constelacion=constelacion, color=color)
        estrella.save()

        return CreateEstrella(
            id=estrella.id,
            nombre=estrella.nombre,
            distancia=estrella.distancia,
            radio=estrella.radio,
            rotacion=estrella.rotacion,
            edad=estrella.edad,
            ubicacion=estrella.ubicacion,
            masa=estrella.masa,
            temperatura=estrella.temperatura,
            constelacion=estrella.constelacion,
            color=estrella.color,
        )

class Mutation(graphene.ObjectType):
    create_estrella = CreateEstrella.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
