import paramiko
import time
import socket
from pprint import pprint


def send_show_command(
    ip,
    username,
    password,
    command,
    max_bytes=60000,
    short_pause=0.5,
    long_pause=2,
):
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(
        hostname=ip,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )

    with cl.invoke_shell() as ssh:
        ssh.send("terminal length 0\n")
        time.sleep(short_pause)
        ssh.recv(max_bytes)

        result = {}
        for command in commands:
            ssh.send(f"{command}\n")
            ssh.settimeout(5)
            output = ""
            while True:
                try:
                    part = ssh.recv(max_bytes).decode("utf-8")
                    output += part
                    time.sleep(0.5)
                except socket.timeout:
                    break
            result[devices] = output

        return result


if __name__ == "__main__":
    with open('path to file', 'r') as file:
        lines = file.readlines()
        for devices in lines:
            devices=devices[:10]
            commands = ['sh memory-utilization']
            result = send_show_command(f"{devices}", "login", "password", commands)
            pprint(result)
