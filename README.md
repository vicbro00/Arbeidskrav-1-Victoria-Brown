# Victoria Louise Brown

## Oppgave 2:
Jeg valgte å strukturere dataene mine innenfor en liste som heter all_sessions.
Innenfor denne listen har jeg 5 dictionaries for studie økter.
Når brukeren da lager en ny økt, blir den lagret som en ny dictionary innenfor all_sessions listen.

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