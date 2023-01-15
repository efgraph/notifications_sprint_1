from config import settings
from flask import Flask
from flask_apscheduler import APScheduler
from jobs import jobs_list
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

app = Flask(__name__)


class Config:
    JOBS = jobs_list
    SCHEDULER_JOBSTORES = {"default": SQLAlchemyJobStore(url=settings.postgres_dsn)}

    SCHEDULER_EXECUTORS = {
        "default": {"type": "threadpool", "max_workers": 16}
    }

    SCHEDULER_JOB_DEFAULTS = {
        "coalesce": False,
        "max_instances": 4,
    }

    SCHEDULER_API_ENABLED = True


app.config.from_object(Config())
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
