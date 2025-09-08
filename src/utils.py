"""
Utilidades compartidas para el proyecto de demostración.
Este archivo también puede tener conflictos menores.
"""

import json
import logging

def cargar_configuracion(archivo_config="config.json"):
    """
    Carga la configuración desde un archivo JSON.
    
    Args:
        archivo_config (str): Ruta al archivo de configuración
    
    Returns:
        dict: Configuración cargada
    """
    try:
        with open(archivo_config, 'r', encoding='utf-8') as f:
            config = json.load(f)
        logging.info(f"Configuración cargada desde {archivo_config}")
        return config
    except FileNotFoundError:
        logging.error(f"Archivo de configuración {archivo_config} no encontrado")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Error al parsear JSON en {archivo_config}")
        return {}

def validar_entrada(valor, tipo_esperado=int):
    """
    Valida que la entrada sea del tipo esperado.
    
    Args:
        valor: Valor a validar
        tipo_esperado: Tipo de dato esperado
    
    Returns:
        bool: True si es válido, False en caso contrario
    """
    # Esta función será modificada en diferentes ramas
    if isinstance(valor, tipo_esperado):
        return True
    else:
        logging.warning(f"Valor {valor} no es del tipo {tipo_esperado}")
        return False

def formatear_salida(datos):
    """
    Formatea los datos para mostrar.
    
    Args:
        datos: Datos a formatear
    
    Returns:
        str: Datos formateados
    """
    # Este formato será diferente en cada rama
    if isinstance(datos, dict):
        return json.dumps(datos, indent=2, ensure_ascii=False)
    else:
        return str(datos)

# Constantes que también causarán conflictos
VERSION_UTILS = "1.0.0"
AUTOR = "Desarrollador Principal"
FECHA_CREACION = "2025-09-08"
