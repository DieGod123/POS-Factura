#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de demostración del sistema POS completo
"""

import sys
import os

# Agregar el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.database_manager import DatabaseManager
from views.login_window import create_default_user


def demo_sistema():
    """Demostración del sistema completo"""
    print("🎯 DEMOSTRACIÓN DEL SISTEMA POS")
    print("=" * 50)
    
    try:
        # 1. Inicializar base de datos
        print("1️⃣ Inicializando base de datos...")
        db_manager = DatabaseManager()
        db_manager.initialize_database()
        print("   ✅ Base de datos creada correctamente")
        
        # 2. Crear usuario por defecto
        print("\n2️⃣ Creando usuario por defecto...")
        create_default_user()
        print("   ✅ Usuario admin creado")
        print("   📋 Credenciales: admin / admin123")
        
        # 3. Mostrar productos de ejemplo
        print("\n3️⃣ Productos de ejemplo cargados:")
        products = db_manager.get_all_products()
        for i, product in enumerate(products, 1):
            print(f"   {i}. {product[1]} - ${product[3]:.2f} - Stock: {product[5]}")
        
        # 4. Información del sistema
        print("\n4️⃣ Información del sistema:")
        print("   🖥️  Interfaz: Tkinter")
        print("   🗄️  Base de datos: SQLite")
        print("   🔐 Autenticación: SHA-256")
        print("   📦 Productos: 4 productos de ejemplo")
        
        print("\n🚀 El sistema está listo para usar!")
        print("💡 Ejecuta 'python main.py' para iniciar la aplicación")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en la demostración: {e}")
        return False


if __name__ == "__main__":
    demo_sistema() 