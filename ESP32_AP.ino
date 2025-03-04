#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>
#include <ESP32Servo.h>
// Khai báo GPIO cho động cơ DC
int IN1 = 4;
int IN2 = 16;
int IN3 = 5;
int IN4 = 18;

// Khai báo cho servo
Servo myservo, myservo2;

// Biến web server, cổng 80
WebServer server(80);

// Nội dung trang web (HTML) hiển thị các nút điều khiển
String webpage = "";

// ----------------- Các hàm điều khiển động cơ -----------------
void moveForward() {
  // Tiến cả 2 bánh
  analogWrite(IN1, 0);
  analogWrite(IN2, 255);
  analogWrite(IN3, 0);
  analogWrite(IN4, 255);
}

void moveBackward() {
  // Lùi cả 2 bánh
  analogWrite(IN1, 255);
  analogWrite(IN2, 0);
  analogWrite(IN3, 255);
  analogWrite(IN4, 0);
}

void moveLeft() {
  // Quay trái tại chỗ
  analogWrite(IN1, 0);
  analogWrite(IN2, 255);
  analogWrite(IN3, 0);
  analogWrite(IN4, 0);
}

void moveRight() {
  // Quay phải tại chỗ
  analogWrite(IN1, 0);
  analogWrite(IN2, 0);
  analogWrite(IN3, 0);
  analogWrite(IN4, 255);
}

void moveForwardLeft() {
  // Tiến, ưu tiên giảm tốc bên trái
  analogWrite(IN1, 0);
  analogWrite(IN2, 255);   // Right motor full
  analogWrite(IN3, 0);
  analogWrite(IN4, 160);   // Left motor slower
}

void moveForwardRight() {
  // Tiến, ưu tiên giảm tốc bên phải
  analogWrite(IN1, 0);
  analogWrite(IN2, 160);  
  analogWrite(IN3, 0);
  analogWrite(IN4, 255);   // Left motor full
}

void moveBackLeft(){
  // Lùi, ưu tiên giảm tốc bên trái
  analogWrite(IN1, 255);
  analogWrite(IN2, 0);
  analogWrite(IN3, 160);
  analogWrite(IN4, 0);
}

void moveBackRight(){
  // Lùi, ưu tiên giảm tốc bên phải
  analogWrite(IN1, 160);
  analogWrite(IN2, 0);
  analogWrite(IN3, 255);
  analogWrite(IN4, 0);
}

void stopMotor() {
  analogWrite(IN1, 0);
  analogWrite(IN2, 0);
  analogWrite(IN3, 0);
  analogWrite(IN4, 0);
}

// ----------------- Các hàm điều khiển servo -----------------
void servoDown() {
  // Ví dụ: hạ servo góc 60
  myservo.write(60);
}

void servoUp() {
  // Ví dụ: nâng servo góc 120
  myservo.write(120);
}

// ----------------- Hàm xử lý khi client truy cập -----------------
void handleRoot() {
  // Gửi mã HTML
  server.send(200, "text/html", webpage);
}

void handleForward() {
  moveForward();
  server.send(200, "text/html", webpage);
  Serial.println("forward");
}
void handleBackward() {
  moveBackward();
  server.send(200, "text/html", webpage);
  Serial.println("backward");
}
void handleLeft() {
  moveLeft();
  server.send(200, "text/html", webpage);
  Serial.println("left");
}
void handleRight() {
  moveRight();
  server.send(200, "text/html", webpage);
  Serial.println("right");
}

void handleForwardLeft(){
  moveForwardLeft();
  server.send(200, "text/html", webpage);
}
void handleForwardRight(){
  moveForwardRight();
  server.send(200, "text/html", webpage);
}
void handleBackLeft(){
  moveBackLeft();
  server.send(200, "text/html", webpage);
}
void handleBackRight(){
  moveBackRight();
  server.send(200, "text/html", webpage);
}

void handleStop() {
  stopMotor();
  server.send(200, "text/html", webpage);
}

