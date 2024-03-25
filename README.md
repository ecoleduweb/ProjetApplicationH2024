# Serveur Proxy

Installation et configuration du serveur proxy.

Celui-ci sert à proxy les deux serveurs web locaux, qui utilisent deux ports différents, pour que ceux-si utilisent le même domaine.

## Avant quoi que ce soit
Assurez vous que le domaine/sous-domaine pointe vers l'adresse IP publique du serveur.

## Installation de NGINX

Uutilisez le gestionnaire de packets apt.

```bash
sudo apt-get install nginx -y
```

### Configuration

Pour la configuration du certificat SSL avec Certbot, il faut laisser la configuration par défaut de nginx.

(/etc/nginx/sites-available/default)

## Installation de Certbot (gestion des certificats SSL Let's Encrypt)

Uutilisez le gestionnaire de packets [snapd](https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal&tab=standard).
```bash
sudo snap install --classic certbot
```
### Configuration
Préparation de la commande certbot
```
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```
Création du certificat SSL (suivez les étapes)
```
sudo certbot --nginx
```

Les certificats SSL sont maintenant créés.
## Configuration du proxy Nginx.

Exécutez la commande suivante
```
sudo nano /etc/nginx/sites-available/default
```
Collez la configuration suivante en modifiant les valeurs en fonction de votre situation.
Les lignes suivantes doivent être concervées à partir du fichier "default" original;
```
ssl_certificate /etc/letsencrypt/live/VOTRE_DOMAINE/fullchain.pem; 
ssl_certificate_key /etc/letsencrypt/live/VOTRE_DOMAINE/privkey.pem;
```

```                                                                                     
  GNU nano 6.2                                                                                        default                                                                                                 
server {
    listen 443 ssl;
    listen [::]:443 ssl;

    server_name prod.domain.ca;

    ssl_certificate /etc/letsencrypt/live/prod.domain.ca/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/prod.domain.ca/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        proxy_pass http://localhost:5173;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /api {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-NginX-Proxy true;
        proxy_pass http://localhost:5000/;
        proxy_ssl_session_reuse off;
        proxy_set_header Host $http_host;
        proxy_cache_bypass $http_upgrade;
        proxy_redirect off;
        }

    # Other SSL and HTTPS configurations
}

server {
    if ($host = prod.domain.ca) {
        return 301 https://$host$request_uri;
    }

    listen 80;
    listen [::]:80;
    server_name prod.domain.ca;
    return 404;
}

```

Puis redémarrez Nginx
```
sudo service nginx restart
```

### Autre documentations
[CertBot](https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal&tab=standard)\
[Issue StackOverflow](https://stackoverflow.com/questions/44425654/nginx-react-node-lets-encrypt-how-to-point-nginx-at-my-react-app)
