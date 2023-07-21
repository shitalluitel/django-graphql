from typing import Optional

import graphene

from djgraphql.utils.resolver import Resolver

__all__ = [
    'MethodType',
    'Query',
    'Mutation',
    'DefaultRouter'
]


class MethodType(graphene.Enum):
    QUERY = 'query'
    MUTATION = 'mutation'


Query = MethodType.QUERY
Mutation = MethodType.MUTATION


class DefaultRouter(object):
    _query_resolvers = None
    _mutation_resolvers = None

    def register(self, resolver: Resolver, method: Optional[MethodType] = None):
        if not method:
            method = Query

        if isinstance(method, MethodType):
            raise ValueError(f'method must be either {Query} or {Mutation}.')

        routers = getattr(self, f'_{method.value}_routers')

        if routers is None:
            routers = []

        routers.append(resolver)

    @property
    def query(self):
        return self._query_resolvers

    @property
    def mutations(self):
        return self._mutation_resolvers
