def sortfirstname(dic):
    dict1 = {}
    sorted_items = sorted(dic.items(),key = lambda x : x[1][0])
    for rollno , (firstname,middlename,lastname) in sorted_items :
        print(f"Roll No. - {rollno} , {(firstname,middlename,lastname)}")

students = {
    101: ("Amit", "Kumar", "Aharma"),
    102: ("Ravi", "Prasad", "Reddy"),
    103: ("Kiran", "Mohan", "Das"),
    104: ("Abhishek", "Singh", "Yadav")
}

sortfirstname(students)
