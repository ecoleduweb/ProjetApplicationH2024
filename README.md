# ProjetApplicationH2024

# API

## Developing

### Prerequisites
Se mettre dans le répertoire /API
```bash
pip install flask
pip install Flask-SQLAlchemy
pip install Flask-Migrate
pip install mariadb
pip install pymysql
```
### Setting up the database (not required)
```
USE todo;
CREATE TABLE todo (
    id int not null auto_increment,
    task varchar(255) ,
    completed boolean ,
    primary key (id)
);
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON todo.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
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
