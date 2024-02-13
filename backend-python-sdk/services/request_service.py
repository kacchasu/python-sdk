from ..entities.request_bean import RequestBean


class ClickstreamValidationException(Exception):
    pass


class JsonRequestBodyException(Exception):
    pass


class RequestService:
    def __init__(self, request_processor, settings, request_repository, url="UNKNOWN", max_retry_count=0):
        self.request_processor = request_processor
        self.settings = settings
        self.request_repository = request_repository
        self.url = url or self.settings.get_url()
        self.max_retry_count = max_retry_count

    def check_url(self):
        if self.url == "UNKNOWN":
            self.url = self.settings.get_url()

    def create_request_bean(self, clickstream_event):
        self.check_url()
        try:
            request = self.request_processor.prepare_request(self.url, [clickstream_event])
            is_sensitive = clickstream_event.event_type == "SENSITIVE"
            request_bean = RequestBean(is_sensitive, clickstream_event.event_action, request)

            if request_bean.is_sensitive:
                return request_bean
            else:
                self.request_repository.add_request(request_bean)
                return request_bean
        except (ClickstreamValidationException, JsonRequestBodyException) as e:
            # Replace print with logging in real application
            print(f"Event: {clickstream_event.event_action} won't be sent")
            return None

    def poll_request(self):
        return self.request_repository.poll_request()

    def add_request(self, request_bean):
        if request_bean.is_sensitive:
            # Replace print with logging in real application
            print(f"Request: {request_bean.title} has sensitive data. It will not be re-sent.")
        elif request_bean.retry_count < self.max_retry_count:
            print(f"Failed to send event: {request_bean.title}, re-adding to queue")
            request_bean.increment_retry_count()
            new_request = self.request_processor.prepare_request_for_resend(self.url, request_bean.request)
            request_bean.set_request(new_request)
            self.request_repository.add_request(request_bean)
        else:
            print(f"Request: {request_bean.title} reached maximum retry attempts. Discarding.")
