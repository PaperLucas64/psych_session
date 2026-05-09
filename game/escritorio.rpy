
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

# ---------------- ANIMACIÓN APARECER POCO A POCO ----------------
transform aparecer_lento(retraso):
    alpha 0.0
    pause retraso
    linear 0.5 alpha 1.0

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
                # CAMBIAMOS ESTA LÍNEA:
                action Show("ventana_pacientes") 
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

# ---------------- VENTANA DE PACIENTES ----------------
screen ventana_pacientes():
    modal True
    
    fixed:
        xsize 1200 ysize 800
        align (0.5, 0.4) 

        # 1. Fondo de la ventana
        add im.Scale("images/ventana_pacientes.png", 1200, 800)

        # 2. BOTÓN CERRAR (X)
        # Ajustado a ~1150 para que entre en los 1200px de ancho
        imagebutton:
            idle Solid("#00000000") 
            hover Solid("#ff000033") 
            xpos 980 ypos 75 # Ajusta estos si la X no coincide exactamente
            xysize (50, 45) 
            action Hide("ventana_pacientes")

        # 3. BOTÓN MAXIMIZAR
        imagebutton:
            idle Solid("#00000000")
            hover Solid("#ffffff33")
            xpos 1085 ypos 15 
            xysize (45, 45)
            action Notify("Ventana ya maximizada.")

        # 4. BOTÓN MINIMIZAR
        imagebutton:
            idle Solid("#00000000")
            hover Solid("#ffffff33")
            xpos 1035 ypos 15 
            xysize (45, 45)
            action Hide("ventana_pacientes")

        # 5. CONTENEDOR DE CARPETAS (Con icon_folder.png)
        grid 5 1:
            xalign 0.5 ypos 150 
            spacing 40

            # Carpeta de Damián
            vbox:
                at aparecer_lento(0.2)
                spacing 5
                imagebutton:
                    # ACTUALIZADO: Ahora usa icon_folder.png
                    idle im.Scale("images/icon_folder.png", 100, 100) 
                    at efecto_click
                    action [Hide("ventana_pacientes"), Show("ventana_damian")] 
                text "Damian" xalign 0.5 size 16 color "#000"

            # Otros espacios bloqueados
            for i in range(2, 6):
                vbox:
                    at aparecer_lento(0.2 * i)
                    spacing 5
                    imagebutton:
                        idle im.Scale("images/icon_folder.png", 100, 100)
                        at efecto_click
                        action Notify("Acceso denegado.")
                    text "---" xalign 0.5 size 16 color "#777"
                
# ---------------- VENTANA ESPECÍFICA DAMIÁN ----------------
screen ventana_damian():
    modal True
    add im.Scale("images/ventana_pacientes.png", 1200, 800) align (0.5, 0.4)
    
    text "Expediente: Damian" xpos 400 ypos 175 size 22 color "#000"

    imagebutton:
        idle Solid("#00000000")
        xpos 1485 ypos 165 xysize (40, 40)
        action [Hide("ventana_damian"), Show("ventana_pacientes")]

    hbox:
        align (0.4, 0.4)
        spacing 100
        
        vbox:
            imagebutton:
                idle "icon_notas"
                at efecto_click
                action Return("historia_damian")
            text "Historia Clínica" xalign 0.5 size 16 color "#000"

        vbox:
            imagebutton:
                idle im.Scale("images/icon_legajo_damian.png", 120, 120)
                at efecto_click
                action Return("legajo_damian")
            text "Legajo" xalign 0.5 size 16 color "#000"