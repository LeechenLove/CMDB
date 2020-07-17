###### **查看版本**
python -m django --version
###### **创建项目**
django-admin startproject mysite
###### **运行服务**
python manage.py runserver
###### **创建应用**
python manage.py startapp polls
###### **生成数据库迁移文件**
python manage.py makemigrations polls
###### **查看迁移执行的SQL**
python manage.py sqlmigrate polls 0001 
###### **应用数据库迁移**
python manage.py migrate
###### **django shell**
python manage.py shell
###### **创建管理员账号**
python manage.py createsuperuser
###### **运行测试用例**
python manage.py test polls 