import time,random


class Instagrame:
    text = "-----WELCOME TO KILLER RED------\n[1]Instagram password crack\n[*]EXIT\n"
    for charactar in text:
        print(charactar, end="", flush=True)
        time.sleep(0.1)
        
    def __init__(self, username):
        self.username = username

    @property
    def usernameREADING(self):
        return self.username
    
    



while True:
    opstione = input('Enter a Opstione : ').strip()
    
    if opstione in ['1',"instagram password crack"]:
        
        enter_userName = input('Instagram User Name : ')#username datails
        instagram = Instagrame(enter_userName)
        text = f"Chack {instagram.usernameREADING}....\n"
        for char in text:
            print(char , end="",flush=True)
            time.sleep(0.1)
        time.sleep(2)
        
        text2 = 'user Name Successfull Found \n'
        
        for cha in text2:
            print(cha , end="",flush=True)
            time.sleep(0.1)

        correct_password = 5522556655885544

        while True:
            password_generatar = random.randint(5522556655880000, 9999999999999999)
            print(password_generatar)
            if password_generatar == correct_password:
                print("Password Found!")

                see = input("See number? (Y/N): ").strip().lower()
                if see in ["y", "yes"]:
                    print(f"""
+----------------------------------+
| Number : {password_generatar}    |
+----------------------------------+
""")
                else:
                    print("Thanks!")
                    break
                
                

    
    elif opstione in ['*','exit']:
        print('Exit...')
        time.sleep(1)
        break

    else:
        print("invalid choise")
        continue


        
        