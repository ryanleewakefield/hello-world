#The goal of this program is to solve sudoku puzzles

def create_address():
    #   This function defines all of the addresses, or places where a number can reside in a sudoku puzzle.
    # The matrices variable is a list to contain the 9 sub blocks within a puzzle, denote by TopLeft = tL,
    # MiddleLeft = mL and so on. Each address is denoted as "r#c#", meaning row #, column #. These addresses
    # are keys of a dictionary. In order to cycle through the dictionary, a series of for loops are used throughout
    # the program. Some functions use the return data of this function to reduce code of the for loops. This has
    # not been fully implemented. 
    addresses = []
    global matrices
    matrices = []
    tL = []
    tM = []
    tR = []
    mL = []
    mM = []
    mR = []
    bL = []
    bM = []
    bR = []
    matrices.append(tL)
    matrices.append(tM)
    matrices.append(tR)
    matrices.append(mL)
    matrices.append(mM)
    matrices.append(mR)
    matrices.append(bL)
    matrices.append(bM)
    matrices.append(bR)
    for i in range(1, 10):
        for j in range(1, 10):
            key = "r" + str(i) + "c" + str(j)
            str(key)
            addresses.append(key)
            #   The organization of the matrices is as such
            #|---------------------------matrix--------------------------------|
            #|------topLeft-------|----topMiddle---------|-------topRight------|
            #|-'r1c1'-r1c2'-r1c3'-|-'r1c4'-'r1c5'-'r1c6'-|-'r1c7'-'r1c8'-r1c9'-|
            #|-'r2c1'-r2c2'-r2c3'-|-'r2c4'-'r2c5'-'r2c6'-|-'r2c7'-'r2c8'-r2c9'-|
            #|-'r3c1'-r3c2'-r3c3'-|-'r3c4'-'r3c5'-'r3c6'-|-'r3c7'-'r3c8'-r3c9'-|
            #|-----middleLeft-----|----middleMiddle------|-----middleRight-----|
            #|-'r4c1'-r4c2'-r4c3'-|-'r4c4'-'r4c5'-'r4c6'-|-'r4c7'-'r4c8'-r4c9'-|
            #|-'r5c1'-r5c2'-r5c3'-|-'r5c4'-'r5c5'-'r5c6'-|-'r5c7'-'r5c8'-r5c9'-|
            #|-'r6c1'-r6c2'-r6c3'-|-'r6c4'-'r6c5'-'r6c6'-|-'r6c7'-'r6c8'-r6c9'-|
            #|-----bottomLeft-----|-----bottomMiddle-----|------bottomRight----|
            #|-'r7c1'-r7c2'-r7c3'-|-'r7c4'-'r7c5'-'r7c6'-|-'r7c7'-'r7c8'-r7c9'-|
            #|-'r8c1'-r8c2'-r8c3'-|-'r8c4'-'r8c5'-'r8c6'-|-'r8c7'-'r8c8'-r8c9'-|
            #|-'r9c1'-r9c2'-r9c3'-|-'r9c4'-'r9c5'-'r9c6'-|-'r9c7'-'r9c8'-r9c9'-|
            #|-----------------------------------------------------------------|
            if i < 4:
                if j < 4:
                    tL.append(key)
                if 4 <= j < 7:
                    tM.append(key)
                if 7 <= j < 10:
                    tR.append(key)
            if 4 <= i < 7:
                if j < 4:
                    mL.append(key)
                if 4 <= j < 7:
                    mM.append(key)
                if 7 <= j < 10:
                    mR.append(key)
            if 7 <= i < 10:
                if j < 4:
                    bL.append(key)
                if 4 <= j < 7:
                    bM.append(key)
                if 7 <= j < 10:
                    bR.append(key)
            #   Thus, logic can be applied to if a particular address is associated with a matrix subset
                    
    return addresses
            
def get_input(box):
    #   This function is for getting input manual through the keyboard. It most likely won't be used as
    # copying and pasting from a text document is easier to avoid entry errors.
    key = create_address()

    for i in key:
        value = input("Enter a value for address " + i + ": ")
        value = int(value)
        box[i] = [value]
        
def get_list(box):
    #    This function gets the data from a global variable called 'numbers_string' which can be copied and pasted
    # into in the main program located further below
    key = create_address()
    numbers_list = []
    #   Each sudoku puzzle is a 9 by 9 grid, so there should be only 81 data entries.
    for j in range(0, 81):
        num = int(numbers_string[j])
        numbers_list.append(num)

    for i in range(0, 81):
        #   This part of the function pairs each key of the dictionary to a value
        # from the original variable 'numbers_string'.
        dop = key[i]
        box[dop] = [numbers_list[i]]
        
def check_box(box):
    for i in range(1, 10):
        for j in range(1, 10):
            key = "r" + str(i) + "c" + str(j)
            
            if box[key][0] in potential_values:
            #   This part checks that the value assigned the address isn't zero
                
                for k in range(1, 10):
                    
                    key_change = "r" + str(i) + "c" + str(k)
                    if box[key_change][0] == 0:
                        box[key_change].append(-box[key][0])
                    #   This part appends the current key's value as a negative number
                    # to each address which has zero value that is in the same row as the current key.
                    key_change = "r" + str(k) + "c" + str(j)
                    if box[key_change][0] == 0:
                        box[key_change].append(-box[key][0])
                    #   This part appends the current key's value as a negative number
                    # to each address which has zero value that is in the same column as the current key.
            else:
                continue
               
            for h in range(0, 9):
                if key in matrices[h]:
                #   This part refers to each sub matrix, such as topLeft, by list index.
                    for g in range(0, 9):
                        key_change = matrices[h][g]
                        #   key_change is equivalent to the address within each sub matrix.
                        if box[key_change][0] == 0:
                        #   If the address doesn't have a definitive value, the first element in its list should
                        # be zero.
                            box[key_change].append(-box[key][0])

            #   The negative values which are appended to each address list will be analyzed later to
            # determine which possible values could fit the puzzle for that address
            
def reduce_duplicates(box):
    #   The check_box function creates a lot of duplicate values. This function clears just the duplicates,
    # in order for the dictionary to be easier to read by humans.
    for i in range(1, 10):
        for j in range(1, 10):
            key = "r" + str(i) + "c" + str(j)
            key_switch = []
            for k in box[key]:
                if k not in key_switch:
                    key_switch.append(k)
            del box[key]
            box[key] = key_switch
                


def sort_addresses(box):
    #   This function arranges each address from greatest to least in order to make sure each zero value
    # is first in the list for addresses without definitive answers, for logic purposes.
    for i in range(1, 10):
        for j in range(1, 10):
            key = "r" + str(i) + "c" + str(j)
            box[key].sort(reverse = True)

def get_answers(box):
    #   This function analyzes which negative values aren't in each address's list and appends those values
    # as postive values.
    for i in range(1, 10):
        for j in range(1, 10):
            key = "r" + str(i) + "c" + str(j)
            for k in potential_answers:
                if box[key][0] == 0:
                    if k not in box[key]:
                        box[key].append(-k)

def sort_answers(box):
    #   This function gets rid of all negative values from each address by appending all zero and
    # positive integers values into a new list, deleting the old key, and adding the old key back
    # with a new list as a value.
    for i in range(1, 10):
        for j in range(1, 10):
            key = "r" + str(i) + "c" + str(j)
            key_switch = []
            for k in box[key]:
                if k not in potential_answers:
                    key_switch.append(k)
            del box[key]
            box[key] = key_switch

def analyze_output(box):
    #   The logic of this function is as follows: If an address has two elements, the elements must be
    # zero and some other value. That other value must be the correct input for that address, because the
    # previous program functions didn't find any other potential answers.
    for i in range(1, 10):
        for j in range(1, 10):
            key = "r" + str(i) + "c" + str(j)
            for k in box[key]:
                if len(box[key]) == 2:
                    box[key].remove(0)

                
def analysis_cycle(box):
    #   This function is just a space saving composite function that ties all the previous functions together.
    # This code can be run multiple times in order to get closer to a complete sudoku solution. The variable
    # analysis_count keeps track of how many times the composite function ran, in order to define how difficult
    # a puzzle was to solve.
    get_list(box)
    check_box(box)
    reduce_duplicates(box)
    sort_addresses(box)
    get_answers(box)
    sort_answers(box)
    analyze_output(box)

    print("""
    Cycle Analysis Complete
        """)
    global analysis_count
    analysis_count += 1
    stringconvert = str(analysis_count)
    print("Total run times: " + stringconvert)
    
    #input("Press Enter to continue")
    
def clear_box(box):
    #   This function clears each address to one element, preparing it to be assembled into a string
    # for further anaylsis runs.
    key = create_address()
    for i in key:       
        while len(box[i]) > 1:
            box[i].pop()
            
def load_answers(box):
    #   This function concatenates the first element of each key into the string, 'numbers_string', in order
    # to run another analysis.
    global numbers_string
    numbers_string = "0"
    for i in range(1, 10):
        for j in range(1, 10):
            key = "r" + str(i) + "c" + str(j)
            
            num = str(box[key][0])
            numbers_string = numbers_string + num

    numbers_string = numbers_string[1:]
    
                    
