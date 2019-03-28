import logging

from student import Student


def main():
    print("creating student...")
    john = Student("John", 1, 111222333, "212 West Ave", 20, "Computer Science")

    print("Printing John's full details")

    john.printStudentInfo()
    print()
    #Note: The debug message and info message won't be visible on terminal. In order to view them you need to change the configuration.
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('This is a debug message')
    logging.info('This is an info message')

    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')


    a = 5
    b = 0

    try:
        c = a / b
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

if __name__ == "__main__":
    main()
