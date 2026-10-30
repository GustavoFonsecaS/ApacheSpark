import csv
import random
import time
from datetime import datetime, timedelta

# Generar dataset histórico de sensores ambientales
# 2000 registros simulando 30 días de mediciones

random.seed(42)
start_date = datetime(2024, 9, 1)
rows = []

for i in range(2000):
    sensor_id = random.randint(1, 10)
    # Algunos valores anómalos para limpiar (5% de los datos)
    if random.random() < 0.05:
        temperature = round(random.uniform(-10, 100), 2)  # fuera de rango
        humidity = round(random.uniform(-5, 120), 2)       # fuera de rango
        co2 = round(random.uniform(-50, 5000), 1)
    else:
        temperature = round(random.uniform(18.0, 38.0), 2)
        humidity = round(random.uniform(35.0, 85.0), 2)
        co2 = round(random.uniform(350.0, 1200.0), 1)

    timestamp = start_date + timedelta(minutes=i * 21)
    location = random.choice(['Planta_A', 'Planta_B', 'Planta_C', 'Almacen'])

    rows.append([sensor_id, temperature, humidity, co2, location,
                 timestamp.strftime('%Y-%m-%d %H:%M:%S')])

with open('/home/vboxuser/sensores_historico.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['sensor_id', 'temperatura', 'humedad', 'co2', 'ubicacion', 'timestamp'])
    writer.writerows(rows)

print(f"Dataset generado: {len(rows)} registros en /home/vboxuser/sensores_historico.csv")
