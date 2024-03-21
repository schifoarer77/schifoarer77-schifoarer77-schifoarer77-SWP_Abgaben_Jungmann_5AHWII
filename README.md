> # [schifoarer77-SWP_Abgaben_Jungmann_5AHWII](https://github.com/schifoarer77/schifoarer77-schifoarer77-schifoarer77-SWP_Abgaben_Jungmann_5AHWII/tree/main)
>
> ### [Aufgabe 01 - Lottoziehung](https://github.com/schifoarer77/schifoarer77-schifoarer77-schifoarer77-SWP_Abgaben_Jungmann_5AHWII/blob/main/Aufgabe1_Lottoziehung.py)
> 
> ◼ **Aufgabe Programmiere Lottoziehung:**
>
>> random.getrand()
> 
>> Algorithmus zum Zufallszahlenziehen muss so programmiert sein, dass keine Zufallszahl zweimal gezogen werden kann.
> 
>>> Das heisst, wenn Sie alle 45 Zahlen ziehen müssten, würden Sie den Zufallszahlengenerator nur 45 mal benutzen dürfen.
>
>>> Ziehe die sechs Zahlen und gib Sie am Bildschirm aus
>
> 🏁 **Fertigstellung 05.10.2023**
>
________________________________________________________________
>
> ### [Aufgabe 02 - Poker](https://github.com/schifoarer77/schifoarer77-schifoarer77-schifoarer77-SWP_Abgaben_Jungmann_5AHWII/blob/main/Aufgabe2_Poker.py)
> 
> ◼ **Aufgabe Programmiere Poker:**
>
>> überlege wie man die Pokerkarten modellieren könnte (vier Farben, 13
Symbole)
> 
>> gib zufällig fünf Karten
> 
>> recherchiere welche Kombinationen beim Pokerspiel exisiteren
>
>> schreibe Funktionen für die Kombinationen Paar, Drillinge, Poker, Flash, Strasse usw.
>
>> spiele 100000 mal und zähle die Anzahl der verschiedenen Kombinationen
>
>> berechne den prozentuellen Anteil einer Kombination zu der
Gesamtspieleanzahl
>
>> recherchiere die richtige Anteile im Netz und vergleiche die Ergebnisse
>
> 🏁 **Fertigstellung 09.11.2023**
>
________________________________________________________________





https://bigbangtheory.fandom.com/de/wiki/Stein,_Papier,_Schere,_Echse,_Spock
http://www.samkass.com/theories/RPSSL.html

1) Als Terminal-Spiel umsetzen
2) Spielmodi COMP vs PLAYER
3) zähle wer wie oft gewonnen
4) zähle alle gewählte Symbole
5) überlege wie die Daten dauerhaft gespeichert werden könnten
6) biete ein Menü an Spielen, Statistik

TIP:

0,1,2,3,4

0->2 or 0->4
1->3 or 1->0
2->4 or 2->1
3->0 or 3->2
4->1 or 4->3

if (pid+2)%5 == cid or (pid-1)%5 == cid:
	return True

Erweiterung KW08 2024:
======================
- gesammelte Daten der von den Spielern gewählte Symbolanzahl zu einem Webserver übertragen und in eine SQLite DB speichern

senden:
import requests

url = 'http://url.com'
query = {'field': value}
res = requests.post(url, data=query)
print(res.text)

empfangen:
https://sentry.io/answers/flask-getting-post-data/

sqlite:
https://www.ionos.at/digitalguide/websites/web-entwicklung/sqlite3-python/

benutze venv, config files, alles ins github laden....
