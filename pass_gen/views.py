from django.shortcuts import render
import random
import string

ALPHABETS = string.ascii_uppercase
alphabets = string.ascii_lowercase
Numbers = '0123456789'
SpecialCharacters = '~!@#$%&*+()-_=[]{}\/:;?.,"'
final_list = ALPHABETS+alphabets+Numbers+SpecialCharacters


def pass_gen(request):
    return render(request, 'pass_gen/pass_gen.html')


def password(request):
    Length = int(request.POST.get('length'))
    num1 = random.choice(alphabets)
    num2 = random.choice(ALPHABETS)
    num3 = random.choice(Numbers)
    num4 = random.choice(SpecialCharacters)
    password1 = [num1, num2, num3, num4]
    random.shuffle(password1)
    for i in range(Length-4):
        password1.append(random.choice(final_list))

    return render(request, 'pass_gen/password.html', {'password1': ''.join(password1)})
