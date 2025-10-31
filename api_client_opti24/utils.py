import hashlib
import calendar
import json
from datetime import date
from .errors import APIError
from aiogram import types


def hash_password(password: str) -> str:
    """SHA-512 хэш пароля в нижнем регистре."""
    return hashlib.sha512(password.encode()).hexdigest().lower()


def scrub(text: str) -> str:
    return text.replace("password", "***")


def validate_month_span(date_from: str, date_to: str):
    """Проверка, что разница между датами не больше месяца."""
    d_from = date.fromisoformat(date_from)
    d_to = date.fromisoformat(date_to)
    if d_to < d_from:
        raise APIError(3, "date_to не может быть меньше date_from")

    days_in_month = calendar.monthrange(d_from.year, d_from.month)[1]
    if (d_to - d_from).days > days_in_month:
        raise APIError(3, f"Разница между датами превышает {days_in_month} дней")


from datetime import datetime


def format_date_russian(date_str: str) -> str:
    # Словарь русских названий месяцев
    months = {
        1: "января", 2: "февраля", 3: "марта",
        4: "апреля", 5: "мая", 6: "июня",
        7: "июля", 8: "августа", 9: "сентября",
        10: "октября", 11: "ноября", 12: "декабря"
    }

    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    day = date_obj.day
    month = months[date_obj.month]
    year = date_obj.year

    return f"{day} {month} {year} года"


def format_number(number: float | int | None) -> str:
    if number is None:
        return "—"
    try:
        return "{:,.2f}".format(float(number)).replace(",", " ")
    except (ValueError, TypeError):
        return "—"


def print_json(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))
