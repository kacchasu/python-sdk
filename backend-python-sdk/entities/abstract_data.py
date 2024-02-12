from dataclasses import dataclass, field
from typing import Dict


@dataclass
class AbstractData:
    # Предположим, что в AbstractData есть метод для получения data_map
    data_map: Dict[str, str] = field(default_factory=dict)

    def get_data_map(self) -> Dict[str, str]:
        return self.data_map