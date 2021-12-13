import sys

def main():
    while (True):
            print("Hello, what is your name?")
            user_input = input()
            if (user_input == 'x'):
                exit()
            else:
                print(f"nice to meet you, {user_input}, my name is ChatBot")


if __name__ == '__main__':
    main()
    
 