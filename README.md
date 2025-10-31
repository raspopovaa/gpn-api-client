# ⛽ APIClientOPTI24 
· Python SDK для Газпромнефть

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/github/actions/workflow/status/your-username/gpn-api-client/ci.yml)
![Downloads](https://img.shields.io/pypi/dm/gpn-api-client)
[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?raspopovaa=anuraghazra)](https://github.com/anuraghazra/github-readme-stats)

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
from gpn_api_client import GPNClient
from gpn_api_client.models import CardFilter

# 1. Инициализация клиента
client = GPNClient(
    base_url="https://api.example.com",
    api_key="your-api-key",
    login="your-login", 
    password="your-password"
)

# 2. Аутентификация
client.authenticate()

# 3. Работа с API
cards = client.cards.get_list(
    filter=CardFilter(status="ACTIVE"),
    page=1,
    on_page=10
)

print(f"🎉 Найдено {len(cards['data'])} активных карт!")
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

## ⚠️ Поддержка

- 🐛 [Баги и issues](https://github.com/your-username/gpn-api-client/issues)
- 💬 [Обсуждения](https://github.com/your-username/gpn-api-client/discussions)
- 📧 Email: your-email@example.com

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2R0ZzZ0ZzZ0ZzZ0ZzZ0ZzZ0ZzZ0ZzZ0ZzZ0ZzZ0ZzZ0ZzZ0JlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKsQ8UQ4l4LhGz6/giphy.gif" width="150" alt="Support Animation">
  <br>
  <b>Happy coding! 🚀</b>
</p>
```

