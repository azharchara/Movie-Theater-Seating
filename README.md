**Author - Azhar Chara**

**Movie Theater Seating Challenge - 2021**

**Language used:**  Python

**Program Description:**

This program takes an input file, reads line by line and processes the user requests for reserving seats in the movie theater.

The algorithm follows following rules:

1. Customers that come first will be allocated seats in the top rows.
2. Each group will be allocated seats in a single row. If the group is larger than the number of seats in the row, split the group and allocate as many seats available in that that row for few members and for others allocate in the other row.
3. Full fill as many requests as possible.
4. After scanning all the rows, if the theater is not able to allocate nearby (consecutive) seats to a group, then allocate seats wherever there is a vacant seat.
5. If the numbers of requested seats are not available in the theater then, inform the customer about insufficient seats.

**Assumptions:**

1. The theater cannot reserve seats for a group if the requested number of seats is greater than the available seats. In that case, the customers are informed about the insufficient number of available seats.
2. The reservation number(R###) will be in sequential order like (R001, R002, R003...) in the input file.

**How are the goals of the problem statement achieved?**

_Customer Satisfaction:_

1. Since customers are reserving seats for groups, they would prefer sitting next to each other. So the first priority will be to allocate seats for the group in a single row.
2. Since the top seats give a better viewing experience in the movie theater, customers who come first will be allocated seats in the top rows.

_Maximum Theater Utilization:_

1. To make sure that we are able to accommodate as many groups as possible and also keep them satisfied by allocating consecutive seats, we start allocating seats from the first column. This will allow us to allocate seats for maximum number of groups in a single row.
2. In one or two cases if we are not able to accommodate a group in a single row, then we allocate the seats starting from top row and wherever there is a vacant seat we allocate in the theater.

**Steps for running**
1. Download and save the folder in a directory.
2. Run the program Start.py with the help of following command : python Start.py
3. Output File path will be presented in the command line