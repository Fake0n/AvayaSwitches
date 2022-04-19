import paramiko
import time
import socket
from pprint import pprint
import re

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
            for i in dict.values(result): # вывод, если нужна какая-то информация о выполнении
                pprint(devices)
                pprint(re.sub("[\r]", "", i))
        return result


if __name__ == "__main__":
    with open('path', 'r') as file: # Нужно указать полный путь к файлу С:/.../xxxx.txt
        lines = file.readlines()
        for devices in lines:
            devices=devices.strip()[:] # Нужно для того, чтобы при чтении файла удалить лишний символ переноса строки '\n', чтобы посдставлялся корректный IP.
            commands = ['sh clock','sh cli info'] # Здесь нужно указать нужные команды последовательно (так, как вводили бы вручную).
            result = send_show_command(f"{devices}", "login", "password", commands)
