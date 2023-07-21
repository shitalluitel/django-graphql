from djgraphql.utils.resolver import Resolver
from djgraphql.utils.routes import DefaultRouter, MethodType


class ResolverGenerator:
    def __new__(cls, name, *args, **kwargs):
        return type(name, (Resolver,), kwargs)


class TestDefaultRouter:
    def test_valid_routers(self):
        router = DefaultRouter()

        # 1. Register query resolvers
        query = ResolverGenerator('QueryResolver')
        router.register(
            resolver=query,
            method=MethodType.QUERY
        )
        assert router.query ==

        # 2. Register mutation resolvers
        mutation = ResolverGenerator('MutationResolver')
        router.register(
            resolver=mutation,
            method=MethodType.MUTATION
        )
        assert router.mutation == [mutation]
