# Proyecto de Demostración: Conflictos de Merge en GitHub

Este proyecto está diseñado específicamente para demostrar y practicar la resolución de conflictos de merge en GitHub.

## ¿Qué es un conflicto de merge?

Un conflicto de merge ocurre cuando Git no puede fusionar automáticamente los cambios de diferentes ramas porque hay modificaciones contradictorias en las mismas líneas de código.

## Estructura del Proyecto

```
EJEMPLO ERROR MERGE/
├── .github/
│   └── copilot-instructions.md
├── src/
│   ├── main.py          # Archivo principal que será modificado en diferentes ramas
│   ├── config.json      # Configuración que causará conflictos
│   └── utils.py         # Utilidades compartidas
├── docs/
│   └── manual.md        # Documentación que será editada simultáneamente
├── README.md            # Este archivo
└── requirements.txt     # Dependencias del proyecto
```

## Escenarios de Conflicto Preparados

### 1. Conflicto Básico de Líneas
- **Archivo**: `src/main.py`
- **Escenario**: Dos desarrolladores modifican la misma función

### 2. Conflicto de Configuración
- **Archivo**: `src/config.json`
- **Escenario**: Cambios en configuraciones diferentes que afectan la misma estructura

### 3. Conflicto de Documentación
- **Archivo**: `docs/manual.md`
- **Escenario**: Actualizaciones simultáneas de documentación

## Cómo Usar Este Proyecto

1. **Clonar el repositorio**
2. **Crear rama feature-1**: `git checkout -b feature-1`
3. **Hacer cambios y commit**
4. **Crear rama feature-2**: `git checkout main && git checkout -b feature-2`
5. **Hacer cambios conflictivos y commit**
6. **Intentar merge**: Aquí aparecerán los conflictos
7. **Resolver conflictos manualmente**
8. **Completar el merge**

## Comandos Git Útiles para Resolución

```bash
# Ver el estado del merge
git status

# Ver los archivos en conflicto
git diff --name-only --diff-filter=U

# Abrir herramienta de merge
git mergetool

# Después de resolver conflictos
git add .
git commit -m "Resolver conflictos de merge"
```

## Tipos de Marcadores de Conflicto

```
<<<<<<< HEAD
# Cambios de la rama actual
=======
# Cambios de la rama que se está fusionando
>>>>>>> nombre-de-rama
```

## Objetivo Educativo

Este proyecto te ayudará a:
- Entender cómo surgen los conflictos de merge
- Practicar la identificación de conflictos
- Aprender a resolverlos manualmente
- Familiarizarte con las herramientas de Git para merge
- Desarrollar buenas prácticas para evitar conflictos
