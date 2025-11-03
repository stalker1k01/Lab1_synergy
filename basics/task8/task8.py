def is_balanced_number(number):
    stroke_Digit = str(number)
    length = len(stroke_Digit)

    left_sum = 0
    right_sum = 0
    
    if length <= 2:
        return True
    
    if length % 2 == 0:
        mid_start = length // 2 - 1
        mid_end = length // 2 + 1
    else:
        mid_start = length // 2
        mid_end = length // 2 + 1

    left_part = stroke_Digit[:mid_start]
    right_part = stroke_Digit[mid_end:]
    
    for digit in left_part:
        left_sum += int(digit)
    for digit in right_part:
        right_sum += int(digit)
    
    return left_sum == right_sum