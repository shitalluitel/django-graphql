from unittest.mock import patch

from djgraphql.schema import SchemaGenerator
from djgraphql.test import TestCaseSetup
from djgraphql.utils import get_resolver_class

QUERY_RESOLVERS = [type('test', (object,), {})]


class TestSchema(TestCaseSetup):
    @patch('djgraphql.schema.SchemaGenerator.get_graphql_apps', lambda x: ['test'])
    @patch(
        'djgraphql.schema.SchemaGenerator.import_resolver',
        lambda *x: type('DummyClass', (), {'QUERY_RESOLVERS': QUERY_RESOLVERS})
    )
    def test_schema(self):
        schema = SchemaGenerator()
        generated_class = [*schema.get_classes()]
        resolver_class = get_resolver_class(QUERY_RESOLVERS)

        self.assertTrue(type(generated_class), 'list')
        self.assertTrue(generated_class, resolver_class)
