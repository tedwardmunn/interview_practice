'''
CISC101 Assignment 4 - Magic Square Program
Name: Charles Cottrelle
Student ID: 20017689
Written Date: Wednesday, March 25, 2020
Last Modified: Friday, March 27, 2020

Magic Square Program
The solution presented below utilizes the time and random module to determine
whether the random number matrix generated creates a magic square. Using loops,
each column, row, and diagonal is assessed to conclude whether a magic square
has been created. 
'''
import random
import time
def main():
    tim_st=time.time()
    tim_st2=time.ctime()
    
    s=0 # s is a counter that prints how many tries have been made
    while True: # keep trying until you find a magic square
        magic=True # assume that magic is True, as a start
        mat1=[] # intialize matrix1 (mat1) to hold 9 unique numbers
        
        # generate a random number between 1 and 9
        # check if the generated number exists in the list,  if it exists try 
        # again, if it doesn't exist in the list then append it to the list
        i=1
        while i < 10:
            rand_number = random.randint(1,9)
            while rand_number in mat1:
                rand_number = random.randint(1,9)
            mat1.append(rand_number)
            i += 1

    # intialize mat2 Multi-dimensional list with
    # 3 rows and 3 columns
        mat2 = [[0,0,0],[0,0,0],[0,0,0]]
        xyz = 3
        abc = 0
        
        # Transfer the nine random number into the mat2 in order 3 x 3 x 3   
        for i in range (xyz):
            for j in range (xyz):
                mat2[i][j] = mat1[abc]
                abc += 1
        
        ##### Sum of the first row, call it sum1
        sum1 = sum(mat2[0])

        ##### Sum of rows, and check if the each row's sum equal to sum1
        if sum(mat2[1]) != sum1 or sum(mat2[2]) != sum1:
            magic = False 

        ##### Sum of colomns, and check if each column's sum equal to sum1        
        for column in range(xyz):
            sum_column = 0
            for row in range(xyz):
                sum_column += mat2[row][column]
            if sum_column != sum1:
                magic = False
                break 

        ##### Sum of first Diagonal, and check if the sum equal to sum1 
        sum_diagonal1 = sum([mat2[0][0],mat2[1][1],mat2[2][2]])
        if sum_diagonal1 != sum1:
            magic = False
            
        ##### Sum of second Diagonal, and check if the sum equal to sum1 
        sum_diagonal2 = sum([mat2[0][2],mat2[1][1],mat2[2][0]])
        if sum_diagonal2 != sum1:
            magic = False

        # if it is a magic squre:
        if magic == True:
            time_end = time.time()
            time_end2 = time.ctime()
            print('It is a magic square.')
            # 1- print the magic square
            print(mat2)
            # 2- print the time it took to find one randomly
            print('It started at : {} using seconds.'.format(tim_st))
            print('It ended   at : {} using seconds.'.format(time_end))
            print('It started at : .', tim_st2)
            print('It ended   at : .', time_end2)
            duration = int(time_end - tim_st)
            print('It took {} seconds to find the magic square!'.format(duration))
            # 3- break out of the loop, STOP the program
            break

        # increment the counter 's' of tries and print it
        s += 1
        print(s)

main()