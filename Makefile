mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

user:
	python3 manage.py createsuperuser

run:
	python3 manage.py runserver

flower:
	celery -A root.celery.app flower --port=5001

bit:
	celery -A root beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler


