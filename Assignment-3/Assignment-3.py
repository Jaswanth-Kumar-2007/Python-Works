# Object - Oriented Focus

class Phone:
    register_phone = []
    
    def __init__(self,phone_number,owner_name,contacts):
        self.phone_number = phone_number
        self.owner_name = owner_name
        self.contacts = contacts
        self.call_history = {}
        Phone.register_phone.append(phone_number)
        
    def add_contact(self,name,phone_number):
        self.contacts[name] = phone_number
        print("Contact Added Successfully")
        
    def start_call(self,name,phone_number):
        if phone_number in Phone.register_phone:
            self.call_history[name] = phone_number
            print("Call Started Successfully")
        else:
            print("Phone Number is Not Registered")
        
    def display_contact(self):
        print(f"{self.contacts}")
        
    def display_history(self):
        print(f"{self.call_history}")
        

p1 = Phone(7670841203,"KJK",{"MS":9391106103,"SS":9398012291})
p2 = Phone(1234567890,"A",{})

p1.add_contact("KS",9391111456)

p1.display_contact()

p1.start_call("B",1234567890)

p1.display_history()



        
