# ==============================================================================
# 01. DEFINICIÓN DE IMÁGENES
# ==============================================================================
image bg_escritorio_full = im.Scale("images/escritorio.png", 1920, 1080)

# Asegurate de que estos archivos existan en game/images/
image icon_pc = im.Scale("images/icon_pc.png", 120, 120)
image icon_folder = im.Scale("images/icon_folder.png", 120, 120)
image icon_notas = im.Scale("images/icon_notas.png", 120, 120)
image icon_explorer = im.Scale("images/icon_explorer.png", 120, 120)
image icon_papelera = im.Scale("images/icon_papelera.png", 120, 120)

# ==============================================================================
# 02. ANIMACIÓN DE ICONOS
# ==============================================================================
transform efecto_click:
    on hover:
        zoom 1.05
        yoffset -5
    on idle:
        zoom 1.0
        yoffset 0
    on selected_hover:
        zoom 0.95
        yoffset 2
    on selected_idle:
        zoom 0.95
        yoffset 2

# ==============================================================================
# 03. PANTALLA DEL ESCRITORIO
# ==============================================================================
screen pantalla_escritorio():
    add "bg_escritorio_full"

    # --- Reloj y Fecha ---
    python:
        import datetime
        ahora = datetime.datetime.now()
        hora_texto = ahora.strftime("%H:%M")
        fecha_texto = ahora.strftime("%d/%m/%Y")

    text "[hora_texto]":
        xpos 1810 ypos 750 size 24 color "#000" bold True
    text "[fecha_texto]":
        xpos 1790 ypos 780 size 18 color "#000"

    # --- Grupo de Iconos (Arriba a la Izquierda) ---
    vbox:
        xpos 60 ypos 60
        spacing 40

        # MI PC
        vbox:
            spacing 5
            imagebutton:
                xalign 0.5 # Esto centra el botón respecto al texto de abajo
                idle "icon_pc"
                at efecto_click
                action Return("legajo")
            text _("Mi PC"):
                xalign 0.5 size 18 color "#000" outlines [(1, "#fff", 0, 0)]

        # PACIENTES
        vbox:
            spacing 5
            imagebutton:
                xalign 0.5
                idle "icon_folder"
                at efecto_click
                action Return("pacientes")
            text _("Pacientes"):
                xalign 0.5 size 18 color "#000" outlines [(1, "#fff", 0, 0)]

        # NOTAS
        vbox:
            spacing 5
            imagebutton:
                xalign 0.5
                idle "icon_notas"
                at efecto_click
                action Return("notas")
            text _("Notas"):
                xalign 0.5 size 18 color "#000" outlines [(1, "#fff", 0, 0)]

        # NAVEGADOR
        vbox:
            spacing 5
            imagebutton:
                xalign 0.5
                idle "icon_explorer"
                at efecto_click
                action Return("explorer")
            text _("Navegador"):
                xalign 0.5 size 18 color "#000" outlines [(1, "#fff", 0, 0)]

    # --- Papelera (Abajo a la Izquierda) ---
    # CORREGIDO: Eliminado xalign 0.5 que chocaba con xpos
    vbox:
        xpos 60 ypos 820
        spacing 5
        imagebutton:
            xalign 0.5
            idle "icon_papelera"
            at efecto_click
            action Return("papelera")
        text _("Papelera"):
            xalign 0.5 size 18 color "#000" outlines [(1, "#fff", 0, 0)]