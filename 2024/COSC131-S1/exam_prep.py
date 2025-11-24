"""exam practice folder"""

GRAVITY = 9.81

def print_times_table(number):
    """dskfbdfvbhuk"""
    x=1
    while x <= 12:
        print(f'{number} x {x} = {number*x}')
        x+=1

def print_fibonacci(f1, f2, num_values):
    """dkfuvyfdvk"""
    num_of_repeats = 1
    total = f1
    print(total)
    total = f2
    while num_of_repeats < num_values:
        print(total)
        total = f1 + f2
        f1 = f2
        f2 = total
        num_of_repeats+=1

def num_left_over(n_disks):
    """dfjfeghfvdhdfvkug"""
    stars = 0
    total = 0
    while total <= n_disks:
        total = 6*stars*(stars-1)+1
        if total == n_disks:
            return n_disks-total
        elif total > n_disks:
            stars-=1
            total = 6*stars*(stars-1)+1
            return n_disks-total
        stars+=1

def get_month():
    """sdjfhbdfvsbhjg"""
    prompt = "Please enter a month (1 - 12): "
    answer = input(prompt)
    while int(answer) < 1 or int(answer) > 12:
        print('Your answer must be in the range 1 - 12')
        answer = input(prompt)
    return int(answer)

def get_multiple_of_7():
    """dsfkjhdsfgbhl"""
    prompt = "Give me a multiple of 7 please: "
    answer = input(prompt)
    while int(answer) % 7 != 0:
        print('Your answer must be a multiple of 7')
        answer = input(prompt)
    return int(answer)

def make_ends(nums):
    """sekrdjhsedfhb"""
    new_list = []
    new_list += [nums[0]]
    new_list += [nums[-1]]
    return new_list

def sum2(nums):
    """dsmfjbdfsghiuvfdku"""
    if len(nums) > 1:
        return nums[0] + nums[1]
    elif len(nums) == 1:
        return nums[0]
    else:
        return 0

def has_same_first_last(nums):
    """sdfkuhsdfh"""
    if len(nums) > 0:
        if nums[0] == nums[-1]:
            return True
        else:
            return False
    else:
        return False

def has_common_end(list_a, list_b):
    """sdjfhvgdsfvbghjjgv"""
    check_1 = len(list_a) > 0 and len(list_b) > 0
    if check_1 == True:
        check_2 = list_a[0] == list_b[0] or list_a[-1] == list_b[-1]
        return check_2
    else:
        return check_1

def has2or3(items):
    """sdfkjdfskbhjkbhj"""
    result = False
    for item in items:
        if item ==2 or item == 3:
            result = True
    return result

def print_evens(numbers):
    """asdfvlsdflvdsfaliuhluiLIGUGUYGIYUGIUYGGYUUIR&^IFRFR"""
    x = 0 
    while x < len(numbers):
        if numbers[x] % 2 == 0:
            print(numbers[x])
        x+=1

def print_in_celsius(fahrenheit_temps):
    """dsfkjhdsfhvj"""
    i = 0
    while i < len(fahrenheit_temps):
        value = (fahrenheit_temps[i]-32)*(5/9)
        print(f'{value:.1f}')
        i+=1

def distances_traveled(height):
    """sdvkusdefkdsvfkujty"""
    times_list = []
    time = 0.5
    travelled_distance = 0
    while travelled_distance < height:
        travelled_distance = 0.5*GRAVITY*(time**2)
        times_list.append(travelled_distance)
        time+=0.5
    return times_list

def tripled_tuple(value):
    """dsfbkhdsf"""
    return (value, value * 3)

def my_product(numbers):
    """dfskjdsfvlhjlhb"""
    result = 1
    for number in numbers:
        result*=number
    return result

def concatenate(strings):
    """sldfkjnfdblhjb"""
    new_string = ""
    for string in strings:
        new_string+=string
    return new_string

def num_bad_days(daily_pm10s):
    """dsfuydfvbhgvyt"""
    result = 0
    for daily_pm10 in daily_pm10s:
        if daily_pm10 > 50:
            result+=1
    return result

def odds(numbers):
    """sdfkjhefrsghiiufyt"""
    return [number for number in numbers if number % 2 == 1]

def alternating_sign_sum(nums):
    """jkhsrgjgsdfhub"""
    i=0 
    answer = 0
    while i < len(nums):
        if i % 2 ==1:
            answer -= nums[i]
        else:
            answer+= nums[i]
        i+=1 
    return answer

def censored(word_list):
    """ksjhdfvvdfbb"""
    new_list = []
    for word in word_list:
        if len(word) == 4:
            new_list.append('****')
        else:
            new_list.append(word)
    return new_list

def squares_and_cubes(data):
    """dsfjvbsjytv"""
    new_list = []
    for number in data:
        if number % 2 == 1:
            new_list.append(number**3)
        else:
            new_list.append(number**2)
    return new_list

def weighted_sum(marks, weights):
    """sdfvikuhdvsfkhkguv"""
    total = 0
    i=0 
    while i < len(marks):
        total+= (marks[i]*weights[i])
        i+=1
    return total

def last_successor(items, target):
    """sldjfvbklhjkgv"""
    result = None
    last_num = None
    for num in items:
        if last_num == target:
            result = num
        last_num=num
    if len(items) > 1:
        if items[-1] == target:
            result = None
    return result

def cumulative_moving_average(data):
    """asdlkjfvdajhblbh"""
    