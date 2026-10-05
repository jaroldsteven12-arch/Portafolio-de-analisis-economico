import pandas as pd
import pyreadstat

# Bogota 2020
ruta1 = r"/home/jarold/Escritorio/python/Proyecto_01_Mercado_laboral/Datos/julio_2020_dta/DTA/caracteristicas_generales.DTA (codificación no válida)"
ruta2 = r"/home/jarold/Escritorio/python/Proyecto_01_Mercado_laboral/Datos/julio_2020_dta/DTA/Desocupados.DTA"
carac, meta = pyreadstat.read_dta(ruta1)
deso, meta = pyreadstat.read_dta(ruta2)

desocupados = deso.loc[:, ['DIRECTORIO', 'SECUENCIA_P', 'ORDEN', 'HOGAR','DPTO', 'FEX_C']]

# Definir la lista con los 4 nombres de columna que forman la llave
llave_compuesta = ['DIRECTORIO', 'SECUENCIA_P', 'ORDEN', 'HOGAR']

# Crear la columna clave concatenada en ambos DataFrames
carac['llave'] = carac[llave_compuesta].astype(str).agg('-'.join, axis=1)
desocupados['llave'] = desocupados[llave_compuesta].astype(str).agg('-'.join, axis=1)

# Mapea los valores directamente creando la nueva columna en df2
desocupados = desocupados.merge(
    carac[['llave', 'P6040']], 
    on='llave', 
    how='left'
)  

desocupados['DPTO'] = desocupados['DPTO'].astype(int)

# Rangos
rangos = [11, 21, 31, 41, 51, 62]
# Etiquetas
labels = ['12-21', '22-31', '32-41', '42-51', '52-62']

# Etiqueta los datos por rango de edad
desocupados['grupo_edad'] = pd.cut(
    desocupados['P6040'],
    bins=rangos,
    labels=labels
)
# Agrupa por etiquetas
resultados_2020 = (
    desocupados[desocupados['DPTO'] == 11]
    .groupby('grupo_edad', observed=True)['FEX_C']
    .sum()
)


