from django.test import TestCase

# Create your tests here.

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

from estrellas.schema import schema
from estrellas.models import Estrella

ESTRELLAS_QUERY = '''
 {
   estrellas {
     id
     nombre
     color
   }
 }
'''
CREATE_ESTRELLA_MUTATION = '''
 mutation createEstrellaMutation($nombre: String,$distancia: String,$radio: Float,$rotacion: Float,$edad: Int,$ubicacion: Int,$masa: Int,$temperatura: Float,$constelacion: String,$color: String) {
     createEstrella(nombre: $nombre,distancia: $distancia,radio: $radio,rotacion: $rotacion,edad: $edad,ubicacion: $ubicacion,masa: $masa,temperatura: $temperatura,constelacion: $constelacion,color: $color) {
        nombre
     }
 }
'''
#distancia,radio,rotacion,edad,ubicacion,masa,temperatura,constelacion,color


class EstrellaTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.estrella1 = mixer.blend(Estrella)
        self.estrella2 = mixer.blend(Estrella)

    def test_estrellas_query(self):
        response = self.query(
            ESTRELLAS_QUERY,
        )


        content = json.loads(response.content)
        #print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print ("query estrella results ")
        print (content)
        assert len(content['data']['estrellas']) == 2

    def test_createEstrella_mutation(self):

        response = self.query(
            CREATE_ESTRELLA_MUTATION,
            variables={'nombre':'Orion','distancia':'5 ly','radio':5.5,'rotacion':7.8,'edad':5,'ubicacion':15,'masa':7,'temperatura':5000.5,'constelacion':'Orion','color':'Amarillo'}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createEstrella": {"nombre":"Orion"}}, content['data'])
        #self.assertDictEqual({"createEstrella": {"nombre":"Orion","distancia":"5 ly"}}, content['data']) 
#"distancia":"5 ly","radio":5.5,"rotacion":7.8,"edad":5,"ubicacion":15,'masa':7,"temperatura":5000.5,"constelacion":"Orion","color":"Amarillo"