import random
import string

def generate_random_email(min_length=5, max_length=10):
    length = random.randint(min_length, max_length)
    characters = string.ascii_lowercase + string.digits
    username = ''.join(random.choices(characters, k=length))
    return f"{username}@gmail.com"

if __name__ == "__main__":
    for _ in range(1):
        print(generate_random_email())
