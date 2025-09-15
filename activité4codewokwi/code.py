from machine import Pin, ADC
import time

# 🔌 Capteurs
pir = Pin(17, Pin.IN)       # Capteur PIR sur GPIO 16
ldr = ADC(26)               # Capteur LDR sur ADC 27

# 💡 LEDs
led1 = Pin(2, Pin.OUT)      # LED sur GPIO 2
led2 = Pin(3, Pin.OUT)      # LED sur GPIO 3

# ⚙️ Seuil de luminosité (à ajuster selon test)
SEUIL_LUMIERE = 5000

# 🔁 Boucle principale
while True:
    mouvement = pir.value()
    luminosite = ldr.read_u16()

    print("PIR:", "Mouvement" if mouvement else "Rien")
    print("LDR:", luminosite, "(faible)" if luminosite < SEUIL_LUMIERE else "(forte)")

    if mouvement and luminosite < SEUIL_LUMIERE:
        print(" Conditions OK → LEDs ON")
        led1.on()
        led2.on()
    else:
        print(" Conditions non remplies → LEDs OFF")
        led1.off()
        led2.off()

    print("-" * 30)
    time.sleep(1)

