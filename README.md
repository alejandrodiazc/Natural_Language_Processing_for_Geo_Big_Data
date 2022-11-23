# Negocios en Nuevo Leon (Natural_Language_Processing_for_Geo_Big_Data)

<p align="center">
  <a href="https://www.inegi.org.mx"><img src="https://user-images.githubusercontent.com/67669430/203458100-1e10d159-3f62-4016-8829-4b9176e3daac.png" width="15%" height="15%">
</p>

El Instituto nacional de Estadistica, Geografia e Informatica (INEGI), cuenta con informacion de toda la poblacion del pais y sus negocios. Esta información se obtiene mediante censos cada dácada y aunque esta sea de acceso publico, no hay una manera simple de consultarla, evitando el aprovechamiento de todo su potencial para la creacion de nuevos negocios. Para solucionar este problema, se creará un chatbot que permita obtener información de las bases de datos mediante preguntas sencillas. Para lograr esto, es necesario utilizar diferentes herramientas e integrarlas, siendo la principal el procesamiento natural de lenguaje (NLP), dividendo el proyecto en dos secciones principales: Chatbot y busqueda de informcion. 



## Chatbot

<p align="center">
  <a href="https://www.neuraan.com"><img src="https://user-images.githubusercontent.com/67669430/203458027-17464d5d-4383-4852-8ea3-184859899117.png" width="15%" height="15%">
</p>



Neuraan es una compañia apasionada por mejorar el entendimiento de las maquinas con el ser humano, de una manera natura, como una comunicación uno a uno. Mediante su API especializada en el idioma español, se realizan las interacciones con usuarios mediante texto. Los usuarios proporcionan el tipo de negocio y ubicacion deseada a lo cual, el chtabot responde con los negocios similares en esa zona y sus caracterisicas. Para que esto sea posible, se entreno una base de conocimiento con los diferentes negocios, colonias y coidgos postales de Nuevo Leon, permitiendo que el programa logre extraer la informacion necesaria para la busqueda.



## Busqueda de Negocios

Cuando el usuario le proporciona la informacion necesaria al chatbot, comienza la busqueda de caracteristicas de negocios similares y la prediccion. Utilizando Pyspark, se extrae la informacion del INEGI y se separan las variables seleccionadas. Utilizando queries en SQL se van obteniendo las caracteristicas de la zona seleccionada y se comparan con las de negocios con el mismo giro en la ubicacion. Finalmente, utilizando machine learning, se realiza una prediccion acerca de si es viable o no poner el negocio.
