suspect_greatest_divisor = 262144 - 1 
        
while suspect_greatest_divisor > 1:
    if 262144 % suspect_greatest_divisor == 0:
        print(suspect_greatest_divisor)
    suspect_greatest_divisor = suspect_greatest_divisor - 1