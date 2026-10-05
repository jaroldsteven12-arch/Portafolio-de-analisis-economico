import pandas as pd
import pyreadstat

# LEER LOS ARCHIVOS NECESARIOS PARA OBTENER LAS VARIABLES
ruta2 = r"Proyecto_01_Mercado_laboral\Datos\Julio_2019_dta\Área - Características generales (Personas).dta".replace('\\', '/')
ruta3 = r"Proyecto_01_Mercado_laboral\Datos\Julio_2019_dta\Área - Ocupados.dta".replace('\\', '/')
ruta4 = r"Proyecto_01_Mercado_laboral\Datos\Julio_2019_dta\Área - Desocupados.dta".replace('\\', '/')

# Leyendolos con pyreadstat por lo antiguos
df2, meta = pyreadstat.read_dta(ruta2)    
df3, meta = pyreadstat.read_dta(ruta3)    
df4, meta = pyreadstat.read_dta(ruta4)    

# PRIMERO SE CALCULAN LAS VARIABLES PARA BOGOTA (julio de 2019)
# población en edad de trabajar (PET)
PET = df2[(df2['DPTO'].astype(int) == 11) & (df2['P6040'] >= 12)] ['fex_c_2011'].sum()
# Población ocupada (PO)
PO =  df3[df3['DPTO'].astype(int) == 11 ] ['fex_c_2011'].sum()
# Población desocupada (PD)
PD = df4[df4['DPTO'].astype(int) == 11 ] ['fex_c_2011'].sum()
# Población economicamente activa (PEA)
PEA = PO + PD


# MEDIDAS DE MERCADO LABORAL
# Tasa de ocupacion (TO)
TO_19 = PO / PET

# Tasa de desocupacion (TD)
TD_19 = PD / PEA

# Tasa global de participacion (TGP)
TGP_19 = PEA / PET
