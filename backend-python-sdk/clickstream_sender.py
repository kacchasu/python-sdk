import asyncio
import aiohttp
from aiohttp import ClientSession
import logging
from typing import List

class clickstream_sender:
    def __init__(self, request_service, validator, max_request_size: int):
        self._invalid_status_codes = [556, 557]
        self._http_client = ClientSession()
        self.request_service = request_service
        self.validator = validator
        self.available_threads_size = asyncio.Semaphore(max_request_size)

    async def send_async(self, request_data: dict) -> int:
        async with self._http_client.post(request_data['url'], json=request_data['data']) as response:
            status = response.status
            if status >= 200 and status < 300:
                return status
            else:
                logging.error(f"Failed to send event asynchronously. Response status code: {status}")
                return status if status not in self._invalid_status_codes else 400

    async def process_async_send(self, request_data: dict):
        logging.debug(f"Sending event to remote Clickstream server: {request_data['title']}")
        status_code = await self.send_async(request_data)
        async with self.available_threads_size:
            if status_code >= 300 and status_code not in self._invalid_status_codes:
                await self.request_service.add_request(request_data)

    async def scheduled_send(self):
        while True:
            await asyncio.sleep(1)  # Replace with actual interval configuration
            async with self.available_threads_size:
                request_data = await self.request_service.poll_request()
                if request_data:
                    await self.process_async_send(request_data)
                else:
                    break

    async def create_send_request(self, event: dict):
        self.validator.validate(event)
        request_data = self.request_service.create_request_data(event)
        if request_data:
            await self.process_async_send(request_data)

    # Метод для закрытия клиентской сессии при завершении работы
    async def close(self):
        await self._http_client.close()

# Пример использования
async def main():
    # Предполагается, что request_service и validator уже определены
    sender = clickstream_sender(request_service, validator, max_request_size=10)
    event = {'url': 'http://example.com/events', 'title': 'Test Event', 'data': {'key': 'value'}}
    await sender.create_send_request(event)
    await sender.scheduled_send()  # Должен быть запущен в фоновом режиме или в отдельном потоке
    await sender.close()

if __name__ == '__main__':
    asyncio.run(main())
