# -*- coding: utf-8 -*-
"""
Ventana de login para autenticación de usuarios
"""

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont
import hashlib
import sqlite3
from src.config.settings import DB_PATH


class LoginWindow:
    """Clase para la ventana de login"""
    
    def __init__(self, parent=None):
        self.parent = parent
        self.user_data = None
        
        # Crear ventana de login
        self.create_login_window()
        
    def create_login_window(self):
        """Crear la ventana de login"""
        self.login_window = tk.Toplevel() if self.parent else tk.Tk()
        
        # Configurar ventana
        self.login_window.title("Iniciar Sesión - Sistema POS")
        self.login_window.geometry("400x300")
        self.login_window.resizable(False, False)
        
        # Centrar ventana
        self.center_window()
        
        # Configurar estilo
        self.setup_styles()
        
        # Crear widgets
        self.create_widgets()
        
        # Configurar eventos
        self.setup_events()
        
        # Hacer la ventana modal si hay parent
        if self.parent:
            self.login_window.transient(self.parent)
            self.login_window.grab_set()
    
    def center_window(self):
        """Centrar la ventana en la pantalla"""
        self.login_window.update_idletasks()
        width = self.login_window.winfo_width()
        height = self.login_window.winfo_height()
        x = (self.login_window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.login_window.winfo_screenheight() // 2) - (height // 2)
        self.login_window.geometry(f'{width}x{height}+{x}+{y}')
    
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
        style.configure('Login.TButton', font=('Arial', 10, 'bold'))
    
    def create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        
        # Frame principal
        main_frame = ttk.Frame(self.login_window, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.login_window.columnconfigure(0, weight=1)
        self.login_window.rowconfigure(0, weight=1)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="Sistema de Punto de Ventas", 
            style='Title.TLabel'
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        # Subtítulo
        subtitle_label = ttk.Label(
            main_frame, 
            text="Iniciar Sesión", 
            font=('Arial', 12)
        )
        subtitle_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # Usuario
        ttk.Label(main_frame, text="Usuario:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.username_entry = ttk.Entry(main_frame, width=30)
        self.username_entry.grid(row=2, column=1, padx=(10, 0), pady=5, sticky=(tk.W, tk.E))
        
        # Contraseña
        ttk.Label(main_frame, text="Contraseña:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.password_entry = ttk.Entry(main_frame, width=30, show="*")
        self.password_entry.grid(row=3, column=1, padx=(10, 0), pady=5, sticky=(tk.W, tk.E))
        
        # Frame de botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=(30, 0))
        
        # Botón de login
        self.login_button = ttk.Button(
            button_frame, 
            text="Iniciar Sesión", 
            command=self.authenticate_user,
            style='Login.TButton'
        )
        self.login_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Botón de cancelar
        self.cancel_button = ttk.Button(
            button_frame, 
            text="Cancelar", 
            command=self.cancel_login
        )
        self.cancel_button.pack(side=tk.LEFT)
        
        # Configurar columnas del main_frame
        main_frame.columnconfigure(1, weight=1)
        
        # Enfocar en el campo de usuario
        self.username_entry.focus()
        
        # Bind Enter key
        self.login_window.bind('<Return>', lambda e: self.authenticate_user())
        self.login_window.bind('<Escape>', lambda e: self.cancel_login())
    
    def setup_events(self):
        """Configurar eventos de la ventana"""
        # Evento de cierre de ventana
        self.login_window.protocol("WM_DELETE_WINDOW", self.cancel_login)
    
    def hash_password(self, password):
        """Hashear contraseña"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def authenticate_user(self):
        """Autenticar usuario"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        # Validar campos
        if not username or not password:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return
        
        try:
            # Conectar a la base de datos
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            
            # Hashear contraseña
            hashed_password = self.hash_password(password)
            
            # Verificar credenciales
            cursor.execute(
                "SELECT username, rol FROM usuarios WHERE username=? AND password=?",
                (username, hashed_password)
            )
            result = cursor.fetchone()
            
            conn.close()
            
            if result:
                self.user_data = {
                    "username": result[0],
                    "rol": result[1]
                }
                messagebox.showinfo("Éxito", f"Bienvenido, {username}!")
                self.login_window.destroy()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
                self.password_entry.delete(0, tk.END)
                self.password_entry.focus()
                
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión: {e}")
    
    def cancel_login(self):
        """Cancelar login"""
        if messagebox.askokcancel("Salir", "¿Está seguro que desea salir?"):
            self.user_data = None
            self.login_window.destroy()
    
    def get_user_data(self):
        """Obtener datos del usuario autenticado"""
        return self.user_data
    
    def run(self):
        """Ejecutar la ventana de login"""
        if not self.parent:
            self.login_window.mainloop()
        else:
            self.login_window.wait_window()
            # Esperar a que la ventana se cierre antes de retornar
            self.login_window.update()
        return self.user_data


def create_default_user():
    """Crear usuario por defecto si no existe"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Verificar si existe la tabla usuarios
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                rol TEXT NOT NULL CHECK(rol IN ('admin', 'usuario')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Verificar si existe el usuario admin
        cursor.execute("SELECT username FROM usuarios WHERE username='admin'")
        if not cursor.fetchone():
            # Crear usuario admin por defecto
            hashed_password = hashlib.sha256("admin123".encode()).hexdigest()
            cursor.execute(
                "INSERT INTO usuarios (username, password, rol) VALUES (?, ?, ?)",
                ("admin", hashed_password, "admin")
            )
            print("Usuario admin creado por defecto")
            print("Usuario: admin")
            print("Contraseña: admin123")
        
        conn.commit()
        conn.close()
        
    except Exception as e:
        print(f"Error al crear usuario por defecto: {e}")


if __name__ == "__main__":
    # Crear usuario por defecto
    create_default_user()
    
    # Ejecutar ventana de login
    login = LoginWindow()
    user_data = login.run()
    
    if user_data:
        print(f"Usuario autenticado: {user_data}")
    else:
        print("Login cancelado")
