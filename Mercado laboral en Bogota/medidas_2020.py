import pandas as pd
import pyreadstat

ruta1 = r"/home/jarold/Escritorio/python/Proyecto_01_Mercado_laboral/Datos/julio_2020_dta/DTA/Fuerza de trabajo.DTA"  
ruta2 = r"/home/jarold/Escritorio/python/Proyecto_01_Mercado_laboral/Datos/julio_2020_dta/DTA/Ocupados.DTA"
ruta3 = r"/home/jarold/Escritorio/python/Proyecto_01_Mercado_laboral/Datos/julio_2020_dta/DTA/Desocupados.DTA"

df1, meta = pyreadstat.read_dta(ruta1)    
df2, meta = pyreadstat.read_dta(ruta2)    
df3, meta = pyreadstat.read_dta(ruta3)  


# población en edad de trabajar (PET)
PET = df1[df1['DPTO'].astype(int) == 11] ['FEX_C'].sum()
# Población ocupada (PO)
PO =  df2[df2['DPTO'].astype(int) == 11 ] ['FEX_C'].sum()
# Población desocupada (PD)
PD = df3[df3['DPTO'].astype(int) == 11 ] ['FEX_C'].sum()
# Población economicamente activa (PEA)
PEA = PO + PD


# MEDIDAS DE MERCADO LABORAL

# Tasa de ocupacion (TO)
TO_20 = PO / PET

# Tasa de desocupacion (TD)
TD_20 = PD / PEA

# Tasa global de participacion (TGP)
TGP_20 = PEA / PET

