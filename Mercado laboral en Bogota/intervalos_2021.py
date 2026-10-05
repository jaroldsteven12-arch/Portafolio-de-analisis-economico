import pandas as pd
import pyreadstat

# Bogota 2021
ruta1 = r"/home/jarold/Escritorio/python/Proyecto_01_Mercado_laboral/Datos/Julio_2021_dta/µrea - Caracter¡sticas generales (Personas).dta"
ruta2 = r"/home/jarold/Escritorio/python/Proyecto_01_Mercado_laboral/Datos/Julio_2021_dta/area - Desocupados.dta"
carac, meta = pyreadstat.read_dta(ruta1)
deso, meta = pyreadstat.read_dta(ruta2)


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
resultados_2021 = (
    desocupados[desocupados['DPTO'] == 11]
    .groupby('grupo_edad', observed=True)['fex_c_2011']
    .sum()
)

