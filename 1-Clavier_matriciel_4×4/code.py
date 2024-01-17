from machine import Pin
import time

LIGNES = [Pin(5, Pin.OUT), Pin(4, Pin.OUT), Pin(0, Pin.OUT), Pin(2, Pin.OUT)]
COLONNES = [Pin(12, Pin.IN, Pin.PULL_UP), Pin(13, Pin.IN, Pin.PULL_UP), Pin(15, Pin.IN, Pin.PULL_UP), Pin(14, Pin.IN, Pin.PULL_UP)]

TOUCHES = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

def lire_touche():
    for i in range(4):
        LIGNES[i].off()
        time.sleep_ms(10)

        for j in range(4):
            if not COLONNES[j].value():
                while not COLONNES[j].value():
                    pass

                LIGNES[i].on()
                return TOUCHES[i][j]

        LIGNES[i].on()

    return None

while True:
    touche = lire_touche()
    time.sleep_ms(10)
    
    if touche is not None:
        print("Touche appuyée :", touche)

