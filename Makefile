########################################
######## DEVELOP
##########################################

shell:
	python3 manage.py  shell_plus

migrate:
	python3 manage.py migrate

makemigrations:
	python3 manage.py makemigrations

server:
	python3 manage.py runserver
