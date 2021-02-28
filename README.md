Start database server
```shell
docker-compose -f .\docker-compose.yml up -d
```

Start application
```shell
export FLASK_ENV='development'
export FLASK_APP="app:create_app('dev')"
flask run
```

```powershell
$env:FLASK_ENV='development'
$env:FLASK_APP="app:create_app('dev')"
flask run
```
