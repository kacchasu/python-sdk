import json
from typing import List, Dict, Any
from ..dto.analytics_data import AnalyticsData
from ..entities.analytics_entity import AnalyticsEntity
class HttpRequestProcessor:
    def __init__(self, meta_profile_repository):
        self.meta_profile_repository = meta_profile_repository

    def prepare_json_request_body(self, events: List[AnalyticsData]) -> str:
        analytics_entity = self.init_analytics_entity(events)

        # Предполагается, что метод to_dict() в AnalyticsEntity конвертирует данные в словарь
        analytics_entity_dict = analytics_entity.to_dict()

        # Конвертирование словаря в JSON строку
        return json.dumps(analytics_entity_dict)

    def init_analytics_entity(self, events: List[AnalyticsData]) -> AnalyticsEntity:
        # Инициализация и заполнение экземпляра AnalyticsEntity данными
        analytics_entity = AnalyticsEntity()
        # Допустим, метод add_events добавляет события в analytics_entity
        self.add_events(analytics_entity, events)
        return analytics_entity

    def add_events(self, analytics_entity: AnalyticsEntity, events: List[AnalyticsData]) -> None:
        # Добавление событий в экземпляр AnalyticsEntity
        for event in events:
            # Допустим, у analytics_entity есть метод add_data() для добавления данных
            analytics_entity.add_data(event)