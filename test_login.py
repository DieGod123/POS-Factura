#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para el sistema de login
"""

import sys
import os

# Agregar el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from views.login_window import LoginWindow, create_default_user
from database.database_manager import DatabaseManager


def test_database_creation():
    """Probar la creación de la base de datos"""
    print("=== Probando creación de base de datos ===")
    
    try:
        db_manager = DatabaseManager()
        db_manager.initialize_database()
        print("✅ Base de datos creada correctamente")
        
        # Probar obtener productos
        products = db_manager.get_all_products()
        print(f"✅ Productos cargados: {len(products)} productos")
        
        return True
    except Exception as e:
        print(f"❌ Error al crear base de datos: {e}")
        return False


def test_user_creation():
    """Probar la creación de usuarios"""
    print("\n=== Probando creación de usuarios ===")
    
    try:
        create_default_user()
        print("✅ Usuario por defecto creado correctamente")
        print("   Usuario: admin")
        print("   Contraseña: admin123")
        return True
    except Exception as e:
        print(f"❌ Error al crear usuario: {e}")
        return False


def test_login():
    """Probar el sistema de login"""
    print("\n=== Probando sistema de login ===")
    
    try:
        # Crear ventana de login
        login = LoginWindow()
        user_data = login.run()
        
        if user_data:
            print(f"✅ Login exitoso: {user_data}")
            return True
        else:
            print("❌ Login cancelado o fallido")
            return False
    except Exception as e:
        print(f"❌ Error en login: {e}")
        return False


def main():
    """Función principal de pruebas"""
    print("🧪 Iniciando pruebas del sistema de login...\n")
    
    # Ejecutar pruebas
    tests = [
        test_database_creation,
        test_user_creation,
        test_login
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Resultados: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("🎉 ¡Todas las pruebas pasaron!")
    else:
        print("⚠️  Algunas pruebas fallaron")


if __name__ == "__main__":
    main() 