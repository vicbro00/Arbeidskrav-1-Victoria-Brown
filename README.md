# Victoria Louise Brown

## Oppgave 1:
Filer:
[oppgave-1.py](oppgave-1.py)

## Oppgave 2:
Jeg valgte å strukturere dataene mine innenfor en liste som heter all_sessions.
Innenfor denne listen har jeg 5 dictionaries for studie økter.
Når brukeren da lager en ny økt, blir den lagret som en ny dictionary innenfor all_sessions listen.

Filer:
[oppgave-2.py](oppgave-2.py)

## Oppgave 3:
Dokumentasjonens nettside jeg brukte var for det meste disse: 
Tittel: datetime objects, link: https://docs.python.org/3/library/datetime.html#datetime-objects,
Tittel: timedelta objects, link: https://docs.python.org/3/library/datetime.html#timedelta-objects,
Tittel: date objects, link: https://docs.python.org/3/library/datetime.html#date-objects.
I tillegg til at jeg brukte dokumentasjonen, brukte jeg også litt vanlige søkemotorer for å finne hjelp til 
hvordan man skriver ulike date objekter, siden jeg syntes det var ganske avansert.

Funksjon: new_date
Input: 23.07.2000
Gyldig resultat: 23.07.2000

Funksjon: new_date
Input: 31.12.2026
Gyldig resultat: 31.12.2026

Funksjon: new_date
Input: 31.32.3200
Ugyldig resultat: feilmelding "Invalid date format. Please try again!"

Funksjon: end_date
Input: 14.30 og 30
Gyldig resultat: 15.00

Funksjon: end_date
Input: 30 og 14.30
Ugyldig resultat: feilmelding "Invalid time format. Please try again!"

Funksjon: end_date
Input: hi og no
Ugyldig resultat: feilmelding "Invalid time format. Please try again!"

Funksjon: remaining_days
Input: 23.07.2000 og 24.07.2000
Gyldig resultat: 1 days between.

Funksjon: remaining_days
Input: 23.07.2000 og nei
Ugyldig resultat: feilmelding "Invalid input. Try again"

Funksjon: remaining_days
Input: nei og nei
Ugyldig resultat: feilmelding "Invalid input. Try again"

Funksjon: chronological_list
Input: 23.07.2000, 24.07.2000, 25.07.2000
Gyldig resultat: 23.07.2000
                 24.07.2000
                 25.07.2000

Funksjon: chronological_list
Input: 25.07.2000, 24.07.2000, 23.07.2000
Gyldig resultat: 23.07.2000
                 24.07.2000
                 25.07.2000

Funksjon: chronological_list:
Input: nei, 23.07.2000
Ugyldig resultat: feilmelding "Invalid input. Try again"

Filer:
[oppgave-3.py](oppgave-3.py)

## Oppgave 4
For del 4 av denne oppgaven så var det første jeg gjorde var å endre:
if request["is_resolved"] = "yes":
til:
if request["is_resolved"] == "yes":
Neste jeg gjorde var å legge til None i selve funksjonen, slik at det ikke blir en error dersom argumentet ikke er et tall.
Deretter la jeg til int foran (request["minutes"]), siden minutes må være et heltall, og ikke en string
Så endret jeg return valuen fra total_minutes til bare total, siden der ikke er en variabel som heter total_minutes,
og det er jo totalen vi vil returnere og bruke opp igjen.
Deretter endret jeg total = int(request["minutes"]), til total += int(request["minutes"]), slik at verdien ikke blir det samme gjennom hele loopen.
Nå vil det bli lagt til en for hver gang koden går gjennom loopen.
Så la jeg til en try og except blokk, slik at viss valuen er feil, så vil ikke koden kjøre.
Det siste jeg så gjorde var å legge til et argument i printen.
Jeg endret fra ingen argument: print(sum_resolved_minutes()) til:
print(sum_resolved_minutes([{"is_resolved": "yes", "minutes": 13}, {"is_resolved": "yes", "minutes": 15}, {"is_resolved": "yes", "minutes": 10}]))
Jeg såg at i selve funksjonen, så måtte argumentet være en liste med dictionaries, hvor jeg trenger to keys og to values.
Etter jeg la inn dette argumentet, så kjørte jeg koden, og resultatet jeg fikk var: 38 minutter totalt.

Filer:
[supporthenvendelser.csv](supporthenvendelser.csv)
[support_rapport.txt](support_rapport.txt)
[oppgave-4.py](oppgave-4.py)