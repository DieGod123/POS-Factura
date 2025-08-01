# -*- coding: utf-8 -*-
"""
Utilidades y funciones helper para el sistema POS
"""

import re
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP


def format_currency(amount):
    """Formatear cantidad como moneda"""
    try:
        amount = Decimal(str(amount))
        return f"${amount:.2f}"
    except:
        return "$0.00"


def validate_email(email):
    """Validar formato de email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_phone(phone):
    """Validar formato de teléfono"""
    # Remover espacios y caracteres especiales
    phone = re.sub(r'[\s\-\(\)]', '', phone)
    # Validar que solo contenga números y tenga longitud válida
    return phone.isdigit() and len(phone) >= 7


def validate_barcode(barcode):
    """Validar código de barras"""
    # Código de barras debe tener entre 8 y 13 dígitos
    return barcode.isdigit() and 8 <= len(barcode) <= 13


def get_current_datetime():
    """Obtener fecha y hora actual formateada"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate_tax(amount, tax_rate=0.16):
    """Calcular impuesto sobre una cantidad"""
    try:
        amount = Decimal(str(amount))
        tax_rate = Decimal(str(tax_rate))
        tax = amount * tax_rate
        return float(tax.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
    except:
        return 0.0


def calculate_discount(amount, discount_percent):
    """Calcular descuento sobre una cantidad"""
    try:
        amount = Decimal(str(amount))
        discount_percent = Decimal(str(discount_percent))
        discount = amount * (discount_percent / 100)
        return float(discount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
    except:
        return 0.0


def generate_receipt_number():
    """Generar número de ticket único"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"TKT-{timestamp}"


def sanitize_filename(filename):
    """Sanitizar nombre de archivo"""
    # Remover caracteres especiales
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Limitar longitud
    if len(filename) > 100:
        filename = filename[:100]
    return filename


def format_datetime_for_display(datetime_str):
    """Formatear fecha y hora para mostrar"""
    try:
        dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        return dt.strftime("%d/%m/%Y %H:%M")
    except:
        return datetime_str 