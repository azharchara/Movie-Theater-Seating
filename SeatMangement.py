class SeatMangement(object):

    def __init__(self):
        self.rows = 10
        self.columns = 20
        self.numberOfSeats = self.rows * self.columns
        self.hm = {}
        self.seats = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.remainingSeats = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
        self.satisfaction = 0
        self.totalCustomers = 0

    def bookSeat(self, reservation): # R001 2
        input = reservation.split(" ")
        rno = input[0]
        count = int(input[1])
        group = count
        output = 0
        if count > 0:
            if self.numberOfSeats >= count:
                self.totalCustomers += count
                while group > 20:
                    output = self.assign(rno, 20)
                    group -= 20
                output = self.assign(rno, group)

                return output
            else:
                return -1
        else:
            return 1

    def assign(self, rno, seatsToBook): # R001 20
        r = 9
        while 0 <= r < self.rows:
            if self.remainingSeats[r] >= seatsToBook:
                for c in range(0, 20):
                    if seatsToBook > 0:
                        if self.seats[r][c] == 0:
                            self.seats[r][c] = rno
                            if rno in self.hm:
                                self.hm[rno].append(chr(r + 65) + str(c + 1))
                            else:
                                list = []
                                list.append(chr(r + 65) + str(c + 1))
                                self.hm[rno] = list

                            self.remainingSeats[r] -= 1
                            self.numberOfSeats -= 1
                            seatsToBook -= 1
                            self.satisfaction += 1
            r = r - 1

        return 0

    def getList(self, row, columnstart, columnEnd):
        list = []
        for c in range(columnstart, columnEnd + 1):
            list.append(self.seats[row][c])
        return list

    def getResults(self):
        return self.hm

    def getNumberOfSeats(self):
        return self.numberOfSeats

    def analysis(self):
        print "-------- REPORT --------"
        print "Total number of groups: ", len(self.hm)
        print "Total customers : ", self.totalCustomers
        print "Total number of Satisfied customers: ", self.satisfaction
        print "Percentage of Satisfied Customers :", self.satisfaction * 100 / self.totalCustomers
        print "Theater Utilization Percent: ", ((float(200 - self.numberOfSeats)/200) * 100)

    def printLayout(self):
        print "------------ BOOKINGS --------------"
        for r in range(0, 10):
            print chr(r + 65) + " "
            for c in range(0, 20):
                print " " + str(self.seats[r][c])

