from django import template

register = template.Library()

@register.filter(name='is_none')
def is_none(value):
    if value is None:
        return ''
    else:
        return value
        
@register.filter(name='calcular_edad')
def calcular_edad(fecha_nacimiento):
    from datetime import date
    hoy = date.today()
    try:
        edad = hoy.year - fecha_nacimiento.year
        return edad
    except Exception as e:
        print("[Error]",e)
        return ''

@register.filter(name='alert')
def alert(fecha_nacimiento):
    edad = calcular_edad(fecha_nacimiento)
    print(edad)
    if edad != '':
        if edad < 18 :
            return 'menor'
        if edad > 50 :
            return 'mayor'
    return ' nada'