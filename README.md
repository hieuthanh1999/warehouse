# docker-compose.yml

* odoo:15
* postgres:14.4-alpine
* pgadmin4
```
sudo chmod -R 777 odoo15/addons
sudo chmod -R 777 odoo15/etc
cd odoo15
docker-compose up -d

```
`localhost:8071`
```

# Odoo configuration

To change Odoo configuration, edit file: **etc/odoo.conf**.
Configuration sample: [www.odoo.com/deploy.html](https://www.odoo.com/documentation/15.0/administration/install/deploy.html#id5)

# Access to PgAdmin:

You can use PgAdmin if you need. It's on port 5050 (127.0.0.1:5050 for example) and default credentials are:

* email: pgadmin4@pgadmin.org
* password: admin

If you don't need PgAdmin, you can comment or delete it in docker-compose.yml.

# Add a new server in PgAdmin:

* Host name/address: db
* Port: 5432
* Username as POSTGRES_USER: odoo
* Password as POSTGRES_PASSWORD: odoo
