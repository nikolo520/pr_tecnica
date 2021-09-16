from django import template

register = template.Library()

@register.filter(name='is_none')
def is_none(value):
    if value is None:
        return ''
    else:
        return value
        
@register.filter(name='total_ventas')
def total_ventas(vendedor_id):
    from apps.venta.models import Venta
    try:

        ventas = Venta.objects.filter(vendedor_id = vendedor_id)
        total = 0
        
        for venta in ventas:
            if venta.valor > 0:
                total += venta.valor
    except Exception as e:
        print(e)
        total = 0
    return total