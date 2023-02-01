# Django-Docker
 
ОПИСАНИЕ Проекта
=========================
   
Использльзованы Geodjango & Postgis
--------------------------  
Таблицы созданные в базе данных:
  - Фермер
  - Поле
  - Культура

Таблица Сезон не создана, потому что в году 4 сезона и это величина постоянная. Таким образом мной добавлен **SEASONS_CHOICES** из 4 сезонов и выбор в поле season внутри таблицы Plot.

Функционал:
- в Админ панели есть возможность поиска фермера по имени(first_name) или фамилии(last_name), культуры по названию. Так же их фильтрация в Таблице Plot.
- для отображения фермеру его земель необходима API, которая автоматически генерируется и присвается фермеру при его создании дополнительным полем в таблице **unique_key**, который он прописывает для получения данных своих земель (**localhost:8000/apikey={unique_key}**)
- Фермер может видеть только свои земли, и указывать на каком поле что посеял c помощью Patch запроса с указанием id plot и id culture. 

Имеется возможность развёртывания через docker:
- для этого нужно установить Docker
- клонировать данный репозиторий 
- запустить в терминале в папке проекта команду **docker-compose up**

Для входа в Админ панель введите логин **admin** и пароль **admin**
