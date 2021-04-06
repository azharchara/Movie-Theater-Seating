from SeatMangement import SeatMangement
from TestCases import TestCases
import os


def main():
    # Reading input file
    file1 = open("input.txt", "r")
    arr = file1.readlines()

    # Seat allocation
    obj = SeatMangement()
    for i in range(0, len(arr)):
        obj.bookSeat(arr[i])

    # Results display
    dict = obj.getResults()
    tempStr = ""
    for key in dict:
        tempStr = tempStr + key + " " + str(dict[key]) + "\n"

    # writing in output file
    text_file = open("output.txt", "w")
    n = text_file.write(tempStr)
    text_file.close()

    testObject = SeatMangement()
    TestCases(testObject)

    print "---------- SEATS ALLOCATIONS -------------"
    print tempStr

    obj.printLayout()
    obj.analysis()

    # File path of output file
    cwd = os.getcwd()
    print "-------- Output File path -------------"
    print cwd + "/output.txt"


if __name__ == "__main__":
    main()
