class Student:
    def __init__(self, name, id, phone, address, age, department):
        self.__name = name
        self.__id = id
        self.__phone = phone
        self.__address = address
        self.__age = age
        self.__department = department

    ##public functions for getting name and id
    def getName(self):
        return self.__name

    def getId(self):
        return self.__id

    ##protected functions for getting and setting address
    def _getAddress_(self):
        return self.__address

    def _setAddress_(self, address):
        self.__address = address

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
        