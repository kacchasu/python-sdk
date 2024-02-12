import socket

from ..entities.profile_data import ProfileData
class ProfileCollector:
    def __init__(self, context_provider, settings):
        self.context_provider = context_provider
        self.settings = settings

    def collect_data(self) -> ProfileData:
        profile_data = ProfileData(data_map={})
        app_version = self.context_provider.get_application_property('clickstream.appVersion')
        client_block = self.context_provider.get_application_property('clickstream.clientBlock')
        app_version_number = self.context_provider.get_application_property('clickstream.appVersionNumber')
        mac_address = self.get_mac_address()

        # Дополняем словарь значениями
        profile_data.data_map['appVersion'] = app_version if app_version else self.settings.get_app_version()
        profile_data.data_map['clientBlock'] = client_block if client_block else self.settings.get_client_block()
        profile_data.data_map[
            'appVersionNumber'] = app_version_number if app_version_number else self.settings.get_app_version_number()
        profile_data.data_map['deviceId'] = mac_address

        return profile_data

    def get_mac_address(self) -> str:
        # Пример получения MAC-адреса, на практике может потребоваться другой метод
        return ':'.join(['{:02x}'.format((socket.gethostbyname(socket.gethostname()))[i]) for i in range(6)])