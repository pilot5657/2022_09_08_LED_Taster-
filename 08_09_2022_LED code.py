# Bibliotheken laden
from gpiozero import Button, LED
import sqlite3
# verbindet mit Datenbank
con = sqlite3.connect('test1.db')
cur = con.cursor()

# erstelt die Datenbank
cur.execute('''CREATE TABLE IF NOT EXISTS LED''')
cur.exicute('''INSERT INTO LED VALUES
                    ('idled, Zeitstämpel , Zustand)''')


con.commit()
for row in cur.exeute('''SELECT * FROM LED'''):
    print(row)

        
        

# Initialisierung von GPIO27 als Button (Eingang)
button = Button(27)

# Initialisierung von GPIO17 als LED (Ausgang)
led = LED(17)
test1

# wenn der Taster gedrückt schalte in den Toggle Berieb
button.when_pressed = led.toggle


    

