from django.shortcuts import render

def basic_calc(request):
    return render(request, 'basic_calculator/basic_calc.html')

def calc_result(request):
    num1 = int(request.POST.get('number1'))
    num2 = int(request.POST.get('number2'))

    if request.POST.get('divide') == "" and num2 == 0:
        result = 'Not Defined'
    elif request.POST.get('add') == "":
        result = num1 + num2
    elif request.POST.get('subtract') == "":
        result = num1 - num2
    elif request.POST.get('multiply') == "":
        result = num1 * num2
    else:
        result = num1 / num2

    return render(request, 'basic_calculator/calc_result.html', {'result': result})