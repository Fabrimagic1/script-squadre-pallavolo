
import itertools
import csv

def carica_database(file_path):
    database = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for riga in reader:
            nome = riga['nome'].strip().lower()
            valore = float(riga['valore'])
            database[nome] = valore
    return database

def crea_squadre_avvicinate():
    database = carica_database("giocatori.csv")

    numero_squadre = int(input("Inserisci il numero di squadre: "))
    numero_persone_per_squadra = int(input("Inserisci il numero di persone per squadra: "))

    variabili = {}
    for i in range(numero_squadre * numero_persone_per_squadra):
        nome_persona = input(f"Inserisci il nome della persona {i + 1}: ").strip()
        nome_lookup = nome_persona.lower()

        if nome_lookup in database:
            valore_persona = database[nome_lookup]
            print(f"✔️ Valore di {nome_persona} caricato dal database: {valore_persona}")
        else:
            valore_persona = float(input(f"❗ Valore per {nome_persona} non trovato. Inserisci manualmente: "))
        variabili[nome_persona] = valore_persona

    persone = list(variabili.items())

    migliori_squadre = None
    differenza_media_minima = float('inf')

    for combinazione in itertools.permutations(persone):
        squadre = {i + 1: [] for i in range(numero_squadre)}
        for i, (persona, valore) in enumerate(combinazione):
            squadra_assegnata = i % numero_squadre + 1
            squadre[squadra_assegnata].append((persona, valore))

        somme_squadre = [sum(valore for _, valore in squadra) for squadra in squadre.values()]
        differenza_media = sum(abs(somma - sum(somme_squadre) / numero_squadre) for somma in somme_squadre) / numero_squadre

        if differenza_media < differenza_media_minima:
            differenza_media_minima = differenza_media
            migliori_squadre = squadre

    print("\n🔢 Migliore distribuzione delle squadre:")
    for squadra, membri in migliori_squadre.items():
        print(f"\n🟦 Squadra {squadra}:")
        for nome, _ in membri:
            print(f"  - {nome}")

if __name__ == "__main__":
    crea_squadre_avvicinate()
