from dataclasses import dataclass, asdict


@dataclass
class CommonDefaults:
    pass


def update_defaults(default, class_name):
    _class = globals()[class_name]
    defaults = asdict(_class())
    default.update(defaults)


def get_defaults(payments):
    agg_defaults = {}

    for payment_class in payments:
        class_name = payment_class.title() + 'Defaults'
        update_defaults(agg_defaults, class_name)

    update_defaults(agg_defaults, 'CommonDefaults')
    return agg_defaults
