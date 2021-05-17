from django import template
import os

register = template.Library()


@register.filter(name='censor')
def censor(value):
    dir = os.path.dirname(r"C:\Users\hp\Desktop\python\censordata.txt")
    file_path = os.path.join(dir, 'censordata.txt')
    file = open(file_path, 'r', encoding='ansi').read()
    censor_list = file.split(', ')
    title = value.split()
    new_t = map(lambda x: x if x not in censor_list else '...', title)
    return ' '.join(new_t)
