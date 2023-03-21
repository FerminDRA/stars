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
