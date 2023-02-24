migrate:
	python manage.py migrate

full-migrate:
	python manage.py makemigrations && python manage.py migrate