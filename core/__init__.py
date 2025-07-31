from celery import Celery

celeryApp = Celery('core',
                   broker='redis://localhost:6379/0',
                   backend='redis://localhost:6379/0',
                   include=['core.tasks'])

celeryApp.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='Asia/Shanghai',
    enable_utc=True,
    task_track_started=True,
    worker_prefetch_multiplier=4,
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    task_time_limit=300,  # 5 minutes
)