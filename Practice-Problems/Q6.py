def sortfirstname(dic):
    dict1 = {}
    sorted_items = sorted(dic.items(),key = lambda x : x[1][0])
    for rollno , (firstname,middlename,lastname) in sorted_items :
        dict1[rollno] = (firstname,middlename,lastname)
    return dict1

students = {
    101: ("Amit", "Kumar", "Sharma"),
    102: ("Ravi", "Prasad", "Reddy"),
    103: ("Kiran", "Mohan", "Das"),
    104: ("Abhishek", "Singh", "Yadav")
}

print(sortfirstname(students))

