import os
import signal
import subprocess
import sys

def kill_port(port):
    try:
        if sys.platform.startswith('win'):
            command = f"netstat -ano | findstr :{port}"
            output = subprocess.check_output(command, shell=True).decode()
            if output:
                pid = output.strip().split()[-1]
                os.kill(int(pid), signal.SIGTERM)
                print(f"✅ Port {port} successfully freed (PID: {pid}).")
        else:
            command = f"lsof -ti:{port}"
            pid = subprocess.check_output(command, shell=True).decode().strip()
            if pid:
                os.kill(int(pid), signal.SIGKILL)
                print(f"✅ Port {port} successfully freed (PID: {pid}).")
    except subprocess.CalledProcessError:
        print(f"ℹ️ Port {port} is already free.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    target_port = input("Enter port to kill (default 5000): ") or 5000
    kill_port(target_port)