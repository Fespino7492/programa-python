# Universidad Nacional Abierta y a Distancia - UNAD
# Zona Caribe ZCAR - Puerto Colombia, Atlántico

# Nombre del estudiante: Fabricio José Escobar Ospino
# Grupo: 2201 - 14
# Programa: Ingeniería de Sistemas
# Código Fuente: Autoría Propia

# Fase 5 - Evaluación Final POA 

# Problema 1: 
# 
# Una matriz almacena datos de sesiones de clientes con el 
# formato: [ID Cliente, Duración (segundos), Eventos Clics].  
# Se necesita una herramienta para evaluar el nivel de compromiso de cada sesión. 
# Requisitos de Desarrollo: - Datos Iniciales: Una matriz con al menos 5 filas de datos. 
# Módulos: Se requiere un módulo (función) para calcular la 
# clasificación de compromiso de una sesión basándose en su duración y clics. 
# 
# Lógica de Negocio: 
# ✓ Clasificar como "Alto" (si Duración > 180s y Clics > 8). 
# ✓ Clasificar como "Bajo" (si Duración < 60s o Clics < 3). 
# ✓ Clasificar como "Medio" en todos los demás casos. 
# 
# Salida: 
# Generar un informe listando el ID del cliente y su 
# clasificación final. 

# ============================================================
#                   ESTRUCTURA DEL PROGRAMA
# ============================================================

def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion > 60 and clics > 3:
        return "Medio"
    else:        
        return "Bajo"

def mostrar_reporte(lista_sesiones):
    print("===== INFORME DE COMPROMISO =====")

    for sesion in lista_sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        clasificacion = clasificar_compromiso(duracion, clics)

        print(f"Cliente ID: {id_cliente} | Duración: {duracion} seg | Clics: {clics} | Compromiso: {clasificacion}")

def main():
    sesiones_clientes = [
        [101, 240, 12],
        [102, 45, 2],
        [103, 120, 5],
        [104, 300, 15],
        [105, 70, 1]
    ]

    mostrar_reporte(sesiones_clientes)

if __name__ == "__main__":
    main()