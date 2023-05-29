import graphene
from graphene_django import DjangoObjectType
from estrellas.models import Estrella, Vote
from graphql import GraphQLError
from django.db.models import Q




from .models import Estrella
from users.schema import UserType


class EstrellaType(DjangoObjectType):
    class Meta:
        model = Estrella

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote

class Query(graphene.ObjectType):
    estrellas = graphene.List(EstrellaType, search=graphene.String())
    votes = graphene.List(VoteType)


    def resolve_estrellas(self, info, search=None, **kwargs):
        # The value sent with the search parameter will be in the args variable
        if search:
            filter = (
                Q(nombre__icontains=search) |
                Q(color__icontains=search)
            )
            return Estrella.objects.filter(filter)

        return Estrella.objects.all()
    
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()


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
    posted_by = graphene.Field(UserType)


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
        user = info.context.user or None
        estrella = Estrella(nombre=nombre, distancia=distancia, radio=radio, rotacion=rotacion, edad=edad, ubicacion=ubicacion, masa=masa,temperatura=temperatura, constelacion=constelacion, color=color,posted_by=user)
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
            posted_by=estrella.posted_by,
        )


class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    estrella = graphene.Field(EstrellaType)

    class Arguments:
        estrella_id = graphene.Int()

    def mutate(self, info, estrella_id):
        user = info.context.user
        if user.is_anonymous:
            #1
            raise GraphQLError('You must be logged to vote!')

        estrella = Estrella.objects.filter(id=estrella_id).first()
        if not estrella:
            #2
            raise Exception('Invalid estrella!')

        Vote.objects.create(
            user=user,
            estrella=estrella,
        )

        return CreateVote(user=user, estrella=estrella)

class Mutation(graphene.ObjectType):
    create_estrella = CreateEstrella.Field()
    create_vote = CreateVote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
