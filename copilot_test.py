import os
import time

def get_uptime():
    try:
        # For Unix/Linux systems
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(time.strftime('%H:%M:%S', time.gmtime(uptime_seconds)))
            print(f"System Uptime: {uptime_string}")
    except FileNotFoundError:
        # For Windows
        import subprocess
        output = subprocess.check_output("net stats workstation", shell=True, text=True)
        for line in output.split('\n'):
            if "Mithun Statistics since" in line:
                print(f"System Uptime: {line.strip()}")
                break

if __name__ == "__main__":
    get_uptime()
