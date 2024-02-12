# API

## Developing

### Prerequisites
Se mettre dans le répertoire /API
```bash
pip install flask
pip install Flask-SQLAlchemy
pip install mariadb
pip install pymysql
pip install flask cors
pip install python-dotenv
pip install PyJWT
pip install virtualenv
```

### Setting up the database
Créer la base de données avec ce script:
```sql
CREATE DATABASE todo;
USE todo;
CREATE TABLE user (
    id int not null auto_increment,
    task varchar(255) ,
    completed boolean ,
    primary key (id)
);
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON todo.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

### Setting up the environment variables
Créer un .env dans le répertoire /API avec les variables suivantes:
```env
DATABASE_TEST_URL=mysql+pymysql://admin:admin@localhost/TODO

DATABASE_DEV_URL=mysql+pymysql://admin:admin@localhost/TODOTEST
```

### Starting the server
```bash
flask run
```

### Running the tests

Créer la base de données de test avec ce script:
```sql
CREATE DATABASE todotest;
USE todotest;
CREATE TABLE todo (
    id int not null auto_increment,
    task varchar(255) ,
    completed boolean ,
    primary key (id)
);
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON todotest.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

```bash
pytest
```

