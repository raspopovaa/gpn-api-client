
# ⛽ APIClientOPTI24
APIClient OPTI24 SDK — библиотека для работы с API топливных карт Газпромнефть. 
APIClient OPTI24 упрощает интеграцию с топливными картами для корпоративных клиентов.

APIClient OPTI24 поддерживает все основные функции API, доступного на opti-24.ru. 
Проект является независимой разработкой и не связан с АО «Газпром нефть». Использование API должно соответствовать официальным правилам.
**Веб-сайт:** [opti-24.ru](https://opti-24.ru)

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/github/actions/workflow/status/your-username/gpn-api-client/ci.yml)
![Downloads](https://img.shields.io/pypi/dm/gpn-api-client)



## 🚀 Возможности

| Группа | Методы | Эмодзи | Описание |
|--------|--------|--------|----------|
| **Аутентификация** | 5+ | 🔐 | Сессии, контракты, права доступа |
| **Топливные карты** | 15+ | 💳 | Балансы, блокировка, лимиты |
| **Транзакции** | 10+ | 💰 | История операций, детализация |
| **Отчеты** | 8+ | 📊 | Генерация, выгрузка, автоматизация |
| **Лимиты** | 12+ | 🚦 | Продуктовые и региональные ограничения |
| **Справочники** | 5+ | 📚 | ТНП, АЗС, регионы, услуги |


## 🚀 Быстрый старт

### 📦 Установка
```bash
pip install gpn-api-client
```

### ⚡ Минимальный пример
```python
import asyncio
from api_client_opti24 import *
from api_client_opti24.config import BASE_URL, API_KEY, LOGIN, PASSWORD

async def main():
    client = APIClient(
        base_url=BASE_URL,   # твой URL API
        api_key=API_KEY,
        login=LOGIN,
        password=PASSWORD
    )

    # Авторизация пользователя
    auth_response = await client.auth_user()
    print("===АВТОРИЗАЦИЯ===")
    print(auth_response.data.contracts[0])

    #Получение статистики
    info_response = await client.get_info()
    print("=== Cтатистика ===")
    print(info_response.data.client_info)
    print(info_response.data.methods)
    logoff_response = await client.logoff()
    
    print("=== LOGOFF ===")
    print(logoff_response)
if __name__ == "__main__":
        asyncio.run(main())
```

## 📖 Документация

### 🔧 Конфигурация
Создайте `.env` файл:
```env
API_BASE_URL=https://api-demo.opti-24.ru/vip/
API_KEY=your_api_key_here
API_LOGIN=your_login
API_PASSWORD=your_password
```

### 🎯 Основные возможности
```python
# 📋 Получение информации о договоре
contract_info = client.contracts.get_data()

# 💳 Работа с картами
cards = client.cards.get_list(status="ACTIVE")
client.cards.block(["card_id_1"], block=True)

# 💰 Транзакции
transactions = client.transactions.get_v2(
    date_from="2024-01-01", 
    date_to="2024-01-31"
)

# 📊 Отчеты
report = client.reports.order_v2(
    report_id="fuel-report",
    report_format="excel",
    params={"period": "month"}
)

# 🚦 Лимиты
limits = client.limits.get(contract_id="contract_123")
```

## 🛡️ Особенности

- **♻️ Автоповторы** при сбоях сети и rate limiting
- **✅ Валидация** данных через Pydantic v2
- **🔒 Безопасность** скрабинг чувствительных данных в логах
- **⚡ Idempotency** защита от дублирующих операций
- **📚 Типобезопасность** полная аннотация типов

## 🧪 Тестирование

```bash
# Установка для разработки
pip install -e ".[dev]"

# Запуск тестов
pytest tests/unit/ -v
pytest tests/integration/ -v
pytest tests/contract/ -v

# Проверка покрытия
pytest --cov=gpn_api_client tests/
```

## 🤝 Участие в разработке

1. 🍴 Форкните репозиторий
2. 🌿 Создайте feature ветку: `git checkout -b feature/amazing-feature`
3. 💾 Коммитьте изменения: `git commit -m 'Add amazing feature'`
4. 📤 Пушите в ветку: `git push origin feature/amazing-feature`
5. 🔄 Создайте Pull Request

## 📄 Лицензия

Распространяется под MIT лицензией. Смотрите [LICENSE](LICENSE) для деталей.

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=raspopovaa&show=reviews,discussions_started,discussions_answered,prs_merged,prs_merged_percentage)


## ⚠️ Поддержка

- 🐛 [Баги и issues](https://github.com/your-username/gpn-api-client/issues)
- 💬 [Обсуждения](https://github.com/your-username/gpn-api-client/discussions)
- 📧 Email: your-email@example.com


```

