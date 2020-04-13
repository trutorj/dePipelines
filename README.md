# Data analysis pipeline
## Objetivo
El objetivo de este proyecto es crear un un script que al ejecutarse en la terminal, genere de forma automática una series de estadísticas que serán reportadas o bien por la terminal de la consola (en formato tabla y/o gráfica), o guardadas como un informe en un archivo pdf.
## Materiales y Métodos
Como datos de partida, se ha descargado un archivo csv con el conjunto de incendios producidos en California en el periodo 2013-2019 (https://www.kaggle.com/ananthu017/california-wildfire-incidents-20132020). El archivo se encuentra en la carpeta **input**.
### Limpieza de datos y descarga de datos a través de una API
El primer paso ha sido la elección de las variables de interés para el desarrollo del proyecto y la limpieza del dataset resultante. Los procesado de estos datos se encuentra en el archivo *data_cleaning.py*. 
En paralelo, y con el objetivo de enriquecer el dataset, se ha procedido a sacar los datos de población y densidad de población para cada uno de los condados de California, accediendo a ellos mediate la API de la web https://www.census.gov/. Para acceder a estos datos, fue preciso adquirir un token.
El proceso de limpieza de datos se puede resumir en:
* Eliminar duplicados, buscando a través de la columna de identificadores únicos que traía el propio dataset.
* Buscar los NAs y sustituirlos, en nuestro caso, por 0.
* Unir los datos del dataset de incendios con los descargados a través de la API mediante un *merge* .

### Estadística
Por un lado, se ha calculado una estadística básica de incendios de la serie agrupada por condados, que incluye:
* Mayor incendio registrado por condado.
* Menor incendio registrado por condado.
* Número de incendios registrados por condado.
* Valores de población y densidad de población por condado.
Para consultar el proceso seguido, consultar el archivo *b_statistics.py*.
Por otro lado, y con el objeto de resumir y agrupar la información por año, se han calculado:
* Número de incendios producidos cada año
* Superficie total quemada en cada año.
Ambos, con su correspondiente gráfica. En el archivo *do_statistics.py* se encuentran las funciones utilizadas.

### Creación de los informes
Por último, se ha creado un archivo, *main.py*, en el que generar los diferentes informes que se mostrarán por la terminal, mediante gráficas o en pdf, dependiendo de las opciones que se escojan. La salida en pdf se definión en el archivo *pdf_generator.py*.

## Resultados
Finalmente, se procede a describir las funcionalidades del script. 
* --county_stats. Muestra por consola una tabla las estadísticas básicas para cada condado.
* -- variable. Variable a partir de la cual se generará una tabla agrupada que muestra el número de incendios por año si la variable = 'Year' y la superficie quemada por año si la variable = 'HaBurned'.
* -- value. El valor por el que se agregarán los datos. Para la variable Year value debe ser igual a 'count' y para para HaBurned, 'sum'.
* --print. Muestra (y guarda en la carpeta **output**) los gráficos generados para cada tipo de análisis.
* --pdf. Genera un pdf a modo de informe que se encuentra en la carpeta **output**


