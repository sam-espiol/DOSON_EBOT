import tkinter as tk
import requests

# Replace with your ESP32's IP address
ESP32_BASE_URL = "http://192.168.4.1"

class RobotController:
    def __init__(self, master):
        self.master = master
        self.master.title("ESP32 WASD Controller")

        # A set to keep track of all currently pressed keys
        self.pressed_keys = set()

        # Bind key press and key release events
        self.master.bind("<KeyPress>", self.on_key_down)
        self.master.bind("<KeyRelease>", self.on_key_up)

        # Optional: Label instructions
        label = tk.Label(
            master, 
            text="Use W/A/S/D or Arrow keys to control the robot.\n"
                 "Press multiple keys for combined commands."
        )
        label.pack(padx=10, pady=10)

    def on_key_down(self, event):
        """When a key is pressed, add it to the pressed_keys set and send a command."""
        self.pressed_keys.add(event.keysym)
        self.send_command()

    def on_key_up(self, event):
        """When a key is released, remove it from the pressed_keys set and send a command."""
        if event.keysym in self.pressed_keys:
            self.pressed_keys.remove(event.keysym)
        self.send_command()

    def send_command(self):
        """Determine the command based on the pressed keys and send to ESP32."""
        command = self.determine_command()
        if command:
            print(f"Sending command: {command}")
            self.http_request(command)
        else:
            self.http_request("/stop")

    def determine_command(self):
        """
        Map key combinations to commands. 
        - W or Up Arrow => Forward
        - S or Down Arrow => Backward
        - A or Left Arrow => Left
        - D or Right Arrow => Right
        - Combined (W + A, etc.) => diagonal directions
        """
        w = ('w' in self.pressed_keys) or ('Up' in self.pressed_keys)
        s = ('s' in self.pressed_keys) or ('Down' in self.pressed_keys)
        a = ('a' in self.pressed_keys) or ('Left' in self.pressed_keys)
        d = ('d' in self.pressed_keys) or ('Right' in self.pressed_keys)

        if w and a:
            return "/forwardleft"
        elif w and d:
            return "/forwardright"
        elif s and a:
            return "/backleft"
        elif s and d:
            return "/backright"
        elif w:
            return "/forward"
        elif s:
            return "/backward"
        elif a:
            return "/left"
        elif d:
            return "/right"

        return None

    def http_request(self, endpoint):
        """Send an HTTP GET request to the ESP32."""
        try:
            url = ESP32_BASE_URL + endpoint
            response = requests.get(url, timeout=3)
            print(f"Sent {endpoint}, received HTTP {response.status_code}")
        except Exception as e:
            print(f"Error sending {endpoint}: {e}")

def main():
    root = tk.Tk()
    app = RobotController(root)
    root.mainloop()

if __name__ == "__main__":
    main()