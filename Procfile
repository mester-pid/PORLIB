web: gunicorn app:app
worker: celery -A app.celery worker --loglevel=info -Q uw --without-gossip --without-mingle --without-heartbeat