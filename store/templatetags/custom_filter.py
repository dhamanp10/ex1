from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)



@register.filter(name='multiply')
def price_total(number1,number2):
    return number1 * number2

