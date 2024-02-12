import socket

from ..entities.meta_data import MetaData

class MetaCollector:
    def __init__(self, context_provider, settings):
        self.context_provider = context_provider
        self.settings = settings

    def collect_data(self) -> MetaData:
        meta_data = MetaData(data_map={})
        api_key = self.context_provider.get_application_property('clickstream.apiKey')
        operating_system = self.context_provider.get_application_property('clickstream.custom.os.name')
        platform = self.context_provider.get_application_property('clickstream.custom.platform')

        # Дополняем словарь значениями
        meta_data.data_map['systemLanguage'] = 'PYTHON'
        meta_data.data_map['apiKey'] = api_key if api_key else self.settings.get_api_key()
        meta_data.data_map['platform'] = platform if platform else 'BACKEND'
        meta_data.data_map['operatingSystem'] = operating_system if operating_system else self.get_operating_system()
        meta_data.data_map['applicationName'] = self.get_application_name()

        return meta_data

    def get_operating_system(self) -> str:
        return socket.gethostname()

    def get_application_name(self) -> str:
        # Пример получения имени приложения
        app_name = self.context_provider.get_application_property('application.name')
        return app_name