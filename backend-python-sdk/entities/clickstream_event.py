from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from typing import List, Dict, Optional
from analytics_property import AnalyticsProperty


@dataclass
class ClickstreamEvent:
    event_action: str
    event_type: Optional[str] = None  # Пример, в оригинале это перечисление (enum)
    properties: List[AnalyticsProperty] = field(default_factory=list)
    timestamp: str = field(init=False)

    def __post_init__(self):
        formatter = '%Y-%m-%dT%H:%M:%S.%f'
        self.timestamp = datetime.now(timezone(timedelta(hours=3))).strftime(formatter)[:-3] + "+03:00"

    def add_property(self, key: str, value: str):
        self.properties.append(AnalyticsProperty(key, value))

    def add_properties(self, new_properties: Dict[str, str]):
        for key, value in new_properties.items():
            self.add_property(key, value)

