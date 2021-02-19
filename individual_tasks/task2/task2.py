def is_ancestor(person1, person2, family):
    while person2 in family:
        if family[person2] == person1:
            return True
        person2 = family[person2]
    return False
        

file_name = "D:\\My_Progs\\python\\python\\individual_tasks\\task2\\input.txt" 
with open(file_name, 'r') as input_file:
    count = int(input_file.readline())
    family_members = dict()
    for _ in range(count-1):
        person1, person2 = input_file.readline().split()
        family_members[person1] = person2

    for line in input_file:
        person1, person2 = line.split()
        if is_ancestor(person1, person2, family_members):
            print(1)
        elif is_ancestor(person2, person1, family_members):
            print(2)
        else:
            print(0)
