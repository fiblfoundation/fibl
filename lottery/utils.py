import random
import string
from celery.schedules import crontab
from celery.task import periodic_task



def code_generator(size=9, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=9):
    new_code = code_generator(size=size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(instance, size=size)
    return new_code


code_list = []
for x in range(10):
    x = code_generator(size=9)
    code_list.append(x)

