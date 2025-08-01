# -*- coding: utf-8 -*-
"""
Configuración del sistema POS
"""

import os
import json
from pathlib import Path


class Settings:
    """Clase para manejar la configuración del sistema"""
    
    def __init__(self):
        self.config_file = "config.json"
        self.default_config = {
            "database": {
                "path": "database/pos_database.db"
            },
            "appearance": {
                "theme": "default",
                "font_size": 10,
                "window_size": "1200x800"
            },
            "business": {
                "name": "Mi Tienda",
                "address": "",
                "phone": "",
                "tax_id": ""
            },
            "receipt": {
                "header": "Sistema de Punto de Ventas",
                "footer": "¡Gracias por su compra!",
                "show_logo": False
            }
        }
        self.config = self.load_config()
    
    def load_config(self):
        """Cargar configuración desde archivo"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return self.default_config
        except Exception as e:
            print(f"Error al cargar configuración: {e}")
            return self.default_config
    
    def save_config(self):
        """Guardar configuración en archivo"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar configuración: {e}")
    
    def get(self, key, default=None):
        """Obtener valor de configuración"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key, value):
        """Establecer valor de configuración"""
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
        self.save_config()
    
    def get_database_path(self):
        """Obtener ruta de la base de datos"""
        return self.get('database.path', 'database/pos_database.db')
    
    def get_business_name(self):
        """Obtener nombre del negocio"""
        return self.get('business.name', 'Mi Tienda')
    
    def get_window_size(self):
        """Obtener tamaño de ventana"""
        return self.get('appearance.window_size', '1200x800') 