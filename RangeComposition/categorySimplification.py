node_ID = "r:0:c" # can be copied in PIO solver if you right click on the board in the viewer

def algorythm(connection):

    solution_path = r"C:\Users\Manuel\Desktop\PIOProjects\TestData\7d6h2h.cfr"


    # load the tree
    output = connection.command(line=f"load_tree {solution_path}")
    print_lines(output)

    # read 1. category hands
    readCat(connection, "12")
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


def readBetFrequency(connetion, index):
    strat = connetion.command("show_strategy " + node_ID)
    bettingStrat = strat[0].split(" ")
    comboFrequency = bettingStrat[index]
    return comboFrequency
### TBD!!! filter out combos that are not in range!!!!!!!!!! (eventuell, bei sets geht es, muss noch schauen wie es funktioniert ektuell)

def readCat(connection, catNumer):
    ## categories:
    # nothing 0, king_high 1, ace_high 2, low_pair 3, 3rd-pair 4, 2nd-pair 5, underpair 6,  top_pair 7, top_pair_tp8, overpair 9, two_pair 10, trips 11, set 12,  straight 13,  flush 14, fullhouse 15, top_fullhouse 16,  quads 17,  straight_flush19, 
    # no_draw 0,  4out_straight_draw 1, 8out_straight_draw 2,  flush_draw 3,  combo_draw 4
    
    cats = connection.command("show_categories 7d6h2h")
    madeHands = cats[0].split(" ")

    combosFrequencies = []
    
    i = 0
    for combo in madeHands:
        if combo == catNumer:
            combosFrequencies.append(readBetFrequency(connection, i))
            
        i = i + 1
    print(combosFrequencies)
    return combosFrequencies
    # return cats



    





def print_lines(lines):
    for line in lines:
        print(line)