from student import *


def main():
    print("creating student...")
    josh = Student("Josh", 1)
    print("student named ", josh.getName(), " with ID ", josh.getAge())
    print("setting Josh's phone number:")
    josh._setPhone_(999888777)
    print("Josh's phone number is ", josh._getPhone_())
    print("setting Josh's age:")
    josh.setAge(21)
    print("Josh is ", josh.getAge(), " years old")
    print("setting Josh's department:")
    josh.setDepartment("Mathematics")
    print("Josh is a student in the ", josh.getDepartment(), " department.")
    print("setting Josh's address")
    josh.setAddress("121 East Street")
    print("Josh lives on ", josh.getAddress())

if __name__ == "__main__":
    main()