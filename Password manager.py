#Author : ShafqatHassan
#Dated : 28th; of Feb 2023
#Repo : Shafqathassan/Cyber-Sec_Tools

#Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key.
from cryptography.fernet import Fernet

class PassswordManager :

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict ={}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        print()(self.key)


    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()


    def create_password_file(self , path, initial_values = None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)
                pass # TODO :add password function



    def load_password_file(self, path):
        self.password_file= path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                seld.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()



    def add_password(seld, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() +"\n")

    def get_password(self, site):
        return self.password_dict[site]




    def  main():
        # Passwords of different accounts like email, facebook, youtube, github etc . 
        password= {
            "email": "1234567",
            "facebook": "myfb",
            "youtube" : "hello",
            "github" : "lessgo"
        }


    pm = PassswordManager()

    print("""
    (1) create a new key
    (2) load an existing psasword
    (3) create a new password file
    (4) Load existing password file
    (5) Add a new password
    (6) Get a password
    (Q) Quit
    """)

    done = False

    while not done:
        choice + input("Input your choice: ")
        if choice =="1" :
            path = input("Enter path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input("Enter path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input("Enter path: ")
            pm.load_password_file(path)
        elif choice == "5":
            site = input("Enter site: ")
            password = input("enter passord: ")
            pm.add_password(site, password)
        elif choice == "Q":
            done = True
            print("Bye")
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
