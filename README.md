Start database server
```shell
docker-compose -f ./docker-compose.yml up -d
```

Create testing database
* login to database container
* use psql to create tesing db

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

Testing
* set PYTHONPATH to project main dir `$env:PYTHONPATH='.'` and run `pytest`
