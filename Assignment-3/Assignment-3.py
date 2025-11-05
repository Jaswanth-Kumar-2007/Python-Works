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
        self.call_end_time = 0
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
        if number in Phone_Directory:
            return Phone_Directory[number].name
        else:
            return f"Unknown {number}"

    def update_contact(self,number,new_name):
        print(f"Running Update_Contact ({number} , {new_name})....")
        if number in self.contacts:
            self.contacts[number] = new_name
            print("Success")
        else:
            print("Error")
    
    def delete_contact(self,number):
        print(f"Running delete_contact({number})....")
        if number in self.contacts:
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

    def search_by_keyword(self, query):
        print(f"Searching by keyword: {query}...")
        tokens = query.lower().split()
        found = False
        for number, name in self.contacts.items():
            name_lower = name.lower()
            if all(token in name_lower for token in tokens) or any(token in number for token in tokens):
                print(f"{number} - {name}")
                found = True
        if not found:
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

    def place_call(self,receiver_number,timestamp):
        timestamp = int(timestamp)
        print(f"{self.name} is attempting to call {receiver_number}....")
        if receiver_number in Phone_Directory:
            receiver = Phone_Directory[receiver_number]
            if not self.is_busy() or not receiver.is_busy:
                self.call_start_time = timestamp
                self.is_calling = True
                self.current_peer = receiver
                receiver.receive_call(self)
                Phone_Directory[receiver_number].is_receiving = True
            else:
                print("Error")
        else:
            print("Receiver Number Not Exist")
        
    def receive_call(self,caller_object):
        print(f"{self.name} is receiving a call from {caller_object.name}....")
        self.is_receiving = True
        self.current_peer = caller_object

    def accept_call(self,timestamp):
        if self.is_receiving:
            if self.current_peer.is_calling:
                self.is_calling = False
                self.is_in_call = True
                self.is_receiving = False
                self.current_peer.is_calling = False
                self.current_peer.is_in_call = True
                self.call_start_time = timestamp
                self.current_peer.call_start_time = self.call_start_time
                print(f"{self.name} accepted the call")

#------End Call-------#

    def end_call(self,timestamp):
        timestamp = int(timestamp)
        self.call_end_time = timestamp
        self.current_peer.call_end_time = timestamp
        print(f"{self.name} is ending the call activity\n")
        if self.is_calling:
            self.is_calling = False
            self._add_to_history(self.current_peer,self.call_start_time,self.call_start_time,"Dialled")
            self.current_peer._add_to_history(self,self.call_start_time,self.call_start_time,"Missed")
        elif self.is_receiving:
            self.is_receiving = False
            self._add_to_history(self.current_peer,self.call_start_time,self.call_start_time,"Missed")
            self.current_peer._add_to_history(self,self.call_start_time,self.call_start_time,"Rejected")
        elif self.is_in_call:
            if self.current_peer.is_receiving:
                call_type_self = "Dialled"
                call_type_peer = "Received"
            else:
                call_type_self = "Received"
                call_type_peer = "Dialled"
            self.current_peer._add_to_history(self,self.call_start_time,self.call_end_time,call_type_self)
            self._add_to_history(self.current_peer,self.call_start_time,self.call_end_time,call_type_peer)
            self.is_in_call = False
            self.current_peer.is_in_call = False

#-------End Call-------#

    def _add_to_history(self,peer,start_time,end_time,call_type):
        res = {}
        peer_name = self.get_contact_name(peer.number)
        res["Name"] = peer_name
        t = self.call_end_time - self.call_start_time
        res["Call Duration"] = f"{abs(int(t))}"
        res["Number"] = peer.number
        res["Call Type"] = call_type
        self.call_history.append(res)

    def print_analysis(self):
        print(f"\n---Call Analysis for {self.name} {self.number} ---")
        #Unique Calls Made
        print("Unique Calls Made:....")
        set1 = set()
        for i in self.call_history:
            for key,value in i.items():
                if i["Call Type"] == "Dialled":
                    set1.add(i["Name"])
        print(len(set1))
        #Average Call Duration
        print("Average Call Duration:....")
        list1 = []
        for i in self.call_history:
            for key,value in i.items():
                if i["Call Type"] in ["Dialled","Received"] and int(i["Call Duration"])>0:
                    list1.append(int(i["Call Duration"]))
        if len(list1) != 0:
            print(sum(list1)/len(list1))
        #Most Frequently Called Numbers
        print("Most Frequently Called Number(s):....")
        dict1 = {}
        for i in self.call_history:
            if i["Call Type"] == "Dialled":
                if i["Name"] in dict1:
                    dict1[i["Name"]] += 1
                else:
                    dict1[i["Name"]] = 1
        if dict1:
            s = max(dict1.values())
            for i,j in dict1.items():
                if j == s:
                    print(i)
        else:
            print("No Dialled Numbers")

def run_simulation(filename):
    print("----Starting Phone Simulation ---")

    with open(filename,'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            command = parts[0]
            try:
                if command == "CREATE_PHONE":
                    if parts[1] not in Phone_Directory:
                        parts[1] = Phone(parts[2],parts[1])   
                elif command == "ADD_CONTACT":
                    Phone_Directory[parts[1]].add_contact(parts[3],parts[2])

                elif command == "CALL":
                    Phone_Directory[parts[1]].place_call(parts[2],parts[3])

                elif command == "ACCEPT":
                    Phone_Directory[parts[1]].accept_call(int(parts[2]))
                
                elif command == "END":
                    Phone_Directory[parts[1]].end_call(int(parts[2]))
            
            except Exception as e:
                print(f"ERROR processing line '{line}': {e}")
            
    print("\n----Simulation Finished ---")

    for phone in Phone_Directory.values():
        phone.print_analysis()

run_simulation("C:\Projects\JK Projects\Python-Works\Python-Works\Assignment-3\commands.txt")

"""  
# -------- Testing Case ---------#
if __name__ == "__main__": 
    print("---Interactive Phone Test---")
    alice = Phone("111","Alice")
    bob = Phone("222", "Bob") 

    print("\n---Testing Contacts---")
    alice.add_contact("222","Bobby")
    alice.add_contact("333", "Charlie") 
    alice.add_contact("111", "Me") 
    alice.update_contact("222", "bob")

    print("\n---Testing Search---")
    alice.search_by_number("222")
    alice.search_by_name("bo")

    print("\n---Testing Call Scenario---")
    alice.place_call("222",0)
    alice.show_status()
    bob.show_status()
    bob.accept_call(2)
    alice.show_status()
    bob.show_status()
    print(".....simulating a 2-second call...")

    time.sleep(2)

    alice.end_call(12)

    alice.show_status()
    bob.show_status()
     
    print("\n----Final Call History ----")
    print(f"Alice's History : {alice.call_history}")
    print(f"Bob's History: {bob.call_history}")
    alice.print_analysis()
    bob.print_analysis()
"""




