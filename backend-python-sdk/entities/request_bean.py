from dataclasses import dataclass, field
from typing import Any

@dataclass
class RequestBean:
    is_sensitive: bool
    title: str
    request: Any  # В Python HttpRequest может быть из библиотеки requests, aiohttp или другой
    retry_count: int = field(default=0, init=False)  # init=False говорит о том, что это поле не используется в конструкторе

    def increment_retry_count(self):
        self.retry_count += 1
