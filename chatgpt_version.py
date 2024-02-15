from utils import (CAPACITY, NUMBER_OF_VALUES, TUPLES, VALUES, WEIGHTS,
                   items_to_indexes, profit, real_profit, to_items, weight)

# Definition der Funktion MAX für die Berechnung des maximalen Profits
def MAX(max_weight, items):
    # Bestimmen der Anzahl der Gegenstände = 100 Gegenstände
    n = len(items)
    
    # Initialisieren der Tabelle dp für die dynamische Programmierung
    # Größe der Tabelle = Matrix; 100 Zeilen und 25001 Spalten
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    # Füllen der Tabelle dp
    for i in range(1, n + 1):
        weight_i, value_i, _ = items[i - 1]  # Gewicht, Wert und Nummer des aktuellen Gegenstands
        for w in range(1, max_weight + 1):
            if weight_i > w:
                dp[i][w] = dp[i - 1][w]  # Wenn der Gegenstand nicht in den Rucksack passt, wird der vorherige Wert übernommen
            else:
                # Vergleich des Werts mit und ohne den aktuellen Gegenstand
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight_i] + value_i)

    # Rückverfolgung der ausgewählten Gegenstände
    selected_items = []
    i, w = n, max_weight
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:  # Überprüfen, ob der aktuelle Gegenstand ausgewählt wurde
            weight_i, _, number = items[i - 1]  # Gewicht, Wert und Nummer des aktuellen Gegenstands
            selected_items.append(number)  # Hinzufügen der Nummer des ausgewählten Gegenstands
            w -= weight_i  # Aktualisieren des verbleibenden Gewichts
        i -= 1

    # Rückgabe des maximalen Profits und der ausgewählten Gegenstände
    return dp[n][max_weight], selected_items

# Laden der Gegenstände aus der JSON-Datei
from utils import TUPLES, to_items
gegenstände = to_items(TUPLES)

# Berechnung des maximalen Profits und der ausgewählten Gegenstände für den schwereren Rucksack
schwerer_rucksack = [96, 97, 98, 99]
max_weight_schwerer = CAPACITY
max_profit_schwerer, selected_items_schwerer = MAX(max_weight_schwerer, gegenstände)
print("Maximaler Profit für den schwereren Rucksack:", max_profit_schwerer, "€")
print("Ausgewählte Gegenstände:", selected_items_schwerer)
print("Gesamtgewicht der ausgewählten Gegenstände:", weight(selected_items_schwerer), "g")
print()

# Berechnung des realen Profits für den ersten und letzten Gegenstand
erster_gegenstand = gegenstände[0]
letzter_gegenstand = gegenstände[-1]  
profit_erster_letzter = real_profit([erster_gegenstand, letzter_gegenstand])
print("Realer Profit für den ersten und letzten Gegenstand:", profit_erster_letzter, "€")
