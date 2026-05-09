# ===============================================
# PSYCH SESSION - sistemas.rpy
# Rapport, estadísticas, trofeos
# ===============================================

# -- Rapport por paciente --
default damian_rapport = 75
default roxana_rapport = 75
default german_rapport = 75
default andres_rapport = 75
default susana_rapport = 75

# -- Memoria de Damián --
default damian_error_s1 = False
default damian_error_s2 = False
default damian_secreto_revelado = False
default damian_sesiones_completadas = 0

# ===============================================
# PANTALLA DE ESTADÍSTICAS
# ===============================================
screen pantalla_stats():

    modal True

    frame:
        xalign 0.5 yalign 0.5
        xsize 600 ysize 500
        background "#1A3A5Cee"

        vbox:
            xalign 0.5
            spacing 20
            ypos 20

            text "Tus estadísticas":
                xalign 0.5
                size 28
                color "#FFFFFF"

            hbox:
                spacing 20
                xalign 0.5
                vbox:
                    spacing 12
                    text "Rapport":
                        color "#AADDFF" size 20
                    text "Interpretacion":
                        color "#AADDFF" size 20
                    text "Contencion":
                        color "#AADDFF" size 20
                    text "Confrontacion":
                        color "#AADDFF" size 20
                    text "Escucha activa":
                        color "#AADDFF" size 20

                vbox:
                    spacing 12
                    text "[stat_rapport]":
                        color "#FFFFFF" size 20
                    text "[stat_interpretacion]":
                        color "#FFFFFF" size 20
                    text "[stat_contencion]":
                        color "#FFFFFF" size 20
                    text "[stat_confrontacion]":
                        color "#FFFFFF" size 20
                    text "[stat_escucha]":
                        color "#FFFFFF" size 20

            textbutton "Cerrar":
                xalign 0.5
                action Hide("pantalla_stats")

# ===============================================
# PANTALLA DE RAPPORT DE PACIENTE
# ===============================================
screen barra_rapport(nombre, valor):

    frame:
        xpos 20 ypos 20
        xsize 250 ysize 60
        background "#00000088"

        hbox:
            spacing 10
            xpos 10 ypos 10

            text "[nombre]:":
                color "#FFFFFF" size 18

            bar:
                value AnimatedValue(valor, 100, 1.0)
                xsize 120 ysize 20
                yalign 0.5
                left_bar Frame("#2E75B6")
                right_bar Frame("#333333")

# ===============================================
# LABEL: CHEQUEAR RAPPORT
# Si llega a 0 el paciente abandona
# ===============================================
label chequear_rapport_damian:
    if damian_rapport <= 0:
        $ damian_activo = False
        $ trofeo_primer_abandono = True
        scene black with fade
        "Damian te manda un mensaje esa noche."
        damian "Creo que no voy a poder seguir con las sesiones. Gracias igual."
        "No volviste a saber de el."
        jump escritorio
    return

# ===============================================
# LABEL: SUMAR ESTADÍSTICAS
# Llamar con: call sumar_stat("escucha")
# ===============================================
label sumar_stat(stat):
    if stat == "rapport":
        $ stat_rapport += 1
    elif stat == "interpretacion":
        $ stat_interpretacion += 1
    elif stat == "contencion":
        $ stat_contencion += 1
    elif stat == "confrontacion":
        $ stat_confrontacion += 1
    elif stat == "escucha":
        $ stat_escucha += 1
    return

# ===============================================
# PANTALLA DE TROFEOS
# ===============================================
screen pantalla_trofeos():

    modal True

    frame:
        xalign 0.5 yalign 0.5
        xsize 600 ysize 500
        background "#1A3A5Cee"

        vbox:
            xalign 0.5
            spacing 16
            ypos 20

            text "Trofeos":
                xalign 0.5
                size 28
                color "#FFD700"

            if trofeo_damian_s1:
                text "Primera sesion con Damian completada":
                    color "#FFFFFF" size 20
            else:
                text "??? - Primera sesion con Damian":
                    color "#555555" size 20

            if trofeo_damian_alta:
                text "Damian recibio el alta":
                    color "#FFFFFF" size 20
            else:
                text "??? - Damian recibe el alta":
                    color "#555555" size 20

            if trofeo_primer_abandono:
                text "Un paciente abandono la terapia":
                    color "#FFFFFF" size 20
            else:
                text "??? - Primer abandono":
                    color "#555555" size 20

            textbutton "Cerrar":
                xalign 0.5
                action Hide("pantalla_trofeos")