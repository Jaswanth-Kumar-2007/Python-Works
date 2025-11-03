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
        print(f"Running add_contact ({number} , {name})....")
        if number in self.contacts:
            print("Error")
        elif number == self.number:
            print("Error")
        else:
            if number in Phone_Directory:
                self.contacts[number] = name
                print("Success")
            else:
                print("Error")
    
    def get_contact_name(self,number):
        return self.contacts,get(number,f"Unknown ({number})")

    def update_contact(self,number,new_name):
        print(f"Running Update_Contact ({number} , {new_name})....")
        if number in self.contacts:
            self.contacts[number] = new_name
            print("Sucess")
        else:
            print("Error")
    
    def delete_contact(self,number):
        print(f"Running delete_contact({number})....")
        if phonenumber in self.contacts:
            self.contacts.pop(number)
            print("Success")
        else:
            print("Error")

    def search_by_number(self,number):
        print(f"Searching by number: {number}....")
        if number in self.contacts:
            print(self.contacts[number])
            print("Found")
        else:
            print("Not Found")

    def search_by_name(self,query):
        l = len(query)
        print(f"Searching by name: {query}....")
        for key,value in self.contacts.items():
            if value[0:l].lower() == query.lower():
                print(key ,"-",value)

# ---- Search By Key Word ---- #
       
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

# ---- Search by Key Word ---- #

    def show_status(self):
        if self.is_calling:
            print(f"Status for {self.name}: Calling")
        elif self.is_in_call:
            print(f"Status for {self.name}: In Call")
        elif self.is_receiving:
            print(f"Status for {self.name}: Incoming Call")
        else:
            print(f"Status for {self.name}: Idle")

    def place_call(self,receiver_number):
        print(f"{self.name} is attempting to call {receiver_number}....")
        if receiver_number in Phone_Directory:
            if self.is_busy:
                self.is_calling = True
        else:
            print("Receiver Number Not Exist")
        
    def receive_call(self,caller_object):
        print(f"{self.name} is receiving a call from {caller_object.name}....")
        self.is_receiving = True
        self.current_peer = caller_object

    def accept_call(self):
        if self.is_receiving:
            self.is_in_call = True
            self.current_peer.is_calling = False
            self.current_peer.is_in_call = True
            self.call_start_time = time.Time()
            self.current_peer.call_start_time = self.call_start_time
            print(f"{self.name} accepted the call")

#------End Call-------#

    def end_call(self):
        print(f"{self.name} is ending the call activity")
        if self.is_calling:
            self.is_calling = False
            self.current_peer.is_receiving = False
            print("Log Dialled (0 Duration) for self,missed for peer")
        elif self.is_receiving:
            self.is_receiving = False
            self.current_peer.is_calling = False
            print("Log missed for self, rejected for peer")
        elif self.is_in_call:
            self.is_in_call = False
            self.current_peer.is_in_call = False
            self.call_end_time = time.Time()
            _add_to_history()
            self.current_peer = None

#-------End Call-------#

    def _add_to_history(self,peer,start_time,end_time,call_type):
        res = {}
        res[peer] = self.caller_object
        res[start_time] = self.call_start_time
        res[end_time] = self.call_end_time
        self.call_history.append(res)



# -------- Testing Case ---------#
if __name__ == "__main__": 
    print("---Interactive Phone Test---")
    alice = Phone("111","Alice")
    bob = Phone("222", "Bob") 

    print("\n---Testing Contacts---")
    alice.add_contact("222","Bobby")
    alice.add_contact("333", "Charlie") 
    alice.add_contact("111", "Me") 
    alice.update_contact("222", "Bob")

    print("\n---Testing Search---")
    alice.search_by_number("222")
    alice.search_by_name("Bo")

    print("\n---Testing Call Scenario---")
    alice.place_call("222")
    alice.show_status()
    

