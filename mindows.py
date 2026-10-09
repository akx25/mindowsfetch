import sys
import os
import platform
import colorama
import psutil
import termcolor
import requests
import argparse
from colorama import init
colorama.init()
#--issue
parser = argparse.ArgumentParser(
    description=(termcolor.colored("mindowsfetch - a system information tool for Windows.", 'cyan', 'on_black'))
)

parser.add_argument(
    "--issue",
    action="store_true",
    help=termcolor.colored("If you have an issue with the tool, contact me on Discord @ak0101101 or GitHub: https://github.com/akx25/mindowsfetch/issues", 'yellow')
)

args = parser.parse_args()

if args.issue:
    print(termcolor.colored("If you have an issue with mindowsfetch contact me on Discord or GitHub:", "yellow"))
    print(termcolor.colored("Discord: @ak0101101", "magenta"))
    print(termcolor.colored("GitHub: https://github.com/akx25/mindowsfetch/issues", 'black', 'on_white'))
    sys.exit(0)



#check if termcolor is installed
def check_termcolor():
    try:
        import termcolor
    except ImportError:
        print(termcolor.colored("termcolor is not installed. Install: https://pypi.org/project/termcolor/'", "red"))
        sys.exit(1)
#check if psutil is installed
def check_psutil():
    try:
        import psutil
    except ImportError:
        print(termcolor.colored("psutil is not installed. Install: https://pypi.org/project/psutil/'", "red"))
        sys.exit(1)
#check if colorama is installed
def check_colorama():
    try:
        import colorama
    except ImportError:
        print(termcolor.colored("colorama is not installed. Install: https://pypi.org/project/colorama/'", "red"))
        sys.exit(1)

#host
def get_host():
    return platform.system()

#os
def get_os():
    return f"{platform.system()} {platform.version()}"

#cpu
def get_cpu():
    return platform.processor()

#gpu
def get_gpu():
    try:
        import subprocess

        result = subprocess.check_output(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"
            ],
            text=True,
            stderr=subprocess.DEVNULL
        )

        gpus = [line.strip() for line in result.splitlines() if line.strip()]

        return ", ".join(gpus) if gpus else "Unknown"

    except Exception:
        return "Unknown"

#memory
def get_memory():
    memory = psutil.virtual_memory()
    return f"{memory.total / (1024 ** 3):.2f} GB"

#disk usage and space
def get_disk():
    disk = psutil.disk_usage("C:\\")
    return f"{disk.total / (1024 ** 3):.2f} GB"

def get_ip_address():
    try:
        import socket

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception:
        return "Unknown"
def get_ip_address_country():

        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data.get("country", "Unknown")

#logo + color
logo = [
    (termcolor.colored("       _.-;;-._ ", "cyan")),
    (termcolor.colored("'-..-'|   ||   |", "cyan")),
    (termcolor.colored("'-..-'|_.-;;-._|", "cyan")),
    (termcolor.colored("'-..-'|   ||   |", "cyan")),
    (termcolor.colored("'-..-'|_.-''-._|", "cyan")),
    (termcolor.colored("                ", "cyan")),
    (termcolor.colored("                ", "cyan")),
    
]

#info thinngs
from termcolor import colored

info = [
    f"{colored('Host:', 'cyan')}   {get_host()}",
    f"{colored('OS:', 'cyan')}     {get_os()}",
    f"{colored('CPU:', 'cyan')}    {get_cpu()}",
    f"{colored('GPU:', 'cyan')}    {get_gpu()}",
    f"{colored('Memory:', 'cyan')} {get_memory()}",
    f"{colored('Disk:', 'cyan')}   {get_disk()}",
    f"{colored('IP:', 'cyan')}     {get_ip_address()} {get_ip_address_country()}",
]

#logo and info placement
for i in range(max(len(logo), len(info))):
    left = logo[i] if i < len(logo) else ""
    right = info[i] if i < len(info) else ""

    print(f"{left:<20} {right}")
