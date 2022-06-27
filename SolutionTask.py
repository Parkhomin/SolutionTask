# Task #1

def domain_name(url):
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = url.replace('www.', '')
    return url.split('.')[0]
# Test
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"


# Task #2

import ipaddress

def int32_to_ip(int32):
    return ipaddress.ip_address(int32).__str__()
# Test
assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"


# Task #3

def zeros(n):
    count = 0
    while n > 0:
        n /= 5
        count += int(n)
    return count
# Test
assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7


#Task #4

from itertools import combinations

def bananas(s):
    result = set()
    dingl = 'banana'
    for combination in combinations(enumerate(s), 6):
        word = ['-' for _ in range(len(s))]
        count = 0
        for i, letter in combination:
            if letter == dingl[count]:
                word[i] = letter
                count += 1
            else:
                break
        if count == len(dingl):
            result.add(''.join(word))
    return result
# Test
assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


#Task #5

from functools import reduce

def count_find_num(primesL, limit):
    if reduce(lambda x, y: x * y, primesL) > limit:
        return []
    s = []
    s.append(reduce(lambda x, y: x * y, primesL))
    for i in primesL:
        for element in s:
            element *= i
            while element <= limit and element not in s:
                s.append(element)
                element *= i
    return [len(s), max(s)]

# Test

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []