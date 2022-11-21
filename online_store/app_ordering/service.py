import random
from django.db.models import Max
from .models import Order
from django.conf import settings
static = settings.STATICFILES_DIRS[0]



def get_number(number:str):
    last_digit = number[-1:]
    if int(last_digit) % 2 == 0 and int(last_digit) != 0:
        result = {'success': True, "error": None}
        return result
    else:
        with open(f'{static}/message_error.txt', 'r', encoding='UTF-8') as file:
            line = file.readlines()
            message = random.choice(line)
        code = random.randint(0, 100)
        result = {'success': False, "error": {'code' : code, 'message': message}}
    return result




def update_order(result, user_id):
    number_order = Order.objects.filter(user_id=user_id).aggregate(Max('number_order'))
    number_order = number_order['number_order__max']
    if result['success']:
        Order.objects.filter(number_order=number_order).update(status=True)
    else:
        text_error = result['error']['message']
        code_error = result['error']['code']
        Order.objects.filter(number_order=number_order).update(text_error=text_error, code_error=code_error)

