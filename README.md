# TestPythonDev
## Python Backend Developer Test  para SPOT

En la implementacion de la solucion se toma como base de los datos JSON identificanco la relacion en la informacion 


```json
{"artistName":"Gunna \u0026 Future","id":"1603748478","name":"pushin P (feat. Young Thug)","releaseDate":"2022-01-06","kind":"songs","artistId":"1236267297","artistUrl":"https://music.apple.com/us/artist/gunna/1236267297","contentAdvisoryRating":"Explict","artworkUrl100":"https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/03/d0/bb/03d0bbde-4315-8bbb-8880-866fc6fdef6d/810043689243.jpg/100x100bb.jpg","genres":[{"genreId":"18","name":"Hip-Hop/Rap","url":"https://itunes.apple.com/us/genre/id18"},{"genreId":"34","name":"Music","url":"https://itunes.apple.com/us/genre/id34"}]

```
se obtiene la relacion en POO con el fin de disemar el ORM y la relacion con las entidades.

![](https://github.com/Templario17/TestPythonDev/blob/main/rootsystem/static/diagrama_clases.png)
## Implementacion en local 
se implementa en cliente-servidor

servidor web HTTPServer de Apache2 en linux Debian10
base de datos en MariaDB
lenguaje de programacion Python3 

Esctructura de directorios del proyecto :
    logs/
    private/
    rootsystem/
        application/
            core/
            modules/
        static/
        
se implemnta un disemo de base de datos realisando un mapero relacional de Objetos en una base de datos de MySql contenido en el archivo *application.sql* en el directorio del rootsistem/application.

La migracion de los datos del json a la base de datos se diseña en el archivo *json_to_db.py*(rootsystem/application) en el cual cuenta con un excrib de lectura de archivo JSON y toma los y los inserta en la base de datos en la tablas diseñadas en el ORM, 


