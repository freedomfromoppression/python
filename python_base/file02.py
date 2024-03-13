#시작경로, 찾을 파일명을 입력받아
#찾으면 input 으로 맞는지 (y/n)을 입력받아 전체경로를
#출력하는 함수를 만드시오!.
# def fn_serch(dir, file_nm):
#     print(dir, file_nm)
# root, nm = input("찾을 시작경로, 파일명을 입력하세요:").split()
# fn_serch(root, nm)

import os
def find_files(start_path, file_name):
    file_paths = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file == file_name:
                file_paths.append(os.path.join(root, file))

    if file_paths:
        for path in file_paths:
            print(path)
        answer = input("찾은 파일이 맞습니까? (y/n): ")
        if answer.lower() == "y":
            pass
        else:
            print("파일이 맞지 않습니다.")
    else:
        print("일치하는 파일이 없습니다.")

start_path = input("시작 경로를 입력하세요: ")
file_name = input("찾을 파일명을 입력하세요: ")

find_files(start_path, file_name)