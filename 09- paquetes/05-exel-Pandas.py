import pandas as pd

# Especifica la ruta del archivo Excel
ruta_archivo_excel = "C:\\Users\\Parraguez\\Desktop\\fruta.xlsx"

# Lee el archivo Excel en un DataFrame de Pandas
df = pd.read_excel(ruta_archivo_excel)

# Muestra el DataFrame
print(df["Nombre Apellido"])
