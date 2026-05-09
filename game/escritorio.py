# ===============================================
# PSYCH SESSION - escritorio.rpy
# Hub principal, reloj, agenda
# ===============================================

image escritorio = im.Scale("images/escritorio.png", 1920, 1080)

# -- Pantalla principal del escritorio --
screen pantalla_escritorio():

    # Fondo
    add "escritorio"

    # Reloj y fecha tomados del sistema
    timer 1.0 action ScreenVariable("hora_actual",
        datetime.datetime.now().strftime("%H:%M")) repeat True

    python:
        import datetime
        hora_actual = datetime.datetime.now().strftime("%H:%M")
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%y")

    # Mostrar hora y fecha sobre la barra de inicio
    text hora_actual:
        xpos 1820 ypos 752
        size 18
        color "#000000"
        font "gui/font/SourceSansPro-Regular.otf"

    text fecha_actual:
        xpos 1800 ypos 772
        size 16
        color "#000000"
        font "gui/font/SourceSansPro-Regular.otf"

    # Icono Mi PC -> legajo
    imagebutton:
        xpos 30 ypos 30
        idle Solid("#00000000")
        hover Solid("#ffffff33")
        xysize (120, 130)
        action Return("legajo")

    # Icono Pacientes -> carpeta pacientes
    imagebutton:
        xpos 30 ypos 185
        idle Solid("#00000000")
        hover Solid("#ffffff33")
        xysize (120, 130)
        action Return("email")

    # Icono Notas -> internet
    imagebutton:
        xpos 30 ypos 330
        idle Solid("#00000000")
        hover Solid("#ffffff33")
        xysize (120, 130)
        action Return("internet")

    # Icono DFH -> videollamada
    imagebutton:
        xpos 30 ypos 520
        idle Solid("#00000000")
        hover Solid("#ffffff33")
        xysize (120, 130)
        action Return("sesion")

    # Rapport de pacientes activos (esquina superior derecha)
    if damian_activo:
        text "Damian: [damian_rapport]":
            xpos 1600 ypos 30
            size 20
            color "#1A3A5C"

# ===============================================
# LABEL ESCRITORIO
# ===============================================
label escritorio:

    python:
        import datetime

    $ resultado = renpy.call_screen("pantalla_escritorio")

    if resultado == "legajo":
        jump escritorio_legajo
    elif resultado == "email":
        jump escritorio_email
    elif resultado == "internet":
        jump escritorio_internet
    elif resultado == "sesion":
        jump agenda

label escritorio_legajo:
    "Abris Mi PC. Por ahora no hay nada nuevo acá."
    jump escritorio

label escritorio_email:
    "Abris la carpeta de Pacientes."
    jump escritorio

label escritorio_internet:
    "Abris el navegador."
    jump escritorio

# ===============================================
# AGENDA - decide qué sesión toca
# ===============================================
label agenda:

    if dia_actual == 1 and damian_activo:
        jump damian_s1
    elif dia_actual == 2 and damian_activo:
        jump damian_s2
    else:
        "No hay sesiones programadas por hoy."
        jump escritorio