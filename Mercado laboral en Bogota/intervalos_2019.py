import pandas as pd
import pyreadstat

# Bogota 2019
ruta1 = r"/home/jarold/Escritorio/python/Proyecto_01_Mercado_laboral/Datos/Julio_2019_dta/Área - Características generales (Personas).dta"
ruta2 = r"/home/jarold/Escritorio/python/Proyecto_01_Mercado_laboral/Datos/Julio_2019_dta/Área - Desocupados.dta"
carac, meta = pyreadstat.read_dta(ruta1)
deso, meta = pyreadstat.read_dta(ruta2)

# Filtrar las columnas necesarias del DataFrame desocupados
desocupados = deso.loc[:, ['DIRECTORIO', 'SECUENCIA_P', 'ORDEN', 'HOGAR','DPTO', 'fex_c_2011']]

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


desocupados['grupo_edad'] = pd.cut(
    desocupados['P6040'],
    bins=rangos,
    labels=labels
)
resultados_2019 = (
    desocupados[desocupados['DPTO'] == 11]
    .groupby('grupo_edad', observed=True)['fex_c_2011']
    .sum()
)

print(resultados_2019)








        