# 1. Напишите программу, которая просит пользователя что-нибудь ввести с клавиатуры. Если он вводит какие-нибудь данные, то на экране должно выводиться сообщение "ОК".
# Если он не вводит данные, а просто нажимает Enter, то программа ничего не выводит на экран.
inp_str = input('Input: ')
if len(inp_str) != 0:
    print('OK')
    
    
# Correct
inp_str = input('Input: ')
if inp_str:
    print('OK')
