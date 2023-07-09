human_data_1 = {
    'first_name' : 'steve',
    'last_name' : 'smith',
    'email' : 'steve@smith.com',
    'age' : 29
}

human_data_2 = {
    'first_name' : 'bob',
    'last_name' : 'Jones',
    'email' : 'bob@Jones.com',
    'age' : 32
}

human_data_3 = {
    'first_name' : 'billy',
    'last_name' : 'bob',
    'email' : 'billy@bob.com',
    'age' : 40
}


class User:
    is_rewards_member = False
    gold_card_points = 0
    def __init__(self, human_data):
        self.first_name = human_data['first_name']
        self.last_name = human_data['last_name']
        self.email = human_data['email']
        self.age = human_data['age']

    def display_info(self):
        print(f"User's first name is: {self.first_name}")
        print(f"User's last name is: {self.last_name}")
        print(f"User's email is: {self.email}")
        print(f"User's age is: {self.age}")
        if self.is_rewards_member == True:
            print("User is a rewards member")
            print(f"User has {self.gold_card_points} Gold Card Points.")
        else:
            print("User is not a rewards member")

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self

    def spend_points(self, amount):
        if self.is_rewards_member == False:
            print(f"Sorry, {self.first_name} is not a rewards member.")
        else:
            if amount > self.gold_card_points:
                print(f"Insufficient balance, sorry, the user only has {self.gold_card_points} Gold Card Points.")
                return False
            else:
                self.gold_card_points = self.gold_card_points - amount
                return self

    def __repr__(self):
        return f"Human Object. First name {self.first_name}, last name {self.last_name}, email {self.email}, age {self.age}, points {self.gold_card_points}."


human1 = User(human_data_1)
human2 = User(human_data_2)
human3 = User(human_data_3)

human1.enroll().spend_points(50)
human2.enroll().spend_points(80)
human3.spend_points(40)

human1.display_info()
human2.display_info()
human3.display_info()
