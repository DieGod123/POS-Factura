#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba simple para el sistema de login
"""

import sys
import os

# Agregar el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from views.login_window import create_default_user, LoginWindow


def test_login_simple():
    """Prueba simple del login"""
    print("=== Prueba Simple del Login ===")
    
    try:
        # Crear usuario por defecto
        create_default_user()
        print("✅ Usuario creado correctamente")
        
        # Crear ventana de login
        print("🔐 Abriendo ventana de login...")
        login = LoginWindow()
        user_data = login.run()
        
        if user_data:
            print(f"✅ Login exitoso: {user_data}")
            return True
        else:
            print("❌ Login cancelado")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    test_login_simple() 