from django.apps import AppConfig


class PollConfig(AppConfig):
    name = 'poll'

    def ready(self):
        from .graphql import routes  # noqa