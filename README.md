# Trước khi cài đặt
*Máy tính cần cài đặt trước git(nếu muốn sử dụng trên terminal)*

Link hướng dẫn tải: https://phoenixnap.com/kb/how-to-install-git-windows
- Clone bản repo này về với lệnh trên terminal:

```
git clone https://github.com/PXDAT/DOSON-EBOT.git
```
hoặc đơn giản hơn là:

![Screenshot 2025-03-02 210352](https://github.com/user-attachments/assets/e8f949ed-ef49-41d5-8625-1de2056d6239)

sau khi tải về các bạn có thể giải nén và truy cập thư mục vừa giải nén.
# Hướng dẫn chi tiết cài đặt
- Hướng dẫn cài đặt và setup EBOT với Arduino IDE: https://github.com/sam-espiol/EBOT-setup-with-Arduino-IDE/blob/main/EBOT-setup-with-Arduino-IDE.md
- Hướng dẫn cài đặt và setup EBOT với platformio: https://github.com/sam-espiol/EBOT-setup-with-platformio/blob/main/EBOT-setup-with-platformio.md

# Điều khiển thông qua Desktop: 
*Đảm bảo rằng máy tính của các bạn đã cài đặt ngôn ngữ python.*

Link hướng dẫn tải python: https://www.digitalocean.com/community/tutorials/install-python-windows-10
- Cần cài đật tất cả các thư viện cần thiết với lệnh
```
pip install -r requirement.txt
```
- Với những bạn đang mở folder được giải nén chọn **Open in Terminal**
![Screenshot 2025-03-02 213002](https://github.com/user-attachments/assets/57e3df6a-ff04-41de-be78-9aa73cc90d51)
- Và nhập lệnh sau: 
```
python ESP32_Dekstop_Application.py
```
- Với những bạn đang ở trong sẵn terminal sau khi vừa nhập lệnh **git clone** thì ta chỉ cần chuyển tới vùng folder vừa giải nén bằng lệnh:
```
cd DOSON-EBOT-main
```
- Cuối cùng nhập lệnh này để hoàn tất việc chạy chương trình điều khiển Desktop:
```
python ESP32_Dekstop_Application.py
```
# Điều khiển thông qua Mobile:
## Lưu ý trước khi thực hiện
**Để dễ dàng cài đặt hệ điều hành của bạn cần chạy windows 10/11 phiên bản pro hoặc linux với distro thuộc nhánh Debian(Ubuntu, Linux Mint, Lubuntu, v.v)*

**Với các máy chạy hệ điều hành Windows cần cài đặt trước WSL2 (recommend) để dễ dàng giả lập hoặc có thể tải những phần mềm máy ảo như Virtual Box hoặc VMware Workstation Player hoặc VMware Workstation Pro để có thể dễ dàng hơn trong quá trình chỉnh sửa phần mềm. Tuy nhiên để cho đơn giản thì đây chỉ là hướng dẫn sử dụng với WSL2*

Link tải WSL2: https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10

Link tải Ubuntu24-04 trên WSL2: https://documentation.ubuntu.com/wsl/en/latest/howto/install-ubuntu-wsl2/

**Phần mềm chỉ chạy trên những thiết bị sử dụng hệ điều hành android 5 trở lên và bật chế độ nhà phát triển cùng với chế độ File transfer*

*(Vì mỗi máy sẽ có cài đặt riêng nên hướng dẫn sau đây chỉ mang tính tham khảo, bạn có thể tra bằng cách gõ từ khóa "developer mode/ File transfer + <tên thiết bị các bạn đang sử dụng>")*

Link hướng dẫn bật developer mode: https://www.youtube.com/watch?v=vYsLR1U_j5c

Link hướng dẫn để chế độ File transfer: https://www.youtube.com/watch?v=yKGlRduZ_sk

**Đây chỉ là hướng dẫn cho những bạn muốn tự tinh chỉnh phần mềm theo sở thích, ý muốn cá nhân còn ai không muốn có thể tải và sử dụng luôn phần mềm điều khiển Ebot*

Link tải phần mềm: https://drive.google.com/drive/folders/1S_5SukDUP2q2geEFwnhd3IsIMWXxMDIf?usp=sharing

## Chi tiết cài đặt
- Sau khi cài đặt xong WSL2 và Ubuntu ta vào mục Linux > Ubuntu-24.04 > home > ubuntu > paste file DOSON-EBOT-main.zip vừa tải về trong phân vùng này

![Screenshot 2025-03-04 093442](https://github.com/user-attachments/assets/aeed77ee-5380-4af3-aa6c-41583589295e)

- Tiếp theo giải nén và mở Ubuntu-24.04

![Screenshot 2025-03-04 093802](https://github.com/user-attachments/assets/21b40bb6-ac30-49bb-88b3-1df9c002c4ae)

- Nhập lệnh sau để truy cập vào thư mục vừa được giải nén

```
cd DOSON-EBOT-main
```

- Cài đặt pip trên linux

```
sudo apt-get install python3-pip
```
![Screenshot 2025-03-04 094129](https://github.com/user-attachments/assets/0cc0993b-21cc-4272-85f7-819052d43f00)

- Tải môi trường ảo

```
sudo apt-get install python3.12-venv
```
![image](https://github.com/user-attachments/assets/89f75b4a-175d-4d28-80ff-b47116f79b26)

- Cấp quyền truy cập root cho folder application và chuyển đến application

```
sudo chmod -R 777 application && cd application
```

- Cài đặt môi trường ảo và truy cập vào môi trường ảo

```
sudo python3 -m venv .venv && source .venv/bin/activate
```

- Cấp quyền truy cập root cho môi trường ảo

```
sudo chmod -R 777 .venv
```

- Tải buildozer

```
pip install --upgrade buildozer
```

![image](https://github.com/user-attachments/assets/3cb7eba7-8e14-4dfb-87a7-b60793043d4f)

- Cập nhật lại những package vừa cài đặt

```
sudo apt update
```

- Tải và cài đặt package libtinfo5

```
wget http://security.ubuntu.com/ubuntu/pool/universe/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
```

![image](https://github.com/user-attachments/assets/85d4e552-656e-4a3c-8875-07e2b2664325)

```
sudo apt install ./libtinfo5_6.3-2ubuntu0.1_amd64.deb
```

![image](https://github.com/user-attachments/assets/64e8cae7-5c08-4061-a966-1506579796fb)

- Tải và cài đặt những công cụ và package cần thiết trong quá trình biên dịch application

```
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

![image](https://github.com/user-attachments/assets/4f42558d-5e23-4a56-8653-2a572dca019b)

- Tiếp theo tải trình biên dịch Cython

```
pip install --upgrade Cython==0.29.33 virtualenv
```

![image](https://github.com/user-attachments/assets/935f07cf-1dc4-402e-b07e-eae847480a62)

- Tiếp theo config sâu trong hệ thống

```
export PATH=$PATH:~/.local/bin/
```

- Sau khi chạy trực tiếp trên terminal mở file .bashrc để config cho những lần sau sử dụng được tự động

```
vi ~/.bashrc
```

bấm tổ hợp phím ESC + Shift + G và paste lệnh này vào dòng trống cuối cùng của file 

```
export PATH=$PATH:~/.local/bin/
```

![Screenshot 2025-03-04 095828](https://github.com/user-attachments/assets/0ec4304f-7a1a-4ffe-bd85-c3bff128bd54)

sau khi paste xong bấm ESC gõ ':wq' + bấm Enter để lưu và thoát 

![Screenshot 2025-03-04 100023](https://github.com/user-attachments/assets/641a8345-e4bf-4cc5-88f6-40322a68393e)

- Tiếp theo ta cần tải automake bằng lệnh:

```
sudo apt install - y automake 
```

- Tiếp theo cần lưu lại địa chỉ mà hệ thống tải những phần mềm và package về máy

```
sudo vi /etc/apt/sources.list
```

paste đoạn mã sau:

```
deb http://archive.ubuntu.com/ubuntu noble universe main
```

![Screenshot 2025-03-04 100549](https://github.com/user-attachments/assets/fce07ce4-e74d-4ca5-bbb3-a0cc553eedb7)

bấm ESC + gõ lệnh ':wq' + bấm Enter để lưu và thoát
- Sau đó cập nhật lại những thay đổi vừa rồi

```
sudo apt update
```

- Tiếp theo để ổn định trong quá trình debug và deploy ứng dụng nhập đoạn lệnh sau:

```
pip install setuptools
```
![image](https://github.com/user-attachments/assets/b99dd29f-501c-4dd3-81ef-0503fb2b6b71)

- Tiếp theo tải công cụ adb trên laptop windows:
link tải adb: [platform-tools-latest-windows.zip](https://github.com/user-attachments/files/19063548/platform-tools-latest-windows.zip)

sau khi tải xong và giải nén ra folder platform-tools, chuyển folder này vào chính ổ C:

![Screenshot 2025-03-04 101942](https://github.com/user-attachments/assets/d16a4fe0-2919-490a-8286-d652e05e66af)

- Tiếp theo kết nối điện thoại vào máy tính (dây kết nối cần có khả năng truyền dữ liệu) mở CMD trên máy tính windows và nhập lệnh
```
cd C:\platform-tools && adb devices
```
![image](https://github.com/user-attachments/assets/fc60cf84-8c5a-4af2-9c35-43a946bb5beb)

- Quay trở lại với Ubuntu-24.04 tải adb bằng lệnh:

```
sudo apt install adb 
```
![image](https://github.com/user-attachments/assets/34117196-80a8-4c77-b990-05aa66c92b37)

- Vào cài đặt điện thoại tìm kiếm địa chỉ IP
( ví dụ cho máy của mình )

![Screenshot_2025-03-04-10-31-29-95_fc704e6b13c4fb26bf5e411f75da84f2](https://github.com/user-attachments/assets/4cc88297-839a-40b7-9001-a6ddfdf4b3bf)

- Quay trở lại với Ubuntu-24.04 và nhập lệnh để kết nối

*Thay đổi địa chỉ IP mà máy bạn đang có như mình ở đây IP của máy đang là: 192.168.7.32*

```
adb connect 192.168.7.32 
```
sau khi kết nối thành công

![image](https://github.com/user-attachments/assets/1ed78781-d191-4f41-8ef2-f0aba261b520)

- Cuối cùng bạn chỉ cần nhập lệnh để có thể cài đặt ứng dụng là xong

```
buildozer android debug deploy run
```

## <ins> LƯU Ý </ins>
- Mỗi lần chạy lệnh cuối cùng, cần xóa app vừa nạp từ máy tính trên điện thoại trước khi chạy để tránh trường hợp ghi đè bộ nhớ dẫn đến xung đột
- Sau khi mỗi lần chạy xong cần chạy lệnh để xóa sạch những file cài đặt được sinh ra để lần sau cài đặt lại không bị gặp lỗi ghi đè file

```
buildozer android clean
```
sau khi nhập lệnh trên thì chỉ cần bắt đầu lại từ bước kết nối với máy điện thoại qua IP cho đến lệnh cuối cùng là xong
