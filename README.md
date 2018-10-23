# Django Boilerplate with django and react with docker-compose

You should need to use Docker Compose to get this app running. To do so:

## To start postgres:
		docker-compose up db 

## To create and run migrations:
		docker-compose up makemigrations
		docker-compose up migrate

## To load sample data:
		docker-compose up load_sample_data

## To run the app:
        docker-compose up web

## Navigate to:
		localhost:8001

# For Thunder:

## Your api should be at:
	
	http://localhost:8001/api/v1.0/scenario/default?limit=0&offset=0

## Home page is:

	http://localhost:8001/home/

## For Cornell Tech students:

If you used this, cite it in your README (This was from Khoa) file like this:

###### Thanks to:
We used Django boilerplate found here: https://github.com/Vchabs/django_boilerplate 
Made by: Vishaal Chhabria and Omari "Thunder" Powell to get rolling
