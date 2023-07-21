from djgraphql.schema import schema
from djgraphql.test.test_routers import ResolverGenerator
from djgraphql.utils.routes import DefaultRouter, MethodType


class TestSchemaGeneration:
    def test_schema_generation(self):
        first_router = DefaultRouter()
        first_query = ResolverGenerator('FirstQueryResolver')
        first_mutation = ResolverGenerator('FirstMutationResolver')
        first_router.register(first_query, MethodType.QUERY)
        first_router.register(first_mutation, MethodType.MUTATION)

        schema.register(first_router)

        second_router = DefaultRouter()
        second_query = ResolverGenerator('SecondQueryResolver')
        second_mutation = ResolverGenerator('SecondMutationResolver')
        second_router.register(second_query, MethodType.QUERY)
        second_router.register(second_mutation, MethodType.MUTATION)

        schema.register(second_router)

        assert schema._resolvers['query'] == [first_query, second_query]
        assert schema._resolvers['mutation'] == [first_mutation, second_mutation]
