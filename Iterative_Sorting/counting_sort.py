# Counting sort is an algorithm that sorts elements based on a numeric key value

'''Input: [10, 7, 12, 4, 9, 13]

1. Find the minimum and maximum value
    If we scan the numbers we see
    min = 4
    max = 13
    So, our range is from 4 to 13
 
2. Create index from 4 to 13
    index [4][5][6][7][8][9][10][11][12][13]

3. Create an array that will hold the count of each number
    count [][][][][][][][][][]

4. Count how many times each element appears in input
    count [1][0][0][1][0][1][1][0][1][1] 
    NOTE: aka 4 appears 1 times, 5 appears 0 times, 6 appears 0 times, 7 appears 1 time etc.

5. Create a sumCount array that will hold the sum of counts for given index
    sumCount [][][][][][][][][][]

6. NOTE: Since index 4 is the first index simply copy the count to sumCount

sumCount [1][][][][][][][][][]

NOTE: index 5 has count 0 and previous index is 4 with sumCount 1
NOTE: so sumCount = sumCount of previous index + count for current index 
NOTE: so sumCount for index 5 = 1 + 0 which is 1

sumCount [1][1][][][][][][][][]

NOTE: index 6 has count 0 and previous index is 5 with sumCount 1
NOTE: so sumCount for index 6 = 1 + 0 which is 1

sumCount [1][1][1][][][][][][][]

NOTE: index 7 has count 1 and previous index is 6 with sumCount 1
NOTE: so sumCount for index 7 = 1 + 1 which is 2

sumCount [1][1][1][2][][][][][][]

NOTE: index 8 has count 0 and previous index is 7 with sumCount 2
NOTE: so sumCount for index 8 = 2 + 0 which is 2

sumCount [1][1][1][2][2][][][][][]

NOTE: index 9 has count 1 and previous index is 8 with sumCount 2
NOTE: so sumCount for index 9 = 2 + 1 which is 3

sumCount [1][1][1][2][2][3][][][][]

NOTE: index 10 has count 1 and previous index is 9 with sumCount 3
NOTE: so sumCount for index 10 = 3 + 1 which is 4

sumCount [1][1][1][2][2][3][4][][][]

NOTE: index 11 has count 0 and previous index is 10 with sumCount 4
NOTE: so sumCount for index 11 = 4 + 0 which is 4

sumCount [1][1][1][2][2][3][4][4][][]

NOTE: index 12 has count 1 and previous index is 11 with sumCount 5
NOTE: so sumCount for index 12 = 5 + 1 which is 5

sumCount [1][1][1][2][2][3][4][4][5][]

NOTE: index 13 has count 1 and previous index is 12 with sumCount 6
NOTE: so sumCount for index 13 = 6 + 1 which is 6

sumCount [1][1][1][2][2][3][4][4][5][6]

7. Sort the input using sumCount
There are 6 numbers in input so we will create 6 positions and 
fill those positions with the given numbers as per sumCount

position [1][2][3][4][5][6]
sorted input [][][][][][]

index    [4][5][6][7][8][9][10][11][12][13]
sumCount [1][1][1][2][2][3][4] [4] [5] [6]

NOTE: first input is 10
NOTE: sumCount for index 10 is 4
NOTE: so place 10 in index 4 and reduce sumCount index 10 by 1
index    [4][5][6][7][8][9][10][11][12][13]
sumCount [ ][ ][ ][ ][ ][ ][3] [ ] [ ] [ ]

position     [1][2][3][4][5][6]
sorted input [ ][ ][ ][10][ ][ ]

NOTE: second input is 7
NOTE: sumCount for index 7 is 2
NOTE: so place 7 in index 2 and reduce sumCount index 7 by 1

index    [4][5][6][7][8][9][10][11][12][13]
sumCount [ ][ ][ ][1][ ][ ][3] [ ] [ ] [ ]

position     [1][2][3][4] [5] [6]
sorted input [ ][7][ ][10][ ] [ ]

NOTE: third input is 12
NOTE: sumCount for index 12 is 5
NOTE: so place 12 in index 5 and reduce sumCount index 12 by 1

index    [4][5][6][7][8][9][10][11][12][13]
sumCount [ ][ ][ ][1][ ][ ][3] [ ] [4 ] [ ]

position     [1][2][3][4] [5] [6]
sorted input [ ][7][ ][10][12] [ ]

NOTE: fourth input is 4
NOTE: sumCount for index 4 is 1
NOTE: so place 4 in index 1 and reduce sumCount index 4 by 1

index    [4][5][6][7][8][9][10][11][12][13]
sumCount [0][ ][ ][1][ ][ ][3] [ ] [4 ] [ ]

position     [1][2][3][4] [5] [6]
sorted input [4][7][ ][10][12][ ]

NOTE: fifth input is 9
NOTE: sumCount for index 9 is 3
NOTE: so place 9 in index 3 and reduce sumCount index 9 by 1

index    [4][5][6][7][8][9][10][11][12][13]
sumCount [0][ ][ ][1][ ][2][3] [ ] [4 ] [ ]

position     [1][2][3][4] [5] [6]
sorted input [4][7][9][10][12][ ]

NOTE: sixth input is 13
NOTE: sumCount for index 13 is 6
NOTE: so place 13 in index 6 and reduce sumCount index 13 by 1

index    [4][5][6][7][8][9][10][11][12][13]
sumCount [0][ ][ ][1][ ][2][3] [ ] [4 ] [5]

position     [1][2][3][4] [5] [6]
sorted input [4][7][9][10][12][13] NOTE: ALL DONE

NOTE: Original sumCount vs sumCount after sort
sumCount        [1][1][1][2][2][3][4][4][5][6]
final sumCount  [0][1][1][1][2][2][3][4][4][5]
'''
