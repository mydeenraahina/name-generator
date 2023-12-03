from random import choice
class Namegenerator:
    def __init__(self):
        self.prefix=[]
        self.suffix=[]
    def getting_prefix_suffix_values(self):
        print(f"Name generator...!")
        for value in range(1,6):
            getting_prefix=input(f"Enter prefix_value{value}: ")
            while not getting_prefix.isalpha():
                print(f"Enter a valid input..")
                getting_prefix=input(f"Enter prefix_value{value}: ")
                self.prefix.append(getting_prefix)
            self.prefix.append(getting_prefix)
          
            getting_suffix=input(f"Enter suffix_value{value}: ")
            while not getting_suffix.isalpha():
                print(f"Enter a valid input..")
                getting_suffix=input(f"Enter suffix_value{value}: ")
                self.suffix.append(getting_suffix)
            self.suffix.append(getting_suffix)
                    
    def name_generating(self):
        prefix=choice(self.prefix)
        suffix=choice(self.suffix)
        generated_name=prefix+suffix
        return f"{generated_name}"
def continue_choice():
    obj=Namegenerator()
    obj.getting_prefix_suffix_values()
    print(f"Generated name..")
    for val in range(1,6):
        print(obj.name_generating())
    while True:
        getting_choice=input("Do you want to  continue this funny  name generator..[yes\no]")
        if getting_choice.casefold()=="yes":
            obj=Namegenerator()
            obj.getting_prefix_suffix_values()
            for val in range(1,6):
                print(obj.name_generating())
            break
        elif getting_choice.casefold()=="no":
            print("name generator is going to exit....")
            exit()
        else:
            print("Enter a  valid input")
continue_choice()
                    
                
                
        
