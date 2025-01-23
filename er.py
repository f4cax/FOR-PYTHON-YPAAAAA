import random

connection = random.random() < 0.6

if connection:
    while connection:
        email = input("Пожалуйста, введите ваш email: ")
        
        if '.' in email and '@' in email:
            print("Спасибо! Ваш email успешно записан.")
            connection = False
        else:
            print("Введенный адрес недействителен. Адрес должен содержать символы '.' и '@'")
            print("Пожалуйста, попробуйте еще раз.")
else:
    print("Нет соединения с сервером. Попробуйте позже.")