# import socket
#
# link = "localhost"
# port = 65043
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind((link, port))
# sock.listen(True)
#
# print("Сервер работает: ", link, port)
# reverse = ''
# permutation = ''
#
# # print(posts)
# msg = "Its work!"

# return render(request, 'base.html', {'posts': posts})



# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from itertools import chain
import socket
import threading
from os import listdir, path

import httrack
import config
import protocol


def dl_status_checker(thread, connection):
    if thread.isAlive:
        protocol.send(connection, "Downloading has started")
    else:
        protocol.send(connection, "Downloading has FAILED")


def handle_commands(connection, command, string):
    if command == "t1":
        """ flip string """
        string = ' '.join(string)
        new_string = ''
        for s in string[::-1]:
            new_string += s
        protocol.send(connection, new_string)

    elif command == "t2":
        """ replace even characters - odd characters """
        string = ' '.join(string)
        string = list(chain(*(x for x in zip(string[1::2], string[::2]))))
        string = ''.join(string)
        protocol.send(connection, string)

    else:
        protocol.send(connection, command)

    # if command == "dl":
    #     if params[1] == '0':
    #         params[1] = False
    #     else:
    #         params[1] = True
    #     if not params[1] and len(params) == 2:
    #         params.append(None)
    #     htt_thread = threading.Thread(target=httrack.download, args=(params[0], params[1], params[2]))
    #     htt_thread.start()
    #     dl_status = threading.Timer(2.0, dl_status_checker, args=(htt_thread, connection))
    #     dl_status.start()
    # elif command == "list":
    #     file_list = listdir(config.sites_directory)
    #     folder_list = []
    #     archive_list = []
    #     for file in file_list:
    #         if path.isdir(config.sites_directory + '/' + file) and file != "hts-cache":
    #             folder_list.append(file)
    #         if path.isfile(config.sites_directory + '/' + file) and \
    #                 (file[-7:] == ".tar.gz" or file[-8:] == ".tar.bz2" or file[-5:] == ".tar"):
    #             archive_list.append(file)
    #     site_string = ""
    #     folder_found = False
    #     if folder_list:
    #         site_string += "List of folders:\n" + "\n".join(folder_list)
    #         folder_found = True
    #     if archive_list:
    #         if folder_found:
    #             site_string += "\n================================================================================\n"
    #         site_string += "List of archives:\n" + "\n".join(archive_list)
    #     if site_string == "":
    #         site_string = "Sites not found!"
    #     protocol.send(connection, site_string)
    # elif command == "load":
    #     load = ""
    #     for i in range (1, 100000):
    #         load += str(i) + ' '
    #         if i % 1000 == 0:
    #             load += '\n'
    #     protocol.send(connection, load)
    # else:
    #     protocol.send(connection, "Invalid request")


def args_analysis(connection, args):
    args = args.split()
    handle_commands(connection=connection, command=args[0], string=args[1:])


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((config.host, config.port))
sock.listen(True)
while True:
    conn, addr = sock.accept()
    print('Connected by ', addr)
    data = protocol.recv(conn)
    args_analysis(connection=conn, args=data)
