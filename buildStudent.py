from student import *

def createStudent(name, id, phone, address, age, dept):
    print("Creating student:")
    person = Student(name, id, phone, address, age, dept)
    print("Student named",name,"Created./n")
    return person

def updatePhoneNumber(person, phone):
    print("updating %s's phone number:", person.getName())
    person._setPhone_(phone)
    print(person.getName()+"'s phone number is now", person._getPhone_(),"\n")

def updatePhone(person, number):
    print(person.getName(),"registered with the following phone number: ", person._getPhone_(),"\n")
    updatePhoneNumber(person, number)

def updateAge(person, newAge):
    print("When",person.getName(),"registered, they were", person.getAge(), " years old.")
    person.setAge(newAge)
    print("Now,",person.getName(),"is ", person.getAge(), " years old\n")

def updateDept(person, newDept):
    print(person.getName()+"'s original department was", person.getDepartment())
    person.setDepartment(newDept)
    print(person.getName(),"is now a student in the", person.getDepartment(), "department.\n")

def updateAddress(person, newAddress):
    print(person.getName()+"'s original address was", person.getAddress())
    person.setAddress("121 East Street")
    print(person.getName(),"now lives at ", person.getAddress())

def main():
    #Make new student
    josh = createStudent("Josh", 1, 111222333, "212 West Ave", 20, "Computer Science")
    #Use getName, getId, and getPhone functions from the class
    print(josh.getName(), " has ID number:", josh.getId())

    #Update phone number
    updatePhone(josh, 999888777)

    #Update age
    updateAge(josh, 21)

    #Update department
    updateDept(josh, "Mathematics")

    #Update address
    updateAddress(josh, "121 East Street")

if __name__ == "__main__":
    main()
