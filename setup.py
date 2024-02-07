from setuptools import setup, find_packages

setup(
    name='my_python_sdk',  # Имя вашей библиотеки
    version='0.1.0',  # Текущая версия вашей библиотеки
    author='me',  # Ваше имя или имя организации
    description='SDK for collecting events and sending them to a server',  # Краткое описание
    packages=find_packages(exclude=('tests',)),  # Пакеты для включения в распространение (исключая тесты)
    install_requires=[  # Список зависимостей для автоматической установки
        'aiohttp>=3.7.4',
        'asyncio',
        'APScheduler',
        # Другие зависимости...
    ],
    extras_require={  # Дополнительные зависимости, которые могут быть установлены по желанию
        'dev': [
            'pytest'
            # Другие зависимости для разработки...
        ],
    },
    python_requires='>=3.6',  # Минимальная требуемая версия Python
    include_package_data=True,  # Включение не кодовых файлов из MANIFEST.in
)