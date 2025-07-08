import subprocess
import shutil
import os

def main():
    os.makedirs(r"C:\Program Files\ULFC", exist_ok=True)
    shutil.copy2("ico.ico", r"C:\Program Files\ULFC\icon.ico")
    try:
        subprocess.run(["reg", "import", "set.reg"], check=True)
        print("Registry import completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error importing registry:", e)

if __name__ == "__main__":
    main()
