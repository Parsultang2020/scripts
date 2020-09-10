#!/usr/bin/env python3

import subprocess  # импортируем модуль subprocess
import optparse  # импортируем модуль optparse


def get_arguments():  # получить аргумент
    parser = optparse.OptionParser()  # OptionParser - класс модуля optparser
    parser.add_option("-i", "--interface", dest="interface", help="Интерфейс для изменения МАС адреса")
    parser.add_option("-m", "--mac", dest="new_mac", help="Новый МАС адрес")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Укажите интерфейс. Для получения информации используйте --help")
    elif not options.new_mac:
        parser.error("Укажите МАС адрес. Для получения информации используйте --help")
    return options


def change_mac(interface, new_mac):
    print("Меням МАС адрес для " + interface + " на " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
