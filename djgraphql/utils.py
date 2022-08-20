import graphene


def get_resolver_class(resolvers: list, resolver_type: str = 'Query') -> type:
    return type(
        resolver_type,
        (
            *resolvers,
            graphene.ObjectType
        ),
        {}
    )
