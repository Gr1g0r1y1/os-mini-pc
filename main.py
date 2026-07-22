import os
import sys
import gc
import machine

VERSION = "1.0.0"
SYSTEM_NAME = "PyMicroOS"

def get_free_space():
    # Расчет свободного места на флеш-памяти
    s = os.statvfs('/')
    return (s[0] * s[3]) / 1024

def shell():
    print(f"=== Добро пожаловать в {SYSTEM_NAME} v{VERSION} ===")
    print("Ввведите 'help' для списка команд.\n")
    
    while True:
        # Строка ввода (приглашение)
        cmd = input(f"{SYSTEM_NAME}:/> ").strip().split()
        if not cmd:
            continue
            
        command = cmd[0].lower()
        args = cmd[1:]
        
        if command == "help":
            print("Доступные команды:")
            print("  ls        - показать файлы")
            print("  cat [f]   - прочитать файл")
            print("  rm [f]    - удалить файл")
            print("  info      - статус системы")
            print("  reboot    - перезагрузка")
            print("  exit      - выход в REPL MicroPython")
            
        elif command == "ls":
            files = os.listdir()
            print("Содержимое диска:")
            for f in files:
                print(f"  {f}")
                
        elif command == "cat":
            if not args:
                print("Ошибка: укажите имя файла.")
                continue
            try:
                with open(args[0], "r") as f:
                    print(f.read())
            except Exception as e:
                print("Ошибка чтения файла:", e)
                
        elif command == "rm":
            if not args:
                print("Ошибка: укажите имя файла.")
                continue
            try:
                os.remove(args[0])
                print(f"Файл {args[0]} удален.")
            except Exception as e:
                print("Ошибка удаления:", e)
                
        elif command == "info":
            print(f"ОС: {SYSTEM_NAME} v{VERSION}")
            print(f"Платформа: {sys.platform}")
            print(f"Свободная ОЗУ: {gc.mem_free()} байт")
            print(f"Свободная флеш-память: {get_free_space():.2f} KB")
            print(f"Частота процессора: {machine.freq() / 1000000} МГц")
            
        elif command == "reboot":
            print("Перезагрузка устройства...")
            machine.reset()
            
        elif command == "exit":
            print("Выход из оболочки ОС.")
            break
            
        else:
            print(f"Команда '{command}' не найдена. Введите 'help'.")

# Запуск оболочки при старте
shell()
