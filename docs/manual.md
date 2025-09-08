# Manual de Usuario - Proyecto Demo Conflictos Merge

## Introducción

Este manual describe cómo usar el proyecto de demostración para conflictos de merge en GitHub.

## Instalación

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd EJEMPLO\ ERROR\ MERGE
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso Básico

### Ejecutar la Aplicación

Para ejecutar la aplicación principal:

```bash
python src/main.py
```

### Configuración

La aplicación utiliza el archivo `src/config.json` para su configuración. Los parámetros principales son:

- **puerto**: Puerto donde se ejecuta la aplicación (por defecto: 8080)
- **debug**: Modo de depuración (por defecto: false)
- **timeout**: Tiempo de espera en segundos (por defecto: 30)

## Funcionalidades

### Calculadora Simple

La función principal permite realizar cálculos básicos:

```python
resultado = calcular_resultado(10, 20)
print(f"Resultado: {resultado}")
```

### Gestión de Configuración

Carga y valida la configuración del sistema:

```python
from utils import cargar_configuracion
config = cargar_configuracion("src/config.json")
```

## Resolución de Problemas

### Error: Archivo de configuración no encontrado

Asegúrate de que el archivo `src/config.json` existe y tiene el formato correcto.

### Error: Dependencias faltantes

Ejecuta `pip install -r requirements.txt` para instalar todas las dependencias.

## Contribuir

Para contribuir al proyecto:

1. Crea una nueva rama
2. Realiza tus cambios
3. Ejecuta las pruebas
4. Envía un pull request

---

*Última actualización: 8 de septiembre de 2025*
