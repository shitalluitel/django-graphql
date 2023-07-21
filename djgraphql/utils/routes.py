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

        resolvers = getattr(self, f'_{method.value}_resolvers')

        if resolvers is None:
            setattr(self, f'_{method.value}_resolvers', [])
            resolvers = getattr(self, f'_{method.value}_resolvers')

        resolvers.append(resolver)

    @property
    def query(self):
        query_resolver = self._query_resolvers or []
        return type(
            'Query',
            (
                *query_resolver,
                graphene.ObjectType
            ),
            {}
        )

    @property
    def mutation(self):
        mutation_resolver = self._mutation_resolvers or []
        return type(
            'Mutation',
            (
                *mutation_resolver,
                graphene.ObjectType,
            ),
            {}
        )
