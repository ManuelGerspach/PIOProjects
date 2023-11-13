import sys
import os
import urllib
import pathlib
import categorySimplification
from SolverConnection.solver import Solver


# parameter
solver_path = "C:\PioSOLVER\PioSOLVER2-pro.exe"
solution_path = r"C:\Users\Manuel\Desktop\PIOProjects\TestData\7d6h2h.cfr"

def main():

    
    # starts the solver process using the provided .exe path
    connection = Solver(solver_path)
    # report success
    print("Solver connected successfully")


    # run the program:
    categorySimplification.algorythm(connection)




    # we have to explicitely close the solver process
    print("Closing connection:")
    connection.exit()
    print("Connection closed.")
    print('Done.')




def print_lines(lines):
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()