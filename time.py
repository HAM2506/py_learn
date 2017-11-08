from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    print('Tick! The time is: %s' % datetime.now())

scheduler = BlockingScheduler()

scheduler.add_job(tick, 'date', run_date='2017-11-08 14:36:35')

scheduler.start()