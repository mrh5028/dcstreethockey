# dcstreethockey

## Clone and run using docker
1. [install_docker](https://docs.docker.com/engine/installation/)
1. [install_docker-compose](https://docs.docker.com/compose/install/)
1. [fork](https://help.github.com/articles/fork-a-repo/) and [clone](https://help.github.com/articles/cloning-a-repository/) repo
1. docker-compose up
1. Stop that process Ctrl+c
1. Download test data set
1. docker-compose run --rm web python manage.py loaddata working-herokudump.json
1. docker-compose up 

## Clone and Run in localhost
1. [download postgres](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#linux) 
   - [generic instructions here](https://www.postgresql.org/download/linux/)
1. [fork](https://help.github.com/articles/fork-a-repo/) and [clone](https://help.github.com/articles/cloning-a-repository/) repo
1. activate virtual environment 
   - pip install virtualenv (if you don't already have virtualenv)
   - cd to dcstreethockey folder
   - virtualenv venv (first time only)
   - source venv/bin/activate
1. pip install -r requirements.txt
1. ./manage.py runserver

## Deploy - keeps dev and heroku in sync
1. ./manage.py makemigrations
1. ./manage.py migrate
1. git push heroku master
1. heroku run python ./manage.py migrate
1. git push origin master

## Ensure DJANGO_SETTINGS_MODULE is set for production deployments
1. heroku config:set DJANGO_SETTINGS_MODULE=dcstreethockey.settings.production

## Create backup of heroku database and restore in local postgres instance
1. heroku pg:backups:capture
1. heroku pg:backups:download
1. Restore downloaded db to local postgres instance: 
   - pg_restore --verbose --clean --no-acl --no-owner -h localhost -U user -d dcstreethockey latest.dump.[backup number]
1. https://devcenter.heroku.com/articles/heroku-postgres-import-export

### Dump Heroku data to json file
1. heroku run ./manage.py dumpdata > herokudump.json --indent 2

## Import/Export CSV file to local postgres db
1. Copy data from CSV - You can specify the columns to read:
   - \copy leagues_stat(assists,goals_against,player_id, season_id,team_id, division_id, matchup_id, empty_net, goals) FROM '/Users/stirling/Downloads/stats.csv' DELIMITER ',' CSV HEADER
   - Remove HEADER if there is no header in the first row.
1. Copy data from PostgreSQL table to csv file:
   - \copy leagues_player TO '/Users/stirling/Downloads/sunday_players.csv' DELIMITER ',' CSV HEADER
   - Remove HEADER if there is no header in the first row.
   
## Push local database to heroku
1. Create backup! https://devcenter.heroku.com/articles/heroku-postgres-import-export 
1. export DATABASE_URL=$(heroku config:get DATABASE_URL -a dcstreethockey 
1. heroku pg:reset DATABASE_URL
1. heroku pg:push dcstreethockey DATABASE_URL --app dcstreethockey
