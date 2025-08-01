# -*- coding: utf-8 -*-
"""
Ventana principal del sistema POS
"""

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont


class MainWindow:
    """Clase para la ventana principal del sistema POS"""
    
    def __init__(self, root, db_manager):
        self.root = root
        self.db_manager = db_manager
        self.current_user = None
        
        # Configurar el estilo
        self.setup_styles()
        
        # Crear la interfaz
        self.create_widgets()
        
        # Configurar eventos
        self.setup_events()
    
    def setup_styles(self):
        """Configurar estilos de la interfaz"""
        style = ttk.Style()
        
        # Configurar tema
        style.theme_use('clam')
        
        # Configurar fuentes
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=10)
        
        # Configurar colores
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Success.TButton', background='green', foreground='white')
        style.configure('Danger.TButton', background='red', foreground='white')
    
    def create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        
        # Título principal
        title_label = ttk.Label(
            self.main_frame, 
            text="Sistema de Punto de Ventas", 
            style='Title.TLabel'
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Frame de botones principales
        self.create_main_buttons()
        
        # Frame de información
        self.create_info_frame()
        
        # Frame de estado
        self.create_status_frame()
    
    def create_main_buttons(self):
        """Crear botones principales"""
        buttons_frame = ttk.LabelFrame(self.main_frame, text="Operaciones Principales", padding="10")
        buttons_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Configurar grid del frame de botones
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)
        buttons_frame.columnconfigure(2, weight=1)
        buttons_frame.columnconfigure(3, weight=1)
        
        # Botones principales
        self.btn_sale = ttk.Button(
            buttons_frame, 
            text="Nueva Venta", 
            command=self.open_sale_window,
            style='Success.TButton'
        )
        self.btn_sale.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.btn_products = ttk.Button(
            buttons_frame, 
            text="Productos", 
            command=self.open_products_window
        )
        self.btn_products.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.btn_reports = ttk.Button(
            buttons_frame, 
            text="Reportes", 
            command=self.open_reports_window
        )
        self.btn_reports.grid(row=0, column=2, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.btn_settings = ttk.Button(
            buttons_frame, 
            text="Configuración", 
            command=self.open_settings_window
        )
        self.btn_settings.grid(row=0, column=3, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Segunda fila de botones
        self.btn_customers = ttk.Button(
            buttons_frame, 
            text="Clientes", 
            command=self.open_customers_window
        )
        self.btn_customers.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.btn_inventory = ttk.Button(
            buttons_frame, 
            text="Inventario", 
            command=self.open_inventory_window
        )
        self.btn_inventory.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.btn_users = ttk.Button(
            buttons_frame, 
            text="Usuarios", 
            command=self.open_users_window
        )
        self.btn_users.grid(row=1, column=2, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.btn_exit = ttk.Button(
            buttons_frame, 
            text="Salir", 
            command=self.exit_application,
            style='Danger.TButton'
        )
        self.btn_exit.grid(row=1, column=3, padx=5, pady=5, sticky=(tk.W, tk.E))
    
    def create_info_frame(self):
        """Crear frame de información"""
        info_frame = ttk.LabelFrame(self.main_frame, text="Información del Sistema", padding="10")
        info_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Información básica
        ttk.Label(info_frame, text="Versión: 1.0.0").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(info_frame, text="Base de datos: SQLite").grid(row=1, column=0, sticky=tk.W)
        ttk.Label(info_frame, text="Usuario actual: No autenticado").grid(row=2, column=0, sticky=tk.W)
    
    def create_status_frame(self):
        """Crear frame de estado"""
        status_frame = ttk.Frame(self.main_frame)
        status_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Barra de estado
        self.status_label = ttk.Label(status_frame, text="Sistema listo")
        self.status_label.pack(side=tk.LEFT)
        
        # Hora actual
        self.time_label = ttk.Label(status_frame, text="")
        self.time_label.pack(side=tk.RIGHT)
        
        # Actualizar hora
        self.update_time()
    
    def setup_events(self):
        """Configurar eventos de la aplicación"""
        # Evento de cierre de ventana
        self.root.protocol("WM_DELETE_WINDOW", self.exit_application)
        
        # Actualizar hora cada segundo
        self.root.after(1000, self.update_time)
    
    def update_time(self):
        """Actualizar la hora en la barra de estado"""
        from datetime import datetime
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)
    
    def open_sale_window(self):
        """Abrir ventana de nueva venta"""
        messagebox.showinfo("Nueva Venta", "Función de nueva venta - En desarrollo")
        # TODO: Implementar ventana de venta
    
    def open_products_window(self):
        """Abrir ventana de productos"""
        messagebox.showinfo("Productos", "Función de productos - En desarrollo")
        # TODO: Implementar ventana de productos
    
    def open_reports_window(self):
        """Abrir ventana de reportes"""
        messagebox.showinfo("Reportes", "Función de reportes - En desarrollo")
        # TODO: Implementar ventana de reportes
    
    def open_settings_window(self):
        """Abrir ventana de configuración"""
        messagebox.showinfo("Configuración", "Función de configuración - En desarrollo")
        # TODO: Implementar ventana de configuración
    
    def open_customers_window(self):
        """Abrir ventana de clientes"""
        messagebox.showinfo("Clientes", "Función de clientes - En desarrollo")
        # TODO: Implementar ventana de clientes
    
    def open_inventory_window(self):
        """Abrir ventana de inventario"""
        messagebox.showinfo("Inventario", "Función de inventario - En desarrollo")
        # TODO: Implementar ventana de inventario
    
    def open_users_window(self):
        """Abrir ventana de usuarios"""
        messagebox.showinfo("Usuarios", "Función de usuarios - En desarrollo")
        # TODO: Implementar ventana de usuarios
    
    def exit_application(self):
        """Salir de la aplicación"""
        if messagebox.askokcancel("Salir", "¿Está seguro que desea salir?"):
            self.root.quit() 