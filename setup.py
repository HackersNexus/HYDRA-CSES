import os
import platform
import sys
import urllib.request

# Apktool version & URLs
APKTOOL_VERSION = "2.12.0"
APKTOOL_JAR_URL = (
    f"https://github.com/iBotPeaches/Apktool/releases/"
    f"download/v{APKTOOL_VERSION}/apktool_{APKTOOL_VERSION}.jar"
)

APKTOOL_LINUX_URL = "https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool"
APKTOOL_WINDOWS_URL = "https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/windows/apktool.bat"

def download_file(url, dest):
    print(f"[*] Downloading {url} → {dest}")
    try:
        urllib.request.urlretrieve(url, dest)
        print(f"[✔] Downloaded: {dest}")
    except Exception as e:
        print(f"[!] Failed to download {url}: {e}")
        sys.exit(1)

def setup_linux_termux(termux=False):
    print("[*] Updating system & installing dependencies...")
    if termux:
        os.system("apt update -y && apt upgrade -y")
        os.system("pkg install -y python openjdk-17 wget")
        pip_cmd = "pip"
    else:
        os.system("sudo apt update -y && sudo apt upgrade -y")
        os.system("sudo apt install -y python3 python3-pip openjdk-17-jdk wget")
        pip_cmd = "pip3"

    print("[*] Installing Python requirements...")
    os.system(f"{pip_cmd} install -r requirements.txt")

    # Download apktool files
    current_dir = os.getcwd()
    apktool_jar = os.path.join(current_dir, "apktool.jar")
    apktool_wrapper = os.path.join(current_dir, "apktool")

    if not os.path.exists(apktool_jar):
        download_file(APKTOOL_JAR_URL, apktool_jar)

    download_file(APKTOOL_LINUX_URL, apktool_wrapper)
    os.chmod(apktool_wrapper, 0o755)

    print("[✔] Apktool setup complete on Linux/Termux.")

def setup_windows():
    print("[*] Installing Python requirements...")
    os.system("pip install -r requirements.txt")

    # Download apktool files
    current_dir = os.getcwd()
    apktool_jar = os.path.join(current_dir, "apktool.jar")
    apktool_bat = os.path.join(current_dir, "apktool.bat")

    if not os.path.exists(apktool_jar):
        download_file(APKTOOL_JAR_URL, apktool_jar)

    download_file(APKTOOL_WINDOWS_URL, apktool_bat)

    print("[✔] Apktool setup complete on Windows.")
    print("[!] Please ensure Java (JDK) is installed manually on Windows.")

if __name__ == "__main__":
    os_type = platform.system().lower()

    if os_type == "windows":
        setup_windows()
    else:
        if "com.termux" in os.environ.get("PREFIX", ""):
            setup_linux_termux(termux=True)
        else:
            setup_linux_termux(termux=False)

    print("\n[✔] Setup finished successfully!")
    print("Run the tool using:\n")
    print("   python3 main.py" if os_type != "windows" else "   python main.py")