def pretty_print(box):
    #   This function prints the passed in dictionary in a easy to read fashion.
    for i in range(1, 10):
        for j in range(1, 10):
            key = "r" + str(i) + "c" + str(j)
            print(key,box[key])               

def dictionary_into_list(box):
    #   This function is for putting the data from the dictionary into a form that can be easily
    # converted into a csv file for spreadsheet anaylsis
    sudoku_list = []
    for i in range(1, 10):
            for j in range(1, 10):
                key = "r" + str(i) + "c" + str(j)
                sudoku_list.append(box[key])
    sudoku_list = str(sudoku_list)
    sudoku_list = sudoku_list[1:-1]
    sudoku_list = sudoku_list.replace("," , " ")
    sudoku_list = sudoku_list.replace("[" , " ")
    sudoku_list = sudoku_list.replace("]" , ",")
    comma_count = 0
    index_of_commas = []
    rows_of_strings = []
    for k in range(len(sudoku_list)):
        if sudoku_list[k] == ",":
            comma_count += 1
            if comma_count % 9 == 0:
                index_of_commas.append(k)
    
    rows_of_strings.append(sudoku_list[0:int(index_of_commas[0])])
    for h in range(0, 8):
        rows_of_strings.append(sudoku_list[int(index_of_commas[h]) + 1:int(index_of_commas[h+1])])
    rows_of_strings.append(sudoku_list[int(index_of_commas[8]):])
            
        
    return rows_of_strings

def matrix_analysis(box):
    for j in range(0, 8):
        analysis_list = []
        
        
        ones = []
        twos = []
        threes = []
        fours = []
        fives = []
        sixes = []
        sevens = []
        eights = []
        nines = []
        numbers = [ones, twos, threes, fours, fives, sixes, sevens, eights, nines]

        
            
        for key in matrices[j]:
            if box[key][0] == 0:
                for i in box[key]:
                    analysis_list.append(i)
        analysis_list.sort()
        for k in analysis_list:
            for h in range(1, 10):
                if k == h:
                    numbers[h-1].append(k)
        for g in numbers:
            if len(g) == 1:
                for key in matrices[j]:
                    if g[0] in box[key]:
                        box[key] = [g[0]]
                
    
               
if __name__ == "__main__":
    
    potential_values = (1,2,3,4,5,6,7,8,9)

    potential_answers = (-1,-2,-3,-4,-5,-6,-7,-8,-9)
    #dog = dictionary_into_list(container_one)
    analysis_count = 0
    #Easy Puzzle 1
    #numbers_string = "010480600623500000000073020092007804800905007706200590070150000000009751005036040"

    #Hard Puzzle 1
    #numbers_string = "000170053000006870073500000005400030800050002040009500000004920064900000950013000"

    #Easy Puzzle 2
    #numbers_string = "030900450079520010006007002005001068700050001140800300900400800080092170014003020"

    #Medium Puzzle 1
    #numbers_string = "100340007000070030780005900670004500001803400004700089005100024010030000300026008"

    #Medium Solution 1
    #answer_string = "129348657456972831783615942678294513291853476534761289965187324812439765347526198"

    #Easy Solution 1
    #answer_string = "917482635623591478458673129592367814831945267746218593279154386364829751185736942"

    #Hard Solution 1
    #answer_string = "489172653521346879673598241295487136837651492146239587318764925764925318952913764"

    #Easy Solution 2
    #answer_string = "231968457879524613456137982395241768768359241142876395927415836583692174614783529"

    #Impossible Puzzle
    #numbers_string = "314100556997073938114156064238047257930482496477166759010400976818475244871716793"
    #numbers_string_copy = "314100556997073938114156064238047257930482496477166759010400976818475244871716793"
    #answer_string = "0"
    
    container_one = {}
    
    
    while True:
        total_length = 0
        analysis_cycle(container_one)
        for i in range(1, 10):
            for j in range(1, 10):
                key = "r" + str(i) + "c" + str(j)
                total_length = total_length + len(container_one[key])
        if total_length <= 81:
            break
        
        clear_box(container_one)

        load_answers(container_one)
       
        
    clear_box(container_one)

    load_answers(container_one)
    pretty_print(container_one)   
    print(numbers_string)
    if numbers_string == answer_string:
        print("Correct")
    else:
        print("Error")
        
#matrix_analysis(container_one)
#pretty_print(container_one)
    
