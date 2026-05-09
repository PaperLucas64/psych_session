# ===============================================
# PSYCH SESSION - script.rpy
# Variables globales, personajes, inicio
# ===============================================

# -- Personajes --
define psi = Character("Vos", color="#2E75B6")
define damian = Character("Damian", color="#8B0000")
define narrador = Character(None)

# -- Variables globales del juego --
default dia_actual = 1
default sesion_actual = 1

# -- Estadísticas del psicólogo --
default stat_rapport = 0
default stat_interpretacion = 0
default stat_contencion = 0
default stat_confrontacion = 0
default stat_escucha = 0

# -- Trofeos --
default trofeo_damian_s1 = False
default trofeo_damian_alta = False
default trofeo_primer_abandono = False

# -- Estado de pacientes (activo/abandonó) --
default damian_activo = True
default roxana_activo = False
default german_activo = False
default andres_activo = False
default susana_activo = False

# ===============================================
# INICIO
# ===============================================
label start:
    scene black with fade
    "Psych Session"
    "Temporada 1"
    pause 1.0
    jump escritorio