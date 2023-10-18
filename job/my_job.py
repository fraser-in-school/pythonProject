from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import download.task as task


def my_job():
    # 这里编写您的定时任务逻辑
    now = datetime.datetime.now()
    print(f"定时任务执行于：{now}")
    task.run()


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    # 设置每天的执行时间（这里设定为每天的凌晨1点）
    scheduler.add_job(my_job, 'cron', hour=18, minute=39)
    scheduler.start()