void handleServoDown(){
  servoDown();
  server.send(200, "text/html", webpage);
}
void handleServoUp(){
  servoUp();
  server.send(200, "text/html", webpage);
}

void setup() {
  Serial.begin(115200);

  // Tắt chế độ sleep Wi-Fi để đảm bảo tín hiệu luôn hoạt động
  WiFi.setSleep(false);
  
  // Chuyển về chế độ AP
  WiFi.mode(WIFI_AP);

  // Cấu hình AP với IP tĩnh
  IPAddress local_ip(192, 168, 4, 1);
  IPAddress gateway(192, 168, 4, 1);
  IPAddress subnet(255, 255, 255, 0);
  WiFi.softAPConfig(local_ip, gateway, subnet);

  // Tạo Access Point trên kênh 6, không ẩn SSID, tối đa 4 kết nối
  const char* ap_ssid = "ROBOT_AP";
  const char* ap_pass = "12345678";
  bool apResult = WiFi.softAP(ap_ssid, ap_pass, 6, false, 4);
  if (apResult) {
    Serial.println("AP created successfully");
  } else {
    Serial.println("Failed to create AP");
  }

  // In ra thông tin AP
  Serial.print("Access Point: ");
  Serial.println(ap_ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.softAPIP());

  // Khởi tạo timer cho thư viện ESP32Servo
  ESP32PWM::allocateTimer(0);
  ESP32PWM::allocateTimer(1);
  ESP32PWM::allocateTimer(2);
  ESP32PWM::allocateTimer(3);

  // Gắn servo vào chân (GPIO25 và GPIO26) với tần số 60Hz (có thể điều chỉnh nếu cần)
  myservo.setPeriodHertz(60);  
  myservo.attach(25, 500, 2400);  
  myservo2.setPeriodHertz(60);  
  myservo2.attach(26, 500, 2400);

  // Cấu hình chân động cơ
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  // Tắt động cơ mặc định
  analogWrite(IN1, 0);
  analogWrite(IN2, 0);
  analogWrite(IN3, 0);
  analogWrite(IN4, 0);

  // Tạo nội dung trang web (HTML)
  webpage = "<!DOCTYPE html><html><head><meta charset='utf-8'/>";
  webpage += "<title>ESP32 Robot Control</title></head><body>";
  webpage += "<h2>Điều khiển Robot qua Wi-Fi</h2>";
  webpage += "<p><a href='/forward'><button>Tiến</button></a>";
  webpage += " <a href='/backward'><button>Lùi</button></a>";
  webpage += " <a href='/left'><button>Trái</button></a>";
  webpage += " <a href='/right'><button>Phải</button></a>";
  webpage += " <a href='/stop'><button>Dừng</button></a></p>";
  webpage += "<p><a href='/forwardleft'><button>Tiến Trái</button></a>";
  webpage += " <a href='/forwardright'><button>Tiến Phải</button></a>";
  webpage += " <a href='/backleft'><button>Lùi Trái</button></a>";
  webpage += " <a href='/backright'><button>Lùi Phải</button></a></p>";
  webpage += "<p><a href='/servoClose'><button>Servo Góc Thấp</button></a>";
  webpage += " <a href='/servoOpen'><button>Servo Góc Cao</button></a></p>";
  webpage += "</body></html>";

  // Cấu hình các route của server
  server.on("/", handleRoot);
  server.on("/forward", handleForward);
  server.on("/backward", handleBackward);
  server.on("/left", handleLeft);
  server.on("/right", handleRight);
  server.on("/forwardleft", handleForwardLeft);
  server.on("/forwardright", handleForwardRight);
  server.on("/backleft", handleBackLeft);
  server.on("/backright", handleBackRight);
  server.on("/stop", handleStop);
  server.on("/servoClose", handleServoDown);
  server.on("/servoOpen", handleServoUp);

  server.begin();
  Serial.println("HTTP server started!");
}

void loop() {
  server.handleClient();
}
