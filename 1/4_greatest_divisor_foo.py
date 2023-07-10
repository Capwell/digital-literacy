def greatest_divisor(testing_num):
    """Возвращает максимальный делитель числа."""
    suspect_greatest_divisor = testing_num - 1
        
    while suspect_greatest_divisor > 1:
        if testing_num % suspect_greatest_divisor == 0:
            return suspect_greatest_divisor
        suspect_greatest_divisor = suspect_greatest_divisor - 1




print(greatest_divisor(10))
print(greatest_divisor(262144))
# Программа работает неверно. Найдите и исправьте ошибки






