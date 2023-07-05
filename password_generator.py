import os
import secrets
import string
from datetime import datetime

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# 비밀번호 길이 설정
password_length = int(input("생성할 비밀번호 길이를 입력하세요.(정수만): "))

# 비밀번호 생성
password = generate_password(password_length)

# 현재 날짜와 시간 가져오기
current_datetime = datetime.now().strftime("%Y.%m.%d-%H:%M:%S")

# 비밀번호 형식에 맞게 문자열 생성
formatted_password = f"-----{current_datetime}-({password_length}자리)-----\n{password}\n\n"

# 파일명 설정
filename = "password.txt"

# 파일이 이미 존재하는지 확인
file_exists = os.path.exists(filename)

# 비밀번호를 .txt 파일에 저장
with open(filename, 'a') as file:
    if file_exists:
        # 이미 파일이 존재하는 경우, 비밀번호를 추가로 저장
        file.write(formatted_password)
    else:
        # 파일이 존재하지 않는 경우, 새로운 파일을 생성하여 저장
        file.write(formatted_password)
        print(f"{filename} 파일을 생성했습니다.")

print(f"{filename} 비밀번호가 생성되었습니다.")
print(password)

os.system("pause")  # 계속하려면 아무 키나 누르십시오..
