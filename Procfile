web: gunicorn app:app
main_worker: celery -A app.celery worker --beat --loglevel=info -Q uw --without-gossip --without-mingle --without-heartbeat