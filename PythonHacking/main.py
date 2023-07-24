class Pirate(object):
    def __init__(self,email):
        self.email=email


    def sign_in(self):
        print('Logged in')

class Captian(Pirate):
    def __init_(self,name,power,email):
        super().__init__(self,email)
        self.name=name
        self.power=power
        
    def attack(self):
        print(f'You are on a god level now : GEAR 5 baby')

class Swordsman(Pirate):
    def __init_(self,name,power,email):
        self.name=name
        self.power=power
        

captian1 = Captian('Luffy',95,'gamogamonum@gmail.com')
print(captian1.email)
