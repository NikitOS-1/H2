# # Обработчик лайков
# from flask import Flask
# from flask import request

data = ["Андрей", "Жанна", "Катя", "Макс", "Андрей", 
"Жанна", "Жанна", "Катя", "Макс", "Андрей", "Жанна", 
"Жанна", "Катя", "Макс", "Андрей", "Жанна"]


def name_valid (arg) -> str:
    """
    (Валидация имени пользователя)
    Функция принимает один аргумент (arg) возвращает логическое значение.
    True если каждый символ в строке является буквой и его длина не более 10 символов.
    В противном случае она возвращает логическое значение False.
    """
    if arg.isalpha() and len(arg) < 10:
        return True
    else:
        return False


def count_likes (arg) -> list:
    """
    (Счетчик лайков)
    Функция принимает один аргумент (arg) 
    обрабатывает колличество лаков, возвращает:
    имена или колличество пользователей которые попали (arg)
    """
    if len(arg) == 1:
        str_name = ''.join(arg)
        return print(str(f'{str_name}' + ' лайкнул(а) это.'))

    elif len(arg) == 2:
        return print(str(f'{arg[0]}' + ' и ' + f'{arg[1]}' + ' лайкнули это.'))

    elif len(arg) == 3:
        return print(str(f'{arg[0]}' + ', ' + f'{arg[1]}' + ' и ' + 
        f'{arg[2]}' + ' лайкнули это.'))

    elif len(arg) > 3:
        end = len(arg)
        if end > 6:
            end = 'к'
        else:
            end = 'ка'
        return print(str(f'{arg[0]}' + ', ' + f'{arg[1]}' + ' и ' + 
        'ещё ' + f'{int(len(arg)-2)}' + ' челове' + f'{end}' + ' лайкнули это.'))

    elif len(arg) == 0 :
        return print(str("Это никому не нравится"))

    else:
        return ('Error: your nickname does not meet the standards of nicknames)')


def data_processing_likes (arg) -> list:
    """
    (Обработка лайков)
    """
    for i in arg:
        if name_valid(i):
            return count_likes(arg)
        else:
            return print('Error: your nickname does not meet the standards of nicknames')

data_processing_likes(data)

# app = Flask(__name__)

# @app.route('/likes', methods=['GET'])
# def likes():
#     username = request.args.get('names')
#     print(username)

# app.run(debug=True)
    


# ---------------------------------------------------------------------------------------
# Создать фласк-приложение с одним ендпоинтом - "/likes", 
# которое выдаст соответствующий результат по запросам, т.е.:

# http://127.0.0.1:8000/likes?names=Андрей,Жанна,Катя,Макс --->  

# {
# "error": False,
# "data": "Андрей, Жанна и ещё 2 человека лайкнули это",
# "error_message": None
# }

# http://127.0.0.1:8000/likes?names=Андрей235,Жа__@$6SF?,Катя ---> 

# {
# "error": True,
# "data": None,
# "error_message": "*Текст сообщения об ошибке*"
# }