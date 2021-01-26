migrate:
	docker-compose run web python manage.py migrate

make_migrations:
	docker-compose run web python manage.py makemigrations

load_data:
	docker-compose run web python manage.py load_scenario_data

run_app:
	docker-compose up web -d

# The below may need some more work
#test:
#	docker-compose run web python manage.py test

bash:
	docker-compose run  bash

echo:
	echo "This should work"