# -*- coding: cp1251 -*- 
import csv
fileCVS = "data.csv"

target_string = "��'�', '�������', '³�','�������"

def check_string(file_name, target_string):
    with open(file_name, "r", encoding="utf8") as file:
        file_contents = file.read()
        if target_string not in file_contents:
            with open(file_name, 'w', newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(['��\'�', '�������', '³�','�������'])

def userInput():
    name = input("��'� - ")
    pr = input("������� - ")
    vik = (input("³� - "))
    phone = (input("����� �������� - "))
    return [name, pr, vik, phone]

def regim():
    while True:
        print("1 = �������� OR 2 = ��������")
        select = input("������ ����� -> ")
        if select  == '1':
            with open(fileCVS, 'a', newline="", encoding="utf-8") as file:
                check_string(fileCVS, target_string)
                w = csv.writer(file)
                dataUser = userInput()
                w.writerow(dataUser)
            break
        elif select == '2':
            with open(fileCVS, 'r', encoding="utf-8") as file:
                reader = csv.reader(file)
                for i in reader:
                    print(*i)
            break
regim()
