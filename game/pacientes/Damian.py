# ===============================================
# PSYCH SESSION - pacientes/damian.rpy
# Las 5 sesiones de Damián
# ===============================================

# ── SESION 1 ──────────────────────────────────
label damian_s1:

    show screen barra_rapport("Damian", damian_rapport)

    scene black with fade
    "Dia [dia_actual]. Primera sesion con Damian Ferreyra."

    damian "Vine porque mi hija me dijo que {b}si no venia a terapia, dejaba de hablarme{/b}."
    damian "No porque crea que necesito esto."

    menu:
        "Que respondés?"

        "Entiendo. Que te hizo venir igual?":
            $ damian_rapport += 5
            $ stat_escucha += 1
            damian "Supongo que... {b}no quiero perderla{/b}."
            jump damian_s1_continua

        "Tu hija te importa?":
            $ damian_rapport -= 15
            $ damian_error_s1 = True
            damian "Que pregunta."
            "Damian se pone rigido."
            jump damian_s1_continua

        "Muchas personas vienen sintiendose asi. No hay apuro.":
            $ damian_rapport += 10
            $ stat_contencion += 1
            damian "Si. Igual. No se bien por donde empezar."
            jump damian_s1_continua

label damian_s1_continua:

    call chequear_rapport_damian

    damian "Valentina dice que soy controlador. Que no la dejo vivir."
    damian "{b}Pero yo solo trato de protegerla.{/b} Siempre fue asi con mis hijos."

    menu:
        "Que respondés?"

        "Que paso con tus otros hijos?":
            $ damian_rapport += 5
            $ stat_interpretacion += 1
            damian "Con los otros... {b}ya no hablamos. Hace años.{/b}"
            jump damian_s1_cierre

        "De que la querias proteger?":
            $ stat_escucha += 1
            damian "Del mundo. La gente no es de fiar."
            jump damian_s1_cierre

        "Ella alguna vez te dijo especificamente que la molesta?":
            $ stat_rapport += 1
            damian "Si. Dice que la llamo demasiado."
            jump damian_s1_cierre

label damian_s1_cierre:

    call chequear_rapport_damian

    damian "{b}Para que sirve esto, en definitiva?{/b}"

    menu:
        "Que respondés?"

        "Para entender por que hacemos lo que hacemos.":
            $ damian_rapport += 5
            damian "Puede ser."

        "Para lo que vos quieras que sirva.":
            $ damian_rapport += 10
            $ stat_contencion += 1
            damian "El jueves a las 18, si puede ser."

    # Fin sesión 1
    $ damian_sesiones_completadas += 1
    $ trofeo_damian_s1 = True
    $ dia_actual += 1

    hide screen barra_rapport

    scene black with fade
    "Sesion 1 con Damian completada."
    "Rapport: [damian_rapport]/100"

    jump escritorio


# ── SESION 2 ──────────────────────────────────
label damian_s2:

    show screen barra_rapport("Damian", damian_rapport)

    scene black with fade
    "Dia [dia_actual]. Segunda sesion con Damian."

    if damian_error_s1:
        damian "La semana pasada me pregunto si mi hija me importaba."
        damian "{b}Eso me molesto bastante.{/b} Igual... volvi."
        $ damian_rapport -= 5
    else:
        damian "Estuve pensando en lo que hablamos."
        damian "No es facil, pero... {b}creo que tiene sentido volver.{/b}"
        $ damian_rapport += 5

    damian "Valentina me llamo dos veces esta semana. No atiendi."

    menu:
        "Que respondés?"

        "Por que no atendiste?":
            $ stat_interpretacion += 1
            $ damian_rapport += 10
            damian "No se. Tenia miedo de lo que me iba a decir."
            damian "{b}Siempre espero lo peor.{/b}"
            jump damian_s2_profundo

        "Como te hizo sentir eso?":
            $ stat_escucha += 1
            $ damian_rapport += 5
            damian "Culpable. Supongo."
            jump damian_s2_profundo

        "Quizas ella solo queria hablar.":
            $ damian_rapport -= 10
            $ damian_error_s2 = True
            damian "Ya se lo que queria. Reclamarme."
            "Damian se cierra."
            jump damian_s2_cierre

label damian_s2_profundo:

    damian "Cuando era chico... aprendes que las noticias malas llegan sin aviso."
    damian "{b}Entonces es mejor no atender.{/b}"

    menu:
        "Que respondés?"

        "Que noticias malas recibiste de chico?":
            $ stat_interpretacion += 2
            $ damian_rapport += 15
            damian "..."
            damian "Teniamos un perro. Bruno."
            $ damian_secreto_revelado = True
            jump damian_s2_perro

        "Eso suena muy agotador de sostener.":
            $ stat_contencion += 1
            $ damian_rapport += 10
            damian "Es lo unico que conozco."
            jump damian_s2_cierre

label damian_s2_perro:

    damian "{b}Un dia llegue del colegio y no estaba.{/b}"
    damian "Mi viejo me dijo que lo habian tenido que llevar al veterinario."
    damian "Tarde años en entender lo que paso."
    damian "Nadie me pregunto. {b}Nadie me dijo nada.{/b}"

    menu:
        "Que respondés?"

        "Que sentiste cuando lo entendiste?":
            $ damian_rapport += 15
            $ stat_interpretacion += 1
            damian "{b}Traicion.{/b} Supongo."
            damian "Que las decisiones se toman sin vos."

        "Eso fue una perdida muy grande para un chico.":
            $ damian_rapport += 10
            $ stat_contencion += 2
            damian "Nunca lo habia pensado asi."
            damian "Como una perdida."

    jump damian_s2_cierre

label damian_s2_cierre:

    call chequear_rapport_damian

    $ damian_sesiones_completadas += 1
    $ dia_actual += 1

    hide screen barra_rapport

    scene black with fade
    "Sesion 2 con Damian completada."
    "Rapport: [damian_rapport]/100"

    jump escritorio