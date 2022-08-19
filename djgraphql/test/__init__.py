from django.test import TestCase
from graphene_django.utils import GraphQLTestCase


class TestCaseSetup(TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()

    def _should_check_constraints(self, connection):
        return False


class GrapheneTestCase(TestCaseSetup, GraphQLTestCase):
    query_string: str = ''
    op_name: str or None = None
    variables: dict or None = None
    GRAPHQL_URL = '/graphql'

    def setUp(self) -> None:
        super().setUp()

    def get_query_string(self):
        assert self.query_string != '', 'Must provide query for this test case.'
        return self.query_string

    def get_variables(self):
        return self.variables

    def get_op_name(self):
        return self.op_name

    def get_values(self, name):
        values = getattr(self, f'get_{name}')()
        if not values:
            return {}
        return {
            name: values
        }

    def _test_query(self):
        variables = self.get_values('variables')
        op_name = self.get_values('op_name')

        response = self.query(
            self.get_query_string(),
            **op_name,
            **variables
        )
        self.assertResponseNoErrors(response)
