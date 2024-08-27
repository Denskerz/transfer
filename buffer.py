import os
import schedule
import time
import paramiko
import base64
import logging
from subprocess import check_output, CalledProcessError

# SSH connection details
SSH_HOST = "172.30.56."
SSH_USER = "graf_user"
SSH_PASSWORD = "graf_pao_user"

encoded_user = base64.b64encode(SSH_USER.encode()).decode()
encoded_password = base64.b64encode(SSH_PASSWORD.encode()).decode()

kinit_command = "kinit -kt ~/admin.keytab admin@HDP.TEST"
kinit_args = kinit_command.split(' ')

# Logging configuration
logging.basicConfig(
    filename='scheduled_kinit.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

host_end_list = ["46", "47", "48", "49", "50"]


def run_kinit():
    try:
        output = check_output(kinit_args, universal_newlines=True)
        logging.info("kinit command executed.")
        print(output)
    except CalledProcessError as e:
        logging.error(f"Error running kinit: {e}")

    for host_end in host_end_list:
        host = SSH_HOST + hostend
        try:
            # Establish SSH connection
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=SSH_USER, password=SSH_PASSWORD)

            # Execute the kinit command on the remote server
            stdin, stdout, stderr = ssh.exec_command(kinit_command)
            output = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            if error:
                logging.error(f"Server Error executing kinit on the {host}: {error}")
            else:
                logging.info(f"kinit command executed on the {host}: {output}")

            # Close the SSH connection
            ssh.close()
        except Exception as e:
            logging.error(f"Error connecting to the remote server {host}: {e}")

# Scheduling the script to run daily at 12:00 AM (midnight)
schedule.every(1).minutes.do(run_kinit)

while True:
    schedule.run_pending()
    time.sleep(30)

