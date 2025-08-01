# Sistema de Punto de Ventas (POS)

Un sistema de punto de ventas completo desarrollado en Python con Tkinter y SQLite para tienda pequeñas.

##  Características

- **Interfaz gráfica moderna** con Tkinter
- **Base de datos SQLite** para almacenamiento local
- **Gestión de productos** pronta implementacion de codigo de barras
- **Control de inventario** en tiempo real
- **Sistema de ventas** con tickets
- **Gestión de clientes**
- **Reportes básicos**
- **Configuración personalizable**

## Requisitos

- Python 3.8 o superior
- Tkinter (incluido con Python)
- SQLite3 (incluido con Python)

### Dependencias opcionales

```bash
pip install pillow>=9.0.0        # Para manejo de imágenes
pip install reportlab>=3.6.0     # Para generar reportes PDF
pip install python-dateutil>=2.8.0  # Para manejo de fechas
```

##  Estructura del Proyecto

```
POS-Factura/
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── config.json            # Configuración del sistema
├── src/                   # Código fuente
│   ├── config/           # Configuración
│   ├── controllers/      # Controladores
│   ├── database/         # Gestión de base de datos
│   ├── models/           # Modelos de datos
│   ├── utils/            # Utilidades
│   ├── views/            # Interfaces de usuario
│   └── assets/           # Recursos (imágenes, íconos)
├── database/             # Base de datos SQLite
├── tests/                # Pruebas unitarias
└── docs/                 # Documentación
```

##  Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd POS-Factura
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```

##  Funcionalidades Principales

### Gestión de Productos
- Agregar, editar y eliminar productos
- Códigos de barras únicos
- Control de stock
- Categorización de productos

### Sistema de Ventas
- Interfaz de venta rápida
- Escaneo de códigos de barras
- Cálculo automático de totales
- Impresión de tickets

### Inventario
- Control de stock en tiempo real
- Alertas de stock bajo
- Movimientos de inventario

### Reportes
- Ventas por período
- Productos más vendidos
- Estado del inventario

##  Configuración

El sistema se configura a través del archivo `config.json` que se crea automáticamente en el primer uso.

### Configuración de Negocio
```json
{
  "business": {
    "name": "Mi Tienda",
    "address": "Dirección de la tienda",
    "phone": "123-456-7890",
    "tax_id": "RFC123456789"
  }
}
```

## 🗄️ Base de Datos

El sistema utiliza SQLite con las siguientes tablas principales:

- **products**: Información de productos
- **categories**: Categorías de productos
- **customers**: Datos de clientes
- **sales**: Registro de ventas
- **sale_items**: Detalles de ventas
- **users**: Usuarios del sistema

## 🧪 Pruebas

```bash
# Ejecutar pruebas
pytest tests/

# Ejecutar pruebas con cobertura
pytest --cov=src tests/
```

##  Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

##  Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

##  Soporte

Para soporte técnico o preguntas, por favor contacta al desarrollador.

##  Roadmap

- [ ] Sistema de usuarios y autenticación
- [ ] Múltiples métodos de pago
- [ ] Integración con impresoras térmicas
- [ ] Backup automático de base de datos
- [ ] Reportes avanzados
- [ ] Integración con proveedores
- [ ] Aplicación web complementaria

---

**Desarrollado por Diegod**