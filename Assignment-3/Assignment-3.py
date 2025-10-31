# Object - Oriented Focus
Phone_Directory = {}

class Phone:
    
    def __init__(self,phone_number,owner_name):
        self.phone_number = phone_number
        self.owner_name = owner_name
        self.contacts = {}
        self.call_history = []
        self.is_calling = False
        self.is_receiving = False
        self.is_in_call = False
        self.current_peer = None
        self.call_start_time = 0
        Phone_Directory[self.phone_number] = self
        print(f"Phone Created for {self.name} ({self.phone_number})")
        
    def add_contact(self,name,phone_number):
        self.contacts[self.phone_number] = self.owner_name
        print("Contact Added Successfully")

    def update_contact(self,phonenumber,new_name):
        if phonenumber in self.contacts:
            self.contacts[phonenumber] = new_name
        else:
            print("Contact Not Exist ")
    
    def delete_contact(self,phonenumber):
        if phonenumber in self.contacts:
            self.contacts.pop(phonenumber)
        else:
            print("Contact Not Exist")

    def search_by_number(self,phonenumber):
        if phonenumber in self.contacts:
            print(self.contacts[phonenumber])
        else:
            print("Contact Not Exist")

    def search_by_name(self,name):
        for key,value in self.contacts.items():
            if value == name:
                print(key)
    
    def wor_to_let(p):
        res = []
        for i in p.split():
            res.append(i)
        return res

    def search_by_keyword(self,query):
        l = wor_to_let(query)
        for key,value in self.contacts.items():
            if l in wor_to_let(key) or l in wor_to_let(value):
                print(key,value)
        else:
            print("Search Not Exist")


    def start_call(self,name,phone_number):
        if phone_number in Phone.register_phone:
            self.call_history.append(phone_number)
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



        
