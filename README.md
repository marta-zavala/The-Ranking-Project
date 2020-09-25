# Project 4. The Ranking Project

![alt text](https://p.kindpng.com/picc/s/128-1280187_github-logo-png-github-transparent-png.png)

En este proyecto se ha creado una API de GitHub que permite obtener información sobre los labs y alumnos de Ironhack.

La API está desplegada en Heroku. Por ejemplo:

https://the-ranking-project.herokuapp.com/student/all

También puede correr en local mediante un contenedor docker conectado a Atlas aplicando este comando en la terminal:

```
docker run -p 3000:3000 --env DBURL="mongodb+srv://admin:<password>@cluster0.7hkah.mongodb.net/ranking?retryWrites=true&w=majority" --env PORT=3000 the-ranking-api
```

O correr en local conectado a la db local con el siguiente comando:

```
docker run -p 3000:3000 --env DBURL="mongodb://host.docker.internal/ranking" the-ranking-api
```

## ¿Cómo funciona?
Para obtener información debes introducir la url de la api seguido de uno de los siguientes endpoints:
```
https://the-ranking-project.herokuapp.com/<endpoint>
```

### Student Endpoints:
(GET) /student/create/<studentname>
- Purpose: Create a student and save into DB
- Params: studentname the student name
- Returns: student_id

(GET) /student/all
- Purpose: List all students in database
- Returns: An array of student objects

(GET) /student/search/<studentname>
- Purpose: Search all pull request of a student
- Params: The student name
- Returns The student pull request info

### Lab Endpoints:
(POST) /lab/create/<name>
- Purpose: Create a lab to be analyzed.
- Params: The lab-prefix to be analyzed. Example: [lab-scavengers]
- Returns: lab_id

(GET) /lab/<lab_prefix>/search
- Purpose: Search student submissions on specific lab
- Params: user_id
- Returns: Lab analysis
    - Number of open PR
    - Number of closed PR
    - Percentage of completeness (closed vs open)
    - Innstructor grade time in hours: (max, min and mean)

(GET) /lab/<lab>/meme
- Purpose: Get a random meme (extracted from the ones used for each student pull request) for that lab.

