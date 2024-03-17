import os

if __name__ == "__main__":
    print("Welcome to Robo Speaker 1.1. Created by Aditya")
    while(True):
        x = input("Enter what you want to speak ")
        if x == "quit":
            os.system("say 'bye bye friend")
            break
        command = f"say {x}"
        os.system(command)