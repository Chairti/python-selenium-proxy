import random

def random_sex(items):
    return random.choice(items)

if __name__ == "__main__":
    items = ["ชาย", "หญิง", "อื่นๆ"]
    print("ผลไม้ที่สุ่มได้คือ:", random_sex(items))
