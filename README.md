#API_testwork
The project was completed according to the requirements below.
---

Требования и задачи
Используя один из framework (Flask, Django, FastApi) создать микросвервис:
Задача сервиса - на запрос   
GET /api/meta 
вернуть список файлов и директорий с датой их создания которые находятся в указанной директории.
#Использование Docker, сервис должен запускаться с помощью docker-compose up.


#Used in the project 
FastAPI framework, OS package

---
#This simple model "get FastAPI" .
To display information, I took a list of all files and folders "os.listdir" (without an argument, displays both). 
Then, using the generator, I fill the dictionary along with the necessary data.
If there is no such directory, then i raise an error.
