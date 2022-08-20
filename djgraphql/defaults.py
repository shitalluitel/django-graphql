from dataclasses import dataclass, asdict


@dataclass
class Defaults:
    GRAPHQL_APPS: list = None
    GRAPHENE = {
        'SCHEMA': 'schema.schema',
        'RELAY_CONNECTION_MAX_LIMIT': 10000,
    }


def update_defaults(default, class_name):
    _class = globals()[class_name]
    defaults = asdict(_class())
    default.update(defaults)


def get_defaults(agg_defaults=None):
    if not agg_defaults:
        agg_defaults = {}
    update_defaults(agg_defaults, 'Defaults')
    return agg_defaults
