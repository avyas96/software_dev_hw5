from student import *


def main():
    print("creating student...")
    josh = Student("Josh", 1, 111222333, "212 West Ave", 20, "Computer Science")
    print("student named ", josh.getName(), " with ID ", josh.getAge())
    print("Josh registered with the following phone number: ", josh._getPhone_())
    print("updating Josh's phone number:")
    josh._setPhone_(999888777)
    print("Josh's phone number is now ", josh._getPhone_())
    print("When Josh registered, he was ", josh.getAge(), " years old.")
    josh.setAge(21)
    print("Now, Josh is ", josh.getAge(), " years old")
    print("Josh's original department was ", josh.getDepartment())
    print("changing Josh's department...")
    josh.setDepartment("Mathematics")
    print("Josh is now a student in the ", josh.getDepartment(), " department.")
    print("setting Josh's address")
    josh.setAddress("121 East Street")
    print("Josh lives on ", josh.getAddress())


if __name__ == "__main__":
    main()
