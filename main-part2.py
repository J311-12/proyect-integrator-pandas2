import numpy as np
from datasets import load_dataset
import pandas as pd

# Cargando el dataset
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Convirtiendo el Dataset en un DataFrame de Pandas
df = pd.DataFrame(data)

# Verificando los tipos de datos en cada columna
tipos_de_datos = df.dtypes
print("Tipos de datos en cada columna:")
print(tipos_de_datos)

# Calculando la cantidad de hombres fumadores y mujeres fumadoras
cantidad_hombres_fumadores = df[df["is_male"] & df["is_smoker"]]["is_male"].count()
cantidad_mujeres_fumadoras = df[~df["is_male"] & df["is_smoker"]]["is_male"].count()

# Imprimiendo los resultados
print("Cantidad de hombres fumadores:", cantidad_hombres_fumadores)
print("Cantidad de mujeres fumadoras:", cantidad_mujeres_fumadoras)
