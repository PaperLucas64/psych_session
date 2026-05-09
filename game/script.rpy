label start:
    scene black
    "Iniciando sesión..."
    jump escritorio

label escritorio:
    window hide 
    $ resultado = renpy.call_screen("pantalla_escritorio")

    if resultado == "pacientes":
        "Sistema: Accediendo a la base de datos de pacientes..."
    elif resultado == "legajo":
        "Sistema: Abriendo legajos..."
    elif resultado == "notas":
        "Sistema: Bloc de notas vacío."
    elif resultado == "explorer":
        "Sistema: Buscando red..."
    elif resultado == "papelera":
        "Sistema: Nada para restaurar."

    jump escritorio