#rational root theorem

def rrt():
    global denominator
    denominator = []
    global numerator
    numerator = []
    if first_coef < 0:
        for i in range(first_coef, 0):
            if first_coef % i == 0:
                denominator.append(i)
            if first_coef % -i == 0:
                denominator.append(-i)
    for i in range(1 , first_coef + 1):
        if first_coef % i == 0:
            denominator.append(i)
        if first_coef % -i == 0:
            denominator.append(-i)
    if constant < 0:
        for i in range(constant, 0):
            if constant % i == 0:
                numerator.append(i)
            if constant % -i == 0:
                numerator.append(-i)
    for i in range(1 , constant + 1):
        if constant % i == 0:
            numerator.append(i)
        if constant % -i == 0:
             numerator.append(-i)

    #print(numerator)
    #print(denominator)

    global rational_roots
    rational_roots = []
    
    for i in numerator:
        for j in denominator:
            roots = i / j
            rational_roots.append(roots)
    #print("The possible roots are...")
    #print(rational_roots)

    
            


def checkans():
    global terms_list
    terms_list = []
    while True:
        try:
            num_terms = int(input("Enter the number of terms up to 10; must have 3: "))
            while num_terms > 10:
                print("Invalid Entry: number of terms must be 10 or less.")
                sleep(1)
                num_terms = int(input("Enter the number of terms to 10; must have 3: "))
            while num_terms < 3:
                print("Invalid Entry: must have at least 3 terms.")
                sleep(1)
                num_terms = int(input("Enter the number of terms to 10; must have 3: "))
            if 3 <= num_terms <= 10:
                break
        except ValueError:
            print("Invalid Entry: Enter integers only")
            
    num_terms_copy = num_terms
    while True:
        try:
            term_input = (int(input("Enter 1st coefficient: ")))
            while term_input != first_coef:
                print("Error: Entry doesn't match previous coefficient.")
                sleep(1)
                term_input = (int(input("Enter 1st coefficient: ")))
            terms_list.append(term_input)
            num_terms -= 1
            if num_terms_copy == num_terms + 1:
                break
        except ValueError:
            print("Invalid Entry: Enter integers only")

    while num_terms != 0:
        if num_terms == 1:
            try:
                term_input = int(input("Enter the constant: "))
                while term_input != constant:
                    print("Error: Entry doesn't match previous constant.")
                    sleep(1)
                    term_input = int(input("Enter the constant: "))
                terms_list.append(term_input)
                break
            except ValueError:
                print("Invalid Entry: Enter integers only")
        while num_terms > 1:
            try:
                term_input = int(input("Enter next coefficient: "))
                terms_list.append(term_input)
                num_terms -= 1
            except ValueError:
                print("Invalid Entry: Enter integers only")
                


    global expon_list
    expon_list = []
    
    global num_terms_ex_copy
    num_terms_ex_copy = num_terms_copy

    
    while num_terms_copy != 1:
        try:
            expon_input = int(input("Enter exponent: "))
            expon_list.append(expon_input)
            num_terms_copy -= 1
        except ValueError:
                print("Invalid Entry: Enter integers only")

def get_ans():
    answers = []
    all_answers_list = []
    if num_terms_ex_copy == 3:
        for i in rational_roots:
            all_answer = terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] 
            all_answers_list.append(all_answer)
            if terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] == 0 :
                answers.append(i)
    if num_terms_ex_copy == 4:
        for i in rational_roots:
            all_answer = terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] * i ** expon_list[2] + terms_list[3]
            all_answers_list.append(all_answer)
            if terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] * i ** expon_list[2] + terms_list[3] == 0:
                answers.append(i)
    if num_terms_ex_copy == 5:
        for i in rational_roots:
            all_answer = terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] * i ** expon_list[2] + terms_list[3] * i ** expon_list[3] + terms_list[4]
            all_answers_list.append(all_answer)
            if terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] * i ** expon_list[2] + terms_list[3] * i ** expon_list[3] + terms_list[4] == 0:
                answers.append(i)
    if num_terms_ex_copy == 6:
        for i in rational_roots:
            all_answer = terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] * i ** expon_list[2] + terms_list[3] * i ** expon_list[3] + terms_list[4] * i ** expon_list[4] + terms_list[5]
            all_answers_list.append(all_answer)
            if terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] * i ** expon_list[2] + terms_list[3] * i ** expon_list[3] + terms_list[4] * i ** expon_list[4] + terms_list[5] == 0:
                answers.append(i)
    if num_terms_ex_copy == 7:
        for i in rational_roots:
            all_answer = terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] * i ** expon_list[2] + terms_list[3] * i ** expon_list[3] + terms_list[4] * i ** expon_list[4] + terms_list[5]* i ** expon_list[5] + terms_list[6]
            all_answers_list.append(all_answer)
            if terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] * i ** expon_list[2] + terms_list[3] * i ** expon_list[3] + terms_list[4] * i ** expon_list[4] + terms_list[5]* i ** expon_list[5] + terms_list[6] == 0:
                answers.append(i)
    if num_terms_ex_copy == 8:
        for i in rational_roots:
            all_answer = terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] * i ** expon_list[2] + terms_list[3] * i ** expon_list[3] + terms_list[4] * i ** expon_list[4] + terms_list[5] * i ** expon_list[5] + terms_list[6] * i ** expon_list[6] + terms_list[7]
            all_answers_list.append(all_answer)
            if terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] * i ** expon_list[2] + terms_list[3] * i ** expon_list[3] + terms_list[4] * i ** expon_list[4] + terms_list[5] * i ** expon_list[5] + terms_list[6] * i ** expon_list[6] + terms_list[7] == 0:
                answers.append(i)
    if num_terms_ex_copy == 9:
        for i in rational_roots:
            all_answer = terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] +  terms_list[2] * i ** expon_list[2] + terms_list[3] * i ** expon_list[3] + terms_list[4] * i ** expon_list[4] + terms_list[5] * i ** expon_list[5] + terms_list[6] * i ** expon_list[6] + terms_list[7] * i ** expon_list[7] + terms_list[8]
            all_answers_list.append(all_answer)
            if terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] +  terms_list[2] * i ** expon_list[2] + terms_list[3] * i ** expon_list[3] + terms_list[4] * i ** expon_list[4] + terms_list[5] * i ** expon_list[5] + terms_list[6] * i ** expon_list[6] + terms_list[7] * i ** expon_list[7] + terms_list[8] == 0:
                answers.append(i)
    if num_terms_ex_copy == 10:
        for i in rational_roots:
            all_answer = terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] * i ** expon_list[2] + terms_list[3] * i ** expon_list[3] + terms_list[4] * i ** expon_list[4] + terms_list[5] * i ** expon_list[5] + terms_list[6] * i ** expon_list[6] + terms_list[7] * i ** expon_list[7] + terms_list[8] * i ** expon_list[8] + terms_list[9]
            all_answers_list.append(all_answer)
            if terms_list[0] * i ** expon_list[0] + terms_list[1] * i ** expon_list[1] + terms_list[2] * i ** expon_list[2] + terms_list[3] * i ** expon_list[3] + terms_list[4] * i ** expon_list[4] + terms_list[5] * i ** expon_list[5] + terms_list[6] * i ** expon_list[6] + terms_list[7] * i ** expon_list[7] + terms_list[8] * i ** expon_list[8] + terms_list[9] == 0:
                answers.append(i)
    print(answers)
    print("These real rational root values satisfy the equation\n")
    #print(all_answers_list)
    #print("These are all calculations of the possible roots")
    
if __name__ == "__main__":
    from time import sleep
    while True:
        print("Rational Root Theorem Program\n")
        try:
            first_coef = input("Enter the first coefficient or q to quit: ")
            if first_coef == "q":
                break
            first_coef = int(first_coef)
            constant = int(input("Enter the constant: "))
 
            rrt()
            checkans()
            get_ans()
            
        except ValueError:
            print("""

            Invalid Entry: Enter integers only""")
            sleep(1)
