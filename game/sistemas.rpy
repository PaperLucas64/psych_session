# Lógica de sistema de juego
init python:
    # Una función simple para verificar si un paciente está en crisis
    def check_crisis(rapport):
        if rapport < 30:
            return True
        return False

# Aquí podés definir barras de estado o UI adicional
screen barra_rapport(nombre, valor):
    frame:
        xalign 0.95 yalign 0.05
        vbox:
            text "Rapport [nombre]: [valor]%" size 18
            bar value valor range 100 xsize 200