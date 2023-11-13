def algorythm(connection):

    solution_path = r"C:\Users\Manuel\Desktop\PIOProjects\TestData\7d6h2h.cfr"

    # load the tree
    output = connection.command(line=f"load_tree {solution_path}")
    print_lines(output)
    print_lines("Hello")


    # read 1. category hands
        # for each category find out frequency of bet
            # safe frequency in vairable and increase counter of all combos for this category
                # safe frequency
                    # print or/and safe average frequency for this single board
    # TBD: erst eine category über alle boards oder alle categorien über ein board
    # TBD: average über alle boards rechnen, nicht nur über ein board (nicht average frequencies zusammen rechnen, sondern average über alle boards bauen)

    # read 2. category
        # repeat step 1
    # repeat for all categories

    # repeat for all files in folder

    # 





def print_lines(lines):
    for line in lines:
        print(line)