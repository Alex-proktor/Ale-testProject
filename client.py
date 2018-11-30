# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import socket

import config
import protocol


def send():
    print("Выберите режим работы: 1 - простой; 2 - пакетный")
    options = input()

    print(options)

    if options == '1':
        print("ПРОСТОЙ режим работы.")
        string = ''
        while string == '':
            print("Введите строку:")
            string = input()

        command = ''
        while command == '' or command not in ['', '1', '2']:
            print("Выберите команду: 1 - реверс строки; 2 - перестановка четн. и нечетн. символов")
            command = input()

        print("Вы выбрали", command)
        return

    elif options == '2':
        print("ПАКЕТНЫЙ режим работы.")


status = True
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((config.host, config.port))
while True:
    protocol.send(sock, input())
    data = protocol.recv(sock)
    print(data)


    if status == False:
        sock.close()
