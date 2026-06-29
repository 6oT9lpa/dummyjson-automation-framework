# DummyJSON API Automation Framework

API-проверки для публичного сервиса [DummyJSON](https://dummyjson.com). Проект оформлен как API automation framework: конфигурация и тестовые данные вынесены в `data`, API-слой построен через доменные клиенты, модели запросов/ответов и сервисы.

## Опыт

- Опыт ручного тестирования: есть базовый опыт проверки требований, составления тест-кейсов, чек-листов и заведения дефектов.
- Опыт нагрузочного тестирования: есть базовый опыт и понимание основных метрик: время отклика, количество запросов, ошибки и стабильность системы под нагрузкой.
- Опыт тестирования безопасности: есть базовый опыт проверок авторизации, работы с токенами, негативных сценариев и контроля доступа.

## Инструменты

- Python 3.10+
- pytest
- requests
- pydantic

## Структура

```text
framework/
├── api/
│   ├── clients/      # BaseApiClient, AuthApiClient, CartsApiClient
│   ├── models/       # Pydantic request/response schemas
│   ├── response/     # ApiResponse wrapper
│   └── services/     # API-flow helpers
├── core/             # config, logger, singleton
├── models/           # config/test data schemas
└── utils/            # JSON data loader

tests/
└── api/
    ├── auth/
    └── carts/
```

`BaseApiClient` инкапсулирует HTTP-логику, сессию, таймауты и логирование. `base_url` и `timeout` берутся через `ConfigManager().config` из `data/config.json`. Тестовые данные берутся через `TestDataManager` из `data/test_data.json` и валидируются Pydantic-моделями.

## Установка

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt
```

## Запуск

```bash
pytest
```

Запуск только API-проверок:

```bash
pytest tests/api -v
```

## Реализованные проверки

- `POST /auth/login` — успешная авторизация пользователя.
- `POST /auth/login` — неуспешная авторизация с неверным паролем.
- `GET /auth/me` — получение текущего пользователя с bearer-токеном.
- `GET /auth/me` — отказ при запросе без токена.
- `GET /carts/user/{userId}` — получение корзин пользователя.
- `GET /carts/{cartId}` — получение корзины по id.
- `POST /carts/add` — создание корзины.
- `PUT /carts/{cartId}` — обновление корзины.
- `DELETE /carts/{cartId}` — удаление корзины.
- `GET /carts/{cartId}` — негативная проверка для несуществующей корзины.

## Примечания

DummyJSON имитирует изменение данных для `POST`, `PUT` и `DELETE`: ответ возвращает результат операции, но состояние не сохраняется между запросами. Поэтому проверки для создания, обновления и удаления валидируют контракт ответа конкретного запроса.
