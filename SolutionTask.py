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