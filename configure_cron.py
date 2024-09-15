import os
from crontab import CronTab
current_dir = os.path.dirname(os.path.abspath(__file__))

def configure_cron(command, schedule):
    print(f'Configuring command: {command}')
    print(f'on schedule: {schedule}')

    cron = CronTab(user=True)

    if not job_exists(cron, command):
        job = cron.new(command=command)
        job.setall(schedule)
        cron.write()
        print("Cron job added successfully.")
    else:
        print("Cron job already exists.")


def job_exists(cron, command):
    for job in cron:
        if job.command == command:
            return True
    return False


if __name__ == "__main__":
    configure_cron(
        command=f'cd {current_dir} && ./main.sh >> "main.$(date \'+%Y-%m-%d %H:%M:%S\').log" 2>&1',
        schedule='* * * * *'
    )
    configure_cron(
        command=f'cd {current_dir} && ./clean-logs.sh >> "clean-logs.$(date \'+%Y-%m-%d %H:%M:%S\').log" 2>&1',
        schedule='0 0 * * *'
    )
