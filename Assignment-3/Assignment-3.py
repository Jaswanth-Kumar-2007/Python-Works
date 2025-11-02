# Object - Oriented Focus
Phone_Directory = {}

import time

class Phone:
    
    def __init__(self,number,name):
        self.number = number
        self.name = name
        self.contacts = {}
        self.call_history = []
        self.is_calling = False
        self.is_receiving = False
        self.is_in_call = False
        self.current_peer = None
        self.call_start_time = 0
        Phone_Directory[self.number] = self
        print(f"Created Phone for {self.name} ({self.number})")

    def is_busy(self):
        return self.is_calling or self.is_receiving or self.is_in_call

    def add_contact(self,number,name):
        if number in self.contacts:
            print("Already Number Exist")
        else:
            self.contacts[number] = name
            print("Contact Added Successfully")
    
    def get_contact_name(self,number):
        print(f"self.contacts[number]")

    def update_contact(self,number,new_name):
        if number in self.contacts:
            self.contacts[number] = new_name
        else:
            print("Contact Not Exist")
    
    def delete_contact(self,number):
        if phonenumber in self.contacts:
            self.contacts.pop(number)
        else:
            print("Contact Not Exist")

    def search_by_number(self,number):
        if number in self.contacts:
            print(self.contacts[number])
        else:
            print("Contact Not Exist")

    def search_by_name(self,query):
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

    def show_status(self):
        if self.is_calling:
            print(f"{self.name} is Started Call")
        elif self.is_in_call:
            print(f"{self.name} is Busy")
        elif self.is_receiving:
            print(f"{self.name} is Receiving Call")

    def place_call(self,receiver_number):
        if receiver_number in Phone_Directory:
            self.is_calling = True
        else:
            print("Receiver Number Not Exist")
        
    def receive_call(self,caller_object):
        if not self.is_busy():
            self.is_receiving = True
            self.current_peer = caller_object
            print(f"{self.name} is Receiving a Call")
        else:
            print(f"{self,name} is in Call")

    def accept_call(self):
        self.is_in_call = True
        print(f"{self.name} is in Call")

    def end_call(self):
        self.is_in_call = False
        print(f"{self.name} is Ended Call")

    def _add_to_history(self,peer,start_time,end_time,call_type):
        pass


"""     
p1 = Phone(7670841203,"KJK",{"MS":9391106103,"SS":9398012291})
p2 = Phone(1234567890,"A",{})

p1.add_contact("KS",9391111456)

p1.display_contact()

p1.start_call("B",1234567890)

p1.display_history()
"""


        
