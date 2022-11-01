# Anote

## API для информационного портала на Django REST Framework

##### Функционал проекта

* Кастомная модель пользователя
* Статьи, категории статей, комментарии к статьям


get **/api/v1/{id}**
get **/api/v1/all**
get, put **/api/v1/account/{id}**


get **/api/v1/portal/article/all**
post **> /api/v1/portal/article/create**
get, put, delete **/api/v1/portal/article/{id}**


get **/api/v1/portal/category/all**
get **/api/v1/portal/category/{category_id}**


post **/api/v1/portal/comment/create**
put, delete **/api/v1/portal/comment/{id}**