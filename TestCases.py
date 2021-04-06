from SeatMangement import SeatMangement


class TestCases(object):

    def __init__(self, movieTheaterIn):
        self.testTheater = SeatMangement()
        self.testMe(movieTheaterIn)

    def testMe(self, movieTheaterIn):
        print "--------- TEST CASES ------------"
        self.testTheater = movieTheaterIn
        self.checkReservationWithZeroTickets()
        self.checkFirstCustomerSeat()
        self.checkConsecutiveSeats()
        self.checkInsufficientSeats()
        self.checkGroupUnableToAccomodateInRow()
        self.checkGroupAccomodationOfSizeLargerSize()

    def checkReservationWithZeroTickets(self):
        if self.testTheater.bookSeat("R001 0") == 1:
            print "Test 1 Passed : No seat reserved for Reservation Id R001 with requirement of zero seats."
        else:
            print "Test 1 Failed : Reservation made for R001 with zero requirement of seats."

    def checkFirstCustomerSeat(self):
        self.testTheater.bookSeat("R002 5")
        list = ["J1", "J2", "J3", "J4", "J5"]

        if self.testTheater.getResults()["R002"] == list:
            print "Test 2 Passed : 5 Seats successfully reserved for first customer at the top row."
        else:
            print "Test 2 Failed : Failed to reserve seats for first customer at the top row."

    def checkConsecutiveSeats(self):
        list = ["R002", "R002", "R002", "R002", "R002"]

        if self.testTheater.getList(9, 0, 4) == list:
            print "Test 3 Passed : 5 Consecutive seats successfully reserved for first customer row J."
        else:
            print "Test 3 Failed : Failed to reserve consecutive seats."

    def checkInsufficientSeats(self):
        self.testTheater.bookSeat("R003 250")
        if self.testTheater.getNumberOfSeats() > 0:
            print "Test 4 Passed : Failed to allocate seats when the request was greater than the available seats."
        else:
            print "Test 4 Failed : Allocated as many seta as possible."

    def checkGroupUnableToAccomodateInRow(self):
        result = self.testTheater.bookSeat("R004 24")
        if result == 0:
            print "Test 5 Passed : Successfully allocated seats to a large group that could not be accomodated in a row."
        else:
            print "Test 5 Failed : Failed to allocate seats to a large group."

    def checkGroupAccomodationOfSizeLargerSize(self):
        list = ["I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10", "I11", "I12", "I13", "I14", "I15", "I16",
                "I17", "I18", "I19", "I20", "J6", "J7", "J8", "J9"]

        if self.testTheater.getResults()["R004"] == list:
            print "Test 6 Passed : Successfully accomodated a group that could not be accomodated in a single row."
        else:
            print "Test 6 Failed : Failed to accomodate the group that could not be accomodated in a single row."
