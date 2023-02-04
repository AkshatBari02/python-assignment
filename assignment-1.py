import random

def main():
    messages = ["today will be a lucky day", "you will meet someone new and interesting", "watch out for obstacles in your path"]
    message = random.choice(messages)
    print(message)

if __name__ == '__main__':
    main()
