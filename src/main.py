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
    # RAMA FEATURE-CALCULADORA-AVANZADA: Implementación con multiplicación y validación
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los parámetros deben ser números")
    
    resultado = a * b  # Cambio a multiplicación
    print(f"Calculando (multiplicación avanzada): {a} * {b} = {resultado}")
    return resultado

def mostrar_mensaje():
    """
    Función que mostrará diferentes mensajes según la rama.
    """
    # RAMA FEATURE-CALCULADORA-AVANZADA: Mensaje específico para calculadora avanzada
    mensaje = "Calculadora Avanzada v2.0 - Con funciones matemáticas extendidas"
    print(f"Estado: {mensaje}")
    print("Características: Multiplicación, validación de tipos, manejo de errores")

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
    
    # RAMA FEATURE-CALCULADORA-AVANZADA: Números más grandes para pruebas
    num1 = 25
    num2 = 30
    
    resultado = calcular_resultado(num1, num2)
    mostrar_mensaje()
    configurar_aplicacion()
    
    print(f"Resultado final: {resultado}")
    print("Programa terminado exitosamente.")
