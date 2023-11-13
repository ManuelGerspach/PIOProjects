import sys
import os
import urllib
import pathlib
from SolverConnection.solver import Solver


# parameter
solver_path = "C:\PioSOLVER\PioSOLVER2-pro.exe"
solution_path = r"C:\Users\Manuel\Desktop\PIOProjects\TestData\7d6h2h.cfr"

def main():
    # check if there are enough command line arguments provided
    # if len(sys.argv) <3:
    #     print("Needs 2 arguments (solver path and path to the .cfr file).")
    #     return
    
    # starts the solver process using the provided .exe path
    connection = Solver(solver_path)
    # report success
    print("Solver connected successfully")

    # now let's use created solver connection to call some commands

    # call and print the result of "show metadata" on the provided .cfr file
    metadata = connection.command(line =f"show_metadata {solution_path}")
    print_lines(metadata)

    # load the tree
    output = connection.command(line=f"load_tree {solution_path}")
    print_lines(output)

    # show hands order (solver will return always the same answer)
    handorder = connection.command("show_hand_order")
    print_lines(handorder)
    
    # show ranges
    print("Range OOP:")
    range = connection.command("show_range OOP r")
    print_lines(range)

    print("Range IP:")
    range = connection.command("show_range IP r")
    print_lines(range)

    # calculate EV
    calcevOOP = connection.command("calc_ev OOP r:0")
    print("EV IP:")
    print_lines(calcevOOP)

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