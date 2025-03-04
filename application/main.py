import os
import kivy
kivy.require("2.1.0")

import threading
import time
import requests
from kivymd.app import MDApp
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp

# Load giao diện từ file KV
Builder.load_file("main.kv")

# Cấu hình các thông số retry và timeout (có thể điều chỉnh)
REQUEST_TIMEOUT = 3      # thời gian timeout (giây)
MAX_RETRIES = 3          # số lần thử lại tối đa
RETRY_DELAY = 0.5        # delay ban đầu giữa các lần thử, sau đó có thể tăng dần

def send_http_request(url):
    """Gửi HTTP GET request với cơ chế retry và exponential backoff."""
    tries = 0
    delay = RETRY_DELAY
    while tries < MAX_RETRIES:
        try:
            resp = requests.get(url, timeout=REQUEST_TIMEOUT)
            print("Sent request to", url, "response code:", resp.status_code)
            return True
        except Exception as e:
            tries += 1
            print(f"Error sending request to {url}, try {tries}: {e}")
            time.sleep(delay)
            delay *= 2  # exponential backoff
    print("Max retries reached for", url)
    return False

class ControlPanel(GridLayout):
    def __init__(self, **kwargs):
        super(ControlPanel, self).__init__(**kwargs)
        self.cols = 2
        self.spacing = 10
        self.padding = 10

        # Các trạng thái nút
        self.forward_pressed = False
        self.backward_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        # Base URL (được set từ IP panel)
        self.base_url = ""

    def set_base_url(self, ip):
        self.base_url = "http://" + ip
        print("ControlPanel base URL set to", self.base_url)

    def on_forward_press(self, instance):
        self.forward_pressed = True
        self.update_command()

    def on_forward_release(self, instance):
        self.forward_pressed = False
        self.update_command()

    def on_backward_press(self, instance):
        self.backward_pressed = True
        self.update_command()

    def on_backward_release(self, instance):
        self.backward_pressed = False
        self.update_command()

    def on_left_press(self, instance):
        self.left_pressed = True
        self.update_command()

    def on_left_release(self, instance):
        self.left_pressed = False
        self.update_command()

    def on_right_press(self, instance):
        self.right_pressed = True
        self.update_command()

    def on_right_release(self, instance):
        self.right_pressed = False
        self.update_command()

    def update_command(self):
        cmd = self.determine_command()
        self.send_command(cmd)

    def determine_command(self):
        f = self.forward_pressed
        b = self.backward_pressed
        l = self.left_pressed
        r = self.right_pressed

        if f and l:
            return "/forwardleft"
        elif f and r:
            return "/forwardright"
        elif b and l:
            return "/backleft"
        elif b and r:
            return "/backright"
        elif f:
            return "/forward"
        elif b:
            return "/backward"
        elif l:
            return "/left"
        elif r:
            return "/right"
        else:
            return "/stop"

    def send_command(self, endpoint):
        if not self.base_url:
            print("No IP set in ControlPanel!")
            return
        url = self.base_url + endpoint
        print("Sending command to", url)
        threading.Thread(target=lambda: send_http_request(url)).start()

class MainControl(BoxLayout):
    def on_start(self):
        try:
            user_data = MDApp.get_running_app().user_data_dir
            self.store = JsonStore(os.path.join(user_data, "saved_ips.json"))
            print("JsonStore path:", os.path.join(user_data, "saved_ips.json"))
        except Exception as e:
            print("Error initializing JsonStore:", e)
        self.update_spinner()

    def set_ip(self):
        ip = self.ids.ip_input.text.strip()
        if ip:
            self.ids.control_panel.set_base_url(ip)
            try:
                if not self.store.exists("ips"):
                    self.store.put("ips", list=[ip])
                else:
                    saved = self.store.get("ips")["list"]
                    if ip not in saved:
                        saved.append(ip)
                        self.store.put("ips", list=saved)
                print("IP saved:", ip)
            except Exception as e:
                print("Error saving IP:", e)
            self.ids.ip_input.text = ""
            self.update_spinner()
        else:
            print("No IP entered!")

    def update_spinner(self):
        try:
            if self.store and self.store.exists("ips"):
                saved = self.store.get("ips")["list"]
                self.ids.ip_spinner.values = saved
                if saved:
                    self.ids.ip_spinner.text = saved[0]
            else:
                if self.store:
                    self.ids.ip_spinner.values = []
                    self.ids.ip_spinner.text = "Saved IPs"
        except Exception as e:
            print("Error updating spinner:", e)

    def on_spinner_select(self, spinner, text):
        if text:
            self.ids.control_panel.set_base_url(text)
            print("Selected saved IP:", text)
    
    def on_speed_change(self, value):
        print("Speed changed to:", value)
        # Nếu có nhãn hiển thị tốc độ, cập nhật nó ở đây.
    
class MyKivyApp(MDApp):
    def build(self):
        return MainControl()

    def on_start(self):
        self.root.on_start()
    
    def servo_open(self):
        base_url = self.root.ids.control_panel.base_url
        if base_url:
            url = base_url + "/servoOpen"
            threading.Thread(target=lambda: send_http_request(url)).start()
            print("Servo Open command sent")
        else:
            print("No IP set for servo command.")

    def servo_close(self):
        base_url = self.root.ids.control_panel.base_url
        if base_url:
            url = base_url + "/servoClose"
            threading.Thread(target=lambda: send_http_request(url)).start()
            print("Servo Close command sent")
        else:
            print("No IP set for servo command.")

if __name__ == "__main__":
    MyKivyApp().run()
