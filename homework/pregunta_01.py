"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re

   
    with open('./files/input/clusters_report.txt', 'r', encoding='utf-8') as archivo:
        lines = archivo.readlines()

   
    filas_utiles = [
        line.strip()
        for line in lines[4:]
        if line.strip() and not line.startswith('-')
    ]

    data = []
    cluster = cantidad = porcentaje = None
    acumulador = []

    for line in filas_utiles:
       
        match = re.match(r'^(\d+)\s+(\d+)\s+([\d,]+)\s%?\s*(.*)', line)
        
        if match:
          
            if cluster is not None:
                palabras_final = ' '.join(acumulador).strip()
                palabras_final = re.sub(r'\s+', ' ', palabras_final) 
                palabras_final = palabras_final.replace('.', '').lower()
                palabras_final = ', '.join(p.strip() for p in palabras_final.split(','))
                palabras_final = palabras_final.strip(', ')
                data.append([cluster, cantidad, porcentaje, palabras_final])
                acumulador = []

            
            cluster = int(match.group(1))
            cantidad = int(match.group(2))
            porcentaje = float(match.group(3).replace(',', '.'))
            resto = match.group(4)
            if resto:
                acumulador.append(resto)
        else:
           
            acumulador.append(line)

   
    if cluster is not None:
        palabras_final = ' '.join(acumulador).strip()
        palabras_final = re.sub(r'\s+', ' ', palabras_final)
        palabras_final = palabras_final.replace('.', '').lower()
        palabras_final = ', '.join(p.strip() for p in palabras_final.split(','))
        palabras_final = palabras_final.strip(', ')
        data.append([cluster, cantidad, porcentaje, palabras_final])

    # Crear el DataFrame
    df = pd.DataFrame(data, columns=[
        'cluster',
        'cantidad_de_palabras_clave',
        'porcentaje_de_palabras_clave',
        'principales_palabras_clave'
    ])
    return df
  
