#!/usr/bin/env python3
"""
Aplicación principal para demostrar conflictos de merge.
Este archivo será modificado en diferentes ramas para crear conflictos.
"""

def calcular_resultado(a, b):
    """
    Función que será modificada para causar conflictos de merge.
    
    Args:
        a (int): Primer número
        b (int): Segundo número
    
    Returns:
        int: Resultado de la operación
    """
    # Esta línea será modificada en diferentes ramas
    resultado = a + b
    print(f"Calculando: {a} + {b} = {resultado}")
    return resultado

def mostrar_mensaje():
    """
    Función que mostrará diferentes mensajes según la rama.
    """
    # Este mensaje será diferente en cada rama
    mensaje = "Versión inicial del proyecto"
    print(f"Estado: {mensaje}")

def configurar_aplicacion():
    """
    Configuración que causará conflictos.
    """
    # Estas configuraciones serán diferentes en cada rama
    version = "1.0.0"
    debug = False
    
    print(f"Aplicación versión {version}, Debug: {debug}")

if __name__ == "__main__":
    print("=== Demostración de Conflictos de Merge ===")
    
    # Estas líneas también serán modificadas
    num1 = 10
    num2 = 20
    
    resultado = calcular_resultado(num1, num2)
    mostrar_mensaje()
    configurar_aplicacion()
    
    print(f"Resultado final: {resultado}")
    print("Programa terminado exitosamente.")
