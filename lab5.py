def t5_1():
    num = int(input('Введите число'))
    x = [2, 3, 4, 5, 6]
    if num in x:
        print(x, '\n', 'Поздравляю, Вы угадали число!')
    else:
        print(x, '\n', 'Нет такого числа!')

def t5_2():
    ls = [2, 3, 3, 4, 5]
    duplicate = {str(x) for x in ls if ls.count(x) > 1}
    x = lambda : print('nothing')
    y = lambda : print(' '.join(duplicate))
    x() if len(duplicate) < 1 else y()
    
def t5_3():
    week = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
    weekends = int(input('Введите количество выходных'))
    print('Выходные:', *week[:-weekends-1:-1])
    print('Рабочие дни:', *week[:-weekends])

def t5_4():
    import socket
    import random
    from ipaddress import IPv4Network, IPv4Address
    hostname=socket.gethostname()
    myip = IPv4Address(socket.gethostbyname(hostname))
    myip_subnet = IPv4Network(myip)
    numbersName = [int(x) for x in list(filter(str.isdigit, hostname))]
    numbersIP = [int(x) for x in list(filter(str.isdigit, str(myip_subnet)))]
    numbers = list(dict.fromkeys(numbersName + numbersIP))
    MD = ("Петров", "Сидоров", "Ли", "Корсун", "Иванов", "Повалий", "Прокофьев", "Лупкин", "Пупкин", "Кличко")
    DM = ("Емцева", "Антонова", "Андреева", "Зерова", "Осипова", "Хилькевич", "Стиценко", "Федотова", "Краснова", "Копейка")
    while len(numbers) < 10:
        numbers.append(random.randint(0, 9))
        numbers = list(dict.fromkeys(numbers))
    print(numbers)
    MDDM = [MD[x] for x in numbers[:3:]]
    MDDM += [DM[x] for x in numbers[:3:]]
    MDDM = sorted(MDDM)
    print(len(MDDM))
    print(MDDM)
    print("Иванов" in MDDM)
    print(MDDM.count("Иванов"))