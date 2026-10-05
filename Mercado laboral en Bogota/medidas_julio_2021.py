import pandas as pd
import pyreadstat

# RUTAS DE LOS ARCHIVOS DTA PARA EL AÑO 2021
ruta1 = r"/home/jarold/Escritorio/python/Proyecto_01_Mercado_laboral/Datos/Julio_2021_dta/area - Fuerza de trabajo.dta"
ruta2 = r"/home/jarold/Escritorio/python/Proyecto_01_Mercado_laboral/Datos/Julio_2021_dta/area - Ocupados.dta"
ruta3 = r"/home/jarold/Escritorio/python/Proyecto_01_Mercado_laboral/Datos/Julio_2021_dta/area - Desocupados.dta"

# LEER LOS ARCHIVOS DTA PARA EL AÑO 2021
df1, meta = pyreadstat.read_dta(ruta1)    
df2, meta = pyreadstat.read_dta(ruta2)    
df3, meta = pyreadstat.read_dta(ruta3)    

# PRIMERO SE CALCULAN LAS VARIABLES PARA BOGOTA (julio de 2021)

# población en edad de trabajar (PET)
PET = df1[df1['DPTO'].astype(int) == 11] ['fex_c_2011'].sum()
# Población ocupada (PO)
PO =  df2[df2['DPTO'].astype(int) == 11 ] ['fex_c_2011'].sum()
# Población desocupada (PD)
PD = df3[df3['DPTO'].astype(int) == 11 ] ['fex_c_2011'].sum()
# Población economicamente activa (PEA)
PEA = PO + PD

# MEDIDAS DE MERCADO LABORAL
# Tasa de ocupacion (TO)
TO_21 = PO / PET

# Tasa de desocupacion (TD)
TD_21 = PD / PEA

# Tasa global de participacion (TGP)
TGP_21 = PEA / PET


  
