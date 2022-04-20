#               Обработчик лайков
# 
# http://127.0.0.1:8000/likes?names=
# http://127.0.0.1:8000/likes?names=Андрей235,Жа__@$6SF?,Катя
# http://127.0.0.1:8000/likes?names=АндрейЖаннаКатяМакс 
# http://127.0.0.1:8000/likes?names=Андрей,Жанна,Катя,Макс
# http://127.0.0.1:8000/likes?names=Андрей,Жанна,Катя,Макс,Жанна,Катя,Макс,Жанна,Катя,Макс,Жанна,Катя,Макс,Жанна,Катя,Макс


from flask import Flask, request, render_template

app = Flask(__name__)

def count_likes (arg) -> str:
    if len(arg) == 1:
        str_name = ''.join(arg)
        return str(f'{str_name}' + ' лайкнул(а) это')

    elif len(arg) == 2:
        return str(f'{arg[0]}' + ' и ' + f'{arg[1]}' + ' лайкнули это')

    elif len(arg) == 3:
        return str(f'{arg[0]}' + ', ' + f'{arg[1]}' + ' и ' + 
        f'{arg[2]}' + ' лайкнули это')

    elif len(arg) > 3:
            end = len(arg)
            if end > 6:
                end = 'к'
            else:
                end = 'ка'
            return str(f'{arg[0]}' + ', ' + f'{arg[1]}' + ' и ' + 
            'ещё ' + f'{int(len(arg)-2)}' + ' челове' + f'{end}' + ' лайкнули это')

@app.route('/likes')
def show_user_profile() -> 'html':
    data_names = request.args.get('names', type=str).split(',')
    
    error = bool()
    error_message = str()

    for i in data_names:
        if i.isalpha() and len(i) < 10: 
            error = False
            continue
        elif i == '':
            data_names = str ('Это никому не нравится')
            error = False
            error_message = None
            return render_template('main.html', the_data = data_names,
                                                the_error = error,
                                                the_error_message = error_message,)
        else:
            error = True
            break

    if error == True:
        error_message = ' Your nickname does not meet the standards of nicknames'
        data_names = None
        return render_template('main.html', the_data = data_names,
                                            the_error = error,
                                            the_error_message = error_message,)
        
    else:
        error_message = None
        return render_template('main.html', the_data = count_likes(data_names),
                                            the_error = error,
                                            the_error_message = error_message,)

app.run(port=8000, debug=True)