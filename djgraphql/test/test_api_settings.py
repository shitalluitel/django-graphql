from djgraphql.settings import APISettings
from djgraphql.test import TestCaseSetup


class TestAPISettings(TestCaseSetup):
    def test_api_settings(self):
        api_settings = APISettings()
        api_settings.defaults = {
            'GRAPHQL_APPS': ['Test'],
        }

        self.assertTrue(api_settings.GRAPHQL_APPS, ['Test'])
