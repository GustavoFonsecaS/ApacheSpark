# ApacheSpark
Procesamiento de datos con Apache Spark
Tarea 3 — Procesamiento de Datos con Apache Spark
Curso: Big Data — Código 202016911
Universidad: Universidad Nacional Abierta y a Distancia (UNAD)
Estudiante: Freddy Gustavo Fonseca Suárez

===========================================================
DESCRIPCIÓN
===========================================================

Este repositorio contiene el código desarrollado para la Tarea 3 del curso
Big Data, que implementa procesamiento de datos en batch con Apache Spark
y procesamiento en tiempo real con Apache Kafka y Spark Streaming.

El caso de uso es el monitoreo de sensores ambientales industriales que
registran temperatura, humedad y CO2 en cuatro zonas de una planta:
Planta_A, Planta_B, Planta_C y Almacén.

===========================================================
ESTRUCTURA DEL REPOSITORIO
===========================================================

generar_datos.py   -> Genera el dataset histórico de sensores (2.000 registros)
tarea3.py          -> Análisis batch con PySpark (RDDs + DataFrames)
producer.py        -> Productor Kafka — envía datos de sensores en tiempo real
consumer.py        -> Consumidor Spark Streaming — lee y procesa datos desde Kafka
zk.sh              -> Script para iniciar ZooKeeper
kafka.sh           -> Script para iniciar el broker Kafka
topic.sh           -> Script para crear el topic de Kafka
README.txt         -> Este archivo

===========================================================
REQUISITOS
===========================================================

- Ubuntu 20.04 (VirtualBox)
- Python 3.8+
- Apache Spark 3.5.1
- Apache Kafka 3.8.1
- Java 11
- Librerías: pyspark, kafka-python

===========================================================
PARTE 1 — PROCESAMIENTO EN BATCH
===========================================================

1. Generar el dataset:
   python3 generar_datos.py
   Genera el archivo /home/vboxuser/sensores_historico.csv con 2.000 registros
   históricos simulados, incluyendo un 5% de valores anómalos para limpieza.

2. Ejecutar el análisis batch:
   spark-submit ~/tarea3.py

   El script realiza las siguientes etapas:
   - Carga del dataset con esquema definido
   - Limpieza de datos con RDD filter() — elimina registros fuera de rango
   - Transformaciones RDD: map, filter, flatMap, groupByKey, reduceByKey
   - Acciones RDD: count, take, reduce, collect
   - EDA con DataFrames: estadísticas descriptivas, promedios por ubicación,
     alertas CO2 > 800 ppm

===========================================================
PARTE 2 — PROCESAMIENTO EN TIEMPO REAL (KAFKA + SPARK STREAMING)
===========================================================

1. Iniciar ZooKeeper:
   bash ~/zk.sh

2. Iniciar Kafka:
   bash ~/kafka.sh

3. Crear el topic:
   bash ~/topic.sh

4. Iniciar el consumidor Spark Streaming:
   spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 ~/consumer.py

5. Iniciar el productor Kafka:
   python3 ~/producer.py

   El productor envía un registro de sensor cada segundo al topic "sensores".
   El consumidor procesa los datos en micro-lotes cada 5 segundos, mostrando
   estadísticas en tiempo real.

===========================================================
DATASET
===========================================================

- Fuente: Datos propios generados (simulación)
- Registros: 2.000 históricos / tiempo real continuo
- Variables: sensor_id, temperatura, humedad, co2, ubicacion, timestamp
- Período simulado: Septiembre 2024 — 30 días de mediciones

===========================================================
REFERENCIAS
===========================================================

- Chambers, B., & Zaharia, M. (2018). Spark: The definitive guide. O'Reilly Media.
- Zaharia, M., et al. (2012). Resilient distributed datasets. USENIX NSDI '12.
- Apache Software Foundation. (2024). Apache Kafka documentation.
  https://kafka.apache.org/documentation/
