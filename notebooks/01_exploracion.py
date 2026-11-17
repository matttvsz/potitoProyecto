import pandas as pd
from pathlib import Path
from IPython.display import display
tablas = {}
for archivo in Path("data/raw").glob("*.xlsx"):
    hojas = pd.read_excel(archivo, sheet_name=None)
    for nombre_hoja, df in hojas.items():
        nombre_tabla = f"{archivo.stem}_{nombre_hoja}"
        tablas[nombre_tabla] = df
        nulos = df.isna().sum()
        print(f"\n=== Archivo: {archivo.name} ===")
        print(f"Hoja: {nombre_hoja}")
        print("Filas y Columnas:", df.shape)
        print("Duplicados:",df.duplicated().sum())
        print("Columnas con nulos:")
        print(nulos[nulos > 0])
        print("Valores vacios por columna")
        print(df.isna().sum())
        
        print("nPorcentaje de valores vacios:")
        print((df.isna().mean() * 100).round(2))
        
        print("\nEjemplos de registros sin editorial:")
        display(df[df["Editorial"].isna()].head())
        
        total_filas = len(df)

        vacios_editorial = df["Editorial"].isna().sum()
        