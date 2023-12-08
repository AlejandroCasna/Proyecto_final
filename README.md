![gift](https://github.com/AlejandroCasna/VoleyStats-Pro/blob/1eb0d8a03e27a9dd85e3ac775496432f4e1b106f/Imagen/VoleyStats-Pro.gif)

* El siguiente proyecto consiste en un encargo realizado por uno de los equipos de la SuperLiga masculina de vóley. 
Se nos informó sobre un problema relacionado con el análisis de estadísticas de los equipos rivales al momento de elaborar un plan de juego. Es fundamental contar con estadísticas de los rivales para poder abordar un plan de juego efectivo. 
`El objetivo´ es mejorar tanto el tiempo y resultados en la obtención de datos sobre los equipos rivales, enfocándose en aspectos como ataque, defensa, recepción y bloqueo.


# Pasos a seguir.

## Obtención de estadísticas de los equipos y sus jugadores.
* Scraping [**Federación Española de Voley**](https://www.rfevb.com/)

* Scraping [**Flasshcore**](https://www.flashscore.es/)

## Base de datos.
* MySQL Worbench
* PostgreSQL

## Visualizacion.
* Streamlit

El resultado de este proceso será la creación de una base de datos sólida y actualizada, alimentada por las estadísticas obtenidas a través del scraping de fuentes confiables como la Federación Española de Vóley y Flashscore. Esta base de datos, gestionada tanto en MySQL Workbench como en PostgreSQL, proporcionará una plataforma integral para el análisis detallado de los equipos y sus jugadores.

Con la ayuda de Streamlit, se logrará una visualización clara y efectiva de las estadísticas recopiladas, permitiendo al equipo en cuestión acceder fácilmente a la información crucial sobre el rendimiento de sus rivales en áreas clave como ataque, defensa, recepción y bloqueo. Este enfoque integral y tecnológicamente avanzado tiene como objetivo mejorar significativamente la toma de decisiones estratégicas, contribuyendo así al éxito y rendimiento óptimo en la liga.

<details>
<summary>PostgresSQL</summary>
<br>
  
![diagrama](https://github.com/AlejandroCasna/VoleyStats-Pro/blob/1eb0d8a03e27a9dd85e3ac775496432f4e1b106f/Imagen/ERG_posgreSQL.png)
</details>



<details>
<summary>Estadísticas por equipo</summary>
<br>

![diagrama](https://github.com/AlejandroCasna/VoleyStats-Pro/blob/078e70a18fb0b569cd32bb23924ab0881668f3cd/Imagen/stats_equipo.png)
</details>

<details>
<summary>Jugadores por equipo</summary>
<br>

![diagrama](https://github.com/AlejandroCasna/VoleyStats-Pro/blob/078e70a18fb0b569cd32bb23924ab0881668f3cd/Imagen/jugadores_quipo.png)
</details>

<details>
<summary>Estadística por jugador</summary>

![diagrama](https://github.com/AlejandroCasna/VoleyStats-Pro/blob/078e70a18fb0b569cd32bb23924ab0881668f3cd/Imagen/stats_jugador.png)
</details>
<br>


# Proximos pasos.

* Desarrollar un mapa de calor a partir de vídeos de vóley con el fin de identificar las áreas del campo de juego a las que los jugadores suelen dirigir sus acciones, teniendo en cuenta diversas circunstancias, como la dirección habitual de la jugada tras la recepción, la posición del colocador, y otras variables relevantes.

* Integrar Streamlit con la base de datos PostgreSQL para garantizar una actualización constante con nuevos datos.

* Desarrollar una aplicación ejecutable que facilite el acceso directo a la página desde dispositivos móviles

# Librerías utilizadas

- [**Python**](https://www.python.org):  El lenguaje de programación principal utilizado para implementar el proceso ETL y llevar a cabo el análisis.

- [**Selenium**](https://www.selenium.dev/documentation/): Una herramienta de automatización web utilizada para interactuar con sitios web y obtener datos de chat de sitios que no proporcionan una API directa.

- [**Sqlalchemy**](https://docs.sqlalchemy.org/en/20/): Una herramienta SQL de Python y un kit de herramientas de ORM que proporciona una manera más sencilla de interactuar con bases de datos SQL.

- [**Re**](https://docs.python.org/3/library/re.html): Una librería en Python para trabajar con expresiones regulares, que son patrones de búsqueda y coincidencia de texto. 

- [**Time**](https://docs.python.org/3/library/time.html): Una librería en Python para trabajar con operaciones relacionadas con el tiempo. Es útil para medir intervalos de tiempo y pausar la ejecución de un programa.

- [**Streamlit**](https://streamlit.io/): Streamlit es un marco de desarrollo de código abierto en Python que simplifica considerablemente la creación de aplicaciones web interactivas y atractivas

- [**Joblib**](https://joblib.readthedocs.io/en/stable/): Una biblioteca de Python para procesar tareas en paralelo. Solo para main.py.

- [**Plotly**](https://plotly.com/python/plotly-express/): Plotly Express es una librería de visualización de datos en Python que proporciona una interfaz fácil de usar para crear gráficos interactivos y visualizaciones estadísticas de manera rápida y sencilla.
