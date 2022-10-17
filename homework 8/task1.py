import re


def car_number(car_id):
    '''
    Функция проверки корректности гос.номера РФ автомобиля
    '''
    validate = re.findall(r'([АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2})(\d{2,3})', car_id)
    if validate:
        print('Номер', car_id, 'валиден. Регион:',validate[0][1])
    else:
        print('Результат: Номер не валиден')

car_number('А222ВС96')

car_number('АБ222ВВ193')

car_number('Б222ВВ193')