#!/usr/bin/env python3

def saludar(nombre):
    """Función simple para saludar"""
    mensaje = f"¡Hola {nombre}! Bienvenido a mi aplicación"
    print(mensaje)
    print("¡Que tengas un excelente día!")  # Nueva línea de despedida
    return mensaje

def main():
    print("=== Mi Aplicación Simple ===")
    usuario = "Usuario"
    saludar(usuario)
    print("¡Gracias por usar la aplicación!")

if __name__ == "__main__":
    main()
