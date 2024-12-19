import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

# Génération de données fictives
def generate_weather_data(start_date, num_entries, interval_hours=3):
    """
    Génère des données météorologiques fictives pour une ville.
    
    Args:
        start_date (str): Date de début au format 'YYYY-MM-DD HH:MM:SS'.
        num_entries (int): Nombre de points de données à générer.
        interval_hours (int): Intervalle de temps entre les enregistrements (en heures).
        
    Returns:
        pd.DataFrame: DataFrame contenant les données fictives.
    """
    data = []
    current_time = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    
    for _ in range(num_entries):
        temperature = round(random.uniform(-5, 30), 1)  # Température en °C
        humidity = random.randint(30, 90)  # Humidité en %
        data.append({
            'datetime': current_time.strftime('%Y-%m-%d %H:%M:%S'),
            'temperature': temperature,
            'humidity': humidity
        })
        current_time += timedelta(hours=interval_hours)
    
    return pd.DataFrame(data)

# Générer des données fictives
start_date = '2024-12-07 00:00:00'
num_entries = 20  # 20 entrées
weather_data = generate_weather_data(start_date, num_entries)

# Afficher les premières lignes des données
print(weather_data)

# Visualisation des données
plt.figure(figsize=(12, 6))

# Tracé des températures
plt.plot(weather_data['datetime'], weather_data['temperature'], marker='o', label='Température (°C)', color='tab:red')

# Tracé de l'humidité
plt.plot(weather_data['datetime'], weather_data['humidity'], marker='s', label='Humidité (%)', color='tab:blue')

# Paramètres du graphique
plt.xticks(rotation=45)
plt.xlabel('Date et Heure')
plt.ylabel('Valeurs')
plt.title("Prévisions météorologiques fictives")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Affichage du graphique
plt.show()
