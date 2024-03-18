# API

## Developing

### Prerequisites
Se mettre dans le répertoire /API
```bash
pip install -r requirements.txt
```

### Setting up the database (not required)
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
GRANT ALL PRIVILEGES ON H2024.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
```

### Setting up the environment variables
Créer un .env dans le répertoire /API avec les variables suivantes:
```env
DATABASE_TEST_URL=mysql+pymysql://admin:admin@localhost/H2024test
DATABASE_DEV_URL=mysql+pymysql://admin:admin@localhost/H2024

SECRET_KEY=secret
```
### Setting migration
```bash
flask db init
flask db migrate -m "Nom_de_la_migration"(cree une nouvelle migration)
flask db upgrade (pour update les changements)
flask db downgrade (pour revenir en arriere)
flask db history (voir toutes les migration)
```
### Starting the server
```bash
flask db branches (Afficher les points de branchement actuels)
flask run
```

#### Starting the server on all the network
```bash
flask run --host=0.0.0.0
```

### Running the tests

Créer la base de données de test avec ce script:
```sql
CREATE DATABASE H2024test;
USE H2024test;
CREATE TABLE user (
    id int not null auto_increment,
    name varchar(255) ,
    email varchar(255) ,
    password varchar(255) ,
    admin boolean ,
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