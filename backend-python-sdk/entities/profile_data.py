from dataclasses import dataclass
from datetime import datetime, timezone, timedelta

from abstract_data import AbstractData


@dataclass
class ProfileData(AbstractData):
    def set_current_session_id(self):
        formatter = "%Y-%m-%dT%H:%M:%S.%f"
        # Предположим, что время необходимо сдвинуть на 3 часа вперед от UTC
        time_stamp = datetime.now(timezone(timedelta(hours=3))).strftime(formatter)[:-3] + "+03:00"
        device_id = self.get_data_map().get("deviceId", "UNKNOWN")
        self.get_data_map()["sessionId"] = f"{time_stamp}_{device_id}"
