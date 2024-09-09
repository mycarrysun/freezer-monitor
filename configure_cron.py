import os
from crontab import CronTab


def configure_cron():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = f"{current_dir}/main.py"

    # Command to run every 5 minutes
    command = f"python {script_path} >> {current_dir}/main.log"

    # Access the current user's crontab
    cron = CronTab(user=True)

    # Add the job if it doesn't exist
    if not job_exists(cron, command):
        job = cron.new(command=command)
        job.minute.every(5)
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
