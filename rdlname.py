import random
import string

def lname(min_length=2, max_length=6):
    length = random.randint(min_length, max_length)
    letters = string.ascii_lowercase
    return ''.join(random.choices(letters, k=length))

if __name__ == "__main__":
    for _ in range(1):
        print("ชื่อที่สุ่มได้:", lname())
