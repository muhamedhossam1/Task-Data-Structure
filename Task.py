def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"
 
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)

def split_evenly(total, people):
    each = total // people
    remainder = total % people
    return each, remainder

def initials(full_name):
    words = full_name.split()
    result = ""
    i = 0
    while i < len(words):
        result += words[i][0].upper()
        i += 1
    return result

def is_palindrome_word(word):
    cleaned = word.strip().lower()
    return cleaned == cleaned[::-1]

def mask_email(email):
    at_index = email.index("@")
    user = email[:at_index]
    domain = email[at_index:]
    if len(user) <= 2:
        masked_user = user
    else:
        masked_user = user[0] + "*" * (len(user) - 2) + user[-1]
    return masked_user + domain

def middle(values):
    n = len(values)
    start = (n - 1) // 2
    end = (n // 2) + 1
    return values[start:end]

def rotate_left(values, k):
    if len(values) == 0:
        return []
    k = k % len(values)
    return values[k:] + values[:k]

def fib_list(n):
    result = []
    a, b = 0, 1
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps