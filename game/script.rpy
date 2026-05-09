label start:
    scene black
    "Iniciando sesión..."
    jump escritorio

label escritorio:
    window hide 
    $ resultado = renpy.call_screen("pantalla_escritorio")

# ---------------- LÓGICA DE CARPETAS Y POPUPS ----------------
    if resultado == "pacientes":
        # ELIMINAR: "Sistema: Abriendo base de datos..."
        # AGREGAR:
        show screen ventana_pacientes
        
    elif resultado == "historia_damian":
        hide screen ventana_damian
        "Revisando notas de sesiones anteriores de Damián..."
        # jump resumen_sesiones (si tenés el label)
        
    elif resultado == "legajo_damian":
        hide screen ventana_damian
        "Nombre: Damián Ferreyra. Edad: 45 años. Ocupación: Contador."

    jump escritorio