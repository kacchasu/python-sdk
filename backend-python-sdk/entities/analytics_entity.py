from dataclasses import dataclass, field
from typing import Dict, List
from ..dto.analytics_data import AnalyticsData


@dataclass
class AnalyticsEntity:
    meta_params: Dict[str, str] = field(default_factory=dict)
    profile_params: Dict[str, str] = field(default_factory=dict)
    data_list: List[AnalyticsData] = field(default_factory=list)

    def add_data(self, analytics_data: AnalyticsData):
        if analytics_data is not None:
            # В Python список является потокобезопасным, поэтому нет необходимости
            # в явной синхронизации, как в Java. Однако, если вы будете использовать
            # этот список в многопоточном контексте, вам может понадобиться
            # внешняя синхронизация или другие потокобезопасные структуры данных.
            self.data_list.append(analytics_data)
