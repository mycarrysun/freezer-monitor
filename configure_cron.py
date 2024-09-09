import os
from crontab import CronTab


def configure_cron():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Command to run every 5 minutes
    command = f"cd {current_dir} && ./main.sh >> main.log 2>&1"

    # Access the current user's crontab
    cron = CronTab(user=True)

    # Add the job if it doesn't exist
    if not job_exists(cron, command):
        job = cron.new(command=command)
        job.minute.every(1)
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
    configure_cron()
