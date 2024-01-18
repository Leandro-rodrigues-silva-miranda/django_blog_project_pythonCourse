from random import SystemRandom
import string
from django.utils.text import slugify

def randomize_letter(k=5):

    return ''.join(SystemRandom().choices(
        string.ascii_letters + string.digits,k=k
    ))

def new_slugified(text,k=5):
    return slugify(text) + '-' +  randomize_letter(k)
