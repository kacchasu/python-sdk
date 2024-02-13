from queue import Queue
from typing import Optional
from ..entities.request_bean import RequestBean

class RequestRepository:
    def __init__(self, max_queue_size: int):
        self.requests = Queue(maxsize=max_queue_size)

    def add_request(self, request: RequestBean) -> None:
        if self.requests.full():
            # Здесь можно залогировать предупреждение, если очередь полна
            print(f"Too many requests to add. Request: {request.title} won't be sent.")
        else:
            self.requests.put(request)

    def poll_request(self) -> Optional[RequestBean]:
        if not self.requests.empty():
            return self.requests.get()
        else:
            return None
