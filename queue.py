# -*- coding: utf-8 -*-
# !/usr/bin/env python3

""" Простой пример с запуском нескольких потоков одновременно: """

import threading
import time


def proc(n, s):
    time.sleep(s)
    print(u'Поток', str(n), u'завершился')


for x in range(1, 4):
    print(u'Поток', str(x), u'стартовал')
    print(u'Количество активных потоков ', threading.activeCount())

    if x == 1:
        threading.Thread(target=proc, args=[x, 3]).start()
    elif x == 2:
        threading.Thread(target=proc, args=[x, 1]).start()
    elif x == 3:
        threading.Thread(target=proc, args=[x, 2]).start()


import sys
from time import sleep
from Queue import Queue
from threading import Thread, enumerate

# Создаем FIFO очередь
q = Queue()


# Функция генерирующая данные для очереди
def source(n):
    for i in xrange(1, 1 + n): yield i


# Функция заполняющая очередь заданиями
def put(n):
    for item in source(n): q.put(item)


def worker():
    while True:
        # Если заданий нет - закончим цикл
        if q.empty(): sys.exit()
        # Получаем задание из очереди
        item = q.get()
        print(u'Очередь: %s выполняется' % item)

        # Сообщаем о выполненном задании
        q.task_done()
        print(u'Очередь: %s завершилась' % item)


# Создаем и запускаем потоки, которые будут обслуживать очередь
for x in range(1, 4):
    print(u'Поток', str(x), u'стартовал')

    put(x)
    Thread(target=worker).start()

    sleep(2)

print('Over')
