import subprocess

def deploy():
    subprocess.run(["streamlit", "deploy", "app.py"])

if __name__ == "__main__":
    deploy()
