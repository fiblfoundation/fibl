import random
import string





def code_generator(size=9, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=9):
    new_code = code_generator(size=size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(instance, size=size)
    return new_code

code_list = ['bfi9qljxd',
             't1247g1em',
             'q9p64zaoc',
             'zwscx7h3l',
             'di9i4losn',
             '0f6fvk4fr',
             'djlm6s47j',
             '2e1ygynd9',
             'b5jyg9jga',
             'gf2x718at']


# for x in range(10):
#     x = code_generator(size=9)
#     code_list.append(x)

