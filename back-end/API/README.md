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
CREATE DATABASE H2024;
USE H2024;
CREATE TABLE user (
    id int not null auto_increment,
    name varchar(255) ,
    email varchar(255) ,
    password varchar(255) ,
    admin boolean ,
    primary key (id)
);
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON H2024.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

### Setting up the environment variables
Créer un .env dans le répertoire /API avec les variables suivantes:
```env
DATABASE_TEST_URL=mysql+pymysql://admin:admin@localhost/H2024
DATABASE_DEV_URL=mysql+pymysql://admin:admin@localhost/H2024test

SECRET_KEY=secret
```

### Starting the server
```bash
flask run
```

### Running the tests

Créer la base de données de test avec ce script:
```sql
CREATE DATABASE H2024test;
USE H2024test;
CREATE TABLE todo (
    id int not null auto_increment,
    task varchar(255) ,
    completed boolean ,
    primary key (id)
);
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON H2024test.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

Lancer les tests avec la commande:
```bash
pytest
```

