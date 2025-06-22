Docker:
```
docker build -t rano_ai -f Dockerfile .
```

```
docker run -d --restart unless-stopped -p 8081:80  rano_ai
```



### Nginx
```
sudo nano /etc/nginx/sites-available/rano-ai.u2s.uz
```

```
server {
    listen 80;
    listen [::]:80;
    server_name rano-ai.u2s.uz;

    location /.well-known/acme-challenge/ {
        root /var/www/html;
        allow all;
    }

    location / {
        proxy_pass http://95.216.144.224:8081;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
```
sudo ln -s /etc/nginx/sites-available/rano-ai.u2s.uz /etc/nginx/sites-enabled/
```
```
sudo nginx -t
```

```
sudo systemctl reload nginx
```

### SSL
```
sudo certbot --nginx -d rano-ai.u2s.uz
```
