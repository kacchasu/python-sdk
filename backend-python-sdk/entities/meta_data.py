from dataclasses import dataclass
from datetime import datetime, timezone, timedelta

from abstract_data import AbstractData

@dataclass
class MetaData(AbstractData):
    def set_current_time_stamp(self):
        formatter = "%Y-%m-%dT%H:%M:%S.%f"
        # Предположим, что время необходимо сдвинуть на 3 часа вперед от UTC
        time_stamp = datetime.now(timezone(timedelta(hours=3))).strftime(formatter)[:-3] + "+03:00"
        self.get_data_map()["timeStamp"] = time_stamp
