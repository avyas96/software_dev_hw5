class Student:
    def __init__(self, name, id, phone, address, age, department):
        self.__name = name
        self.__id = id
        self.__phone = phone
        self.__address = address
        self.__age = age
        self.__department = department

    ##public functions for getting name, id
    def getName(self):
        return self.__name

    def getId(self):
        return self.__id
    
    ##publicly visible "package" functions for getting and setting student address
    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    ##protected functions for getting and setting phone
    def _getPhone_(self):
        return self.__phone

    def _setPhone_(self, phone):
        self.__phone = phone

    ##public functions for getting and setting age and department
    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def getDepartment(self):
        return self.__department

    def setDepartment(self, department):
        self.__department = department

    ##function that prints student info
    def printStudentInfo(self):
        print("Student name: ", self.__name)
        print("Student id: ", self.__id)
        print("Student phone: ", self.__phone)
        print("Student address: ", self.__address)
        print("Student age: ", self.__age)
        print("Student department: ", self.__department)
        
