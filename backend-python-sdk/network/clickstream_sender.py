import asyncio
import aiohttp
from aiohttp import ClientSession


class ClickstreamSenderImpl:
    INVALID_STATUS_CODES = {556, 557}

    def __init__(self, request_service, validator, max_request_size, send_interval):
        self.request_service = request_service
        self.validator = validator
        self.max_request_size = max_request_size
        self.send_interval = send_interval
        self.session = None  # aiohttp client session

    async def create_and_send_request(self, clickstream_event):
        # Validate the event
        await self.validator.validate(clickstream_event)

        # Create the request bean
        request_bean = await self.request_service.create_request_bean(clickstream_event)

        if request_bean:
            await self.process_async_send(request_bean)

    async def send_async(self, request_bean):
        async with self.session.post(request_bean.url, json=request_bean.data,
                                     headers=request_bean.headers) as response:
            status = response.status
            if status in self.INVALID_STATUS_CODES or status >= 300:
                # Handle invalid status code, e.g., requeue or log
                print(f'Invalid status code received: {status}')
            return status

    async def process_async_send(self, request_bean):
        await self.send_async(request_bean)

    async def scheduled_send(self):
        while True:
            # Implement logic to get request from the queue
            request_bean = None  # Replace with actual method to get the request bean

            if request_bean:
                await self.process_async_send(request_bean)
            await asyncio.sleep(self.send_interval)

    async def start(self):
        self.session = ClientSession()
        asyncio.create_task(self.scheduled_send())

    async def stop(self):
        await self.session.close()
