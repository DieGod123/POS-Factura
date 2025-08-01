#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Punto de Ventas (POS)
Autor: Diego
Versión: 1.0.0
"""

import tkinter as tk
from tkinter import ttk
import sys
import os

# Agregar el directorio src al path para importar módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from views.main_window import MainWindow
from views.login_window import LoginWindow, create_default_user
from database.database_manager import DatabaseManager
from config.settings import Settings


class POSApplication:
    """Clase principal de la aplicación POS"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.settings = Settings()
        self.db_manager = DatabaseManager()
        self.current_user = None
        
        # Configurar la ventana principal
        self.setup_main_window()
        
        # Inicializar la base de datos
        self.db_manager.initialize_database()
        
        # Crear usuario por defecto si no existe
        create_default_user()
        
        # Mostrar login antes de la aplicación principal
        self.show_login()
    
    def show_login(self):
        """Mostrar ventana de login"""
        login_window = LoginWindow(self.root)
        user_data = login_window.run()
        
        if user_data:
            self.current_user = user_data
            self.create_main_application()
        else:
            # Si no se autenticó, cerrar la aplicación
            self.root.destroy()
    
    def create_main_application(self):
        """Crear la aplicación principal después del login exitoso"""
        # Crear la ventana principal
        self.main_window = MainWindow(self.root, self.db_manager, self.current_user)
        
        # Actualizar información del usuario en la ventana principal
        if hasattr(self.main_window, 'update_user_info'):
            self.main_window.update_user_info(self.current_user)
    
    def setup_main_window(self):
        """Configurar la ventana principal"""
        self.root.title("Sistema de Punto de Ventas")
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)
        
        # Centrar la ventana en la pantalla
        self.center_window()
        
        # Configurar el ícono (opcional)
        # self.root.iconbitmap('src/assets/icons/pos_icon.ico')
    
    def center_window(self):
        """Centrar la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def run(self):
        """Ejecutar la aplicación"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\nAplicación cerrada por el usuario")
        except Exception as e:
            print(f"Error en la aplicación: {e}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Limpiar recursos antes de cerrar"""
        if hasattr(self, 'db_manager'):
            self.db_manager.close_connection()


def main():
    """Función principal"""
    print("Iniciando Sistema de Punto de Ventas...")
    
    try:
        app = POSApplication()
        app.run()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 