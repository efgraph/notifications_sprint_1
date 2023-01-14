from os import getenv

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from jobs import jobs_list

scheduler_thread_pool_str = getenv("SCHEDULER_THREAD_POOL")
if scheduler_thread_pool_str:
    scheduler_thread_pool = int(scheduler_thread_pool_str)
postgres_dsn = getenv("POSTGRES_DSN", "postgresql://postgres:password@localhost:5432")
rabbit_dsn = getenv("RABBIT_DSN", "amqp://guest:guest@localhost:5672/")


class Config:
    JOBS = jobs_list

    SCHEDULER_JOBSTORES = {"default": SQLAlchemyJobStore(url=postgres_dsn)}

    SCHEDULER_EXECUTORS = {
        "default": {"type": "threadpool", "max_workers": 16}
    }

    SCHEDULER_JOB_DEFAULTS = {
        "coalesce": False,
        "max_instances": 4,
    }

    SCHEDULER_API_ENABLED = True
