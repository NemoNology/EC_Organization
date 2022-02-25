def Is_it_8(number):                                    # Функция проверки корректности ввода

    for i in range(len(number)):                    # Проверяем всё число

        if int(number[i]) > 7:                          # Если находим цифру больше 7

            raise Exception('Inputed invalid argument!')        # Выбрасываем исключение

            break                                                               # Выходим из цикла

        


def from8to10(number):                              # Функция перевода восьмиричного числа в десятичное


    res = 0                                         # Результирующая цеочисленная переменная
    

    for i in range(len(number)):                    # Проходим по всему числу

        res += int(number[i]) * float(pow(8, - i - 1))           # Действуем по формуле перевода

    return res                                      # Возвращаем результат




def from10to16(number):                             # Функция перевода десятичного числа в 16-ное

    
    res = ""                                        # Результирующая строка переменная  
    
    temp = number                                   # Число, с которым работает функия (чтобы не изменять исходное число)
    

    for i in range(5):
        
        res += Getaletter(int(temp * 16))
        
        temp = (temp * 16)
        
        temp -= int(temp)
        
    
    return res                                      # Возвращаем пеервёрнутую строку (По формуле перевода)




def Getaletter(n):                                      # Функция для "перевода" десятичной цифры/числа в 16-ую

    if n < 10:                                          # От 0 до 9 возвращает символы цифр

        return str(n)


    elif n == 10:                                       # От 10 до 15 возвращает оставшиеся символы 16-тиричных цифр

        return "A"

    elif n == 11:

        return "B"

    elif n == 12:

        return "C"

    elif n == 13:

        return "D"

    elif n == 14:

        return "E"

    elif n == 15:

        return "F"

    

        
number = input("Input the number: ")            # Начало программы: ввод числа

number = number.lstrip("0.")                    # Т.к. в целой части нет необходимости, то отметаем её

Is_it_8(number)                                 # Проверяем корректность введёного числа

res = from10to16(from8to10(number))             # Переводим из 8-ного числа в 60-ое


res = "0." + res


print("Result:\t", res)                         # Выводим результат, переведя из 8-ого числа в 16-ое


