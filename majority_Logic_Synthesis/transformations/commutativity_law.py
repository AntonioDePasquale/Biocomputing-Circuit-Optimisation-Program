from auxillary_functions import *

class Commutativity :
    
    # Constructor for the Commutativity  class.
    # Combination dict is required for commutativity functionality and initialsed with the class constructor
    def __init__(self) :
        
        self.combinations = [
    {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0},
    {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 1},
    {'A': 0, 'B': 0, 'C': 0, 'D': 1, 'E': 0},
    {'A': 0, 'B': 0, 'C': 0, 'D': 1, 'E': 1},
    {'A': 0, 'B': 0, 'C': 1, 'D': 0, 'E': 0},
    {'A': 0, 'B': 0, 'C': 1, 'D': 0, 'E': 1},
    {'A': 0, 'B': 0, 'C': 1, 'D': 1, 'E': 0},
    {'A': 0, 'B': 0, 'C': 1, 'D': 1, 'E': 1},
    {'A': 0, 'B': 1, 'C': 0, 'D': 0, 'E': 0},
    {'A': 0, 'B': 1, 'C': 0, 'D': 0, 'E': 1},
    {'A': 0, 'B': 1, 'C': 0, 'D': 1, 'E': 0},
    {'A': 0, 'B': 1, 'C': 0, 'D': 1, 'E': 1},
    {'A': 0, 'B': 1, 'C': 1, 'D': 0, 'E': 0},
    {'A': 0, 'B': 1, 'C': 1, 'D': 0, 'E': 1},
    {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 0},
    {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 1},
    {'A': 1, 'B': 0, 'C': 0, 'D': 0, 'E': 0},
    {'A': 1, 'B': 0, 'C': 0, 'D': 0, 'E': 1},
    {'A': 1, 'B': 0, 'C': 0, 'D': 1, 'E': 0},
    {'A': 1, 'B': 0, 'C': 0, 'D': 1, 'E': 1},
    {'A': 1, 'B': 0, 'C': 1, 'D': 0, 'E': 0},
    {'A': 1, 'B': 0, 'C': 1, 'D': 0, 'E': 1},
    {'A': 1, 'B': 0, 'C': 1, 'D': 1, 'E': 0},
    {'A': 1, 'B': 0, 'C': 1, 'D': 1, 'E': 1},
    {'A': 1, 'B': 1, 'C': 0, 'D': 0, 'E': 0},
    {'A': 1, 'B': 1, 'C': 0, 'D': 0, 'E': 1},
    {'A': 1, 'B': 1, 'C': 0, 'D': 1, 'E': 0},
    {'A': 1, 'B': 1, 'C': 0, 'D': 1, 'E': 1},
    {'A': 1, 'B': 1, 'C': 1, 'D': 0, 'E': 0},
    {'A': 1, 'B': 1, 'C': 1, 'D': 0, 'E': 1},
    {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 0},
    {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1}
]
        
    # Commutativity Ω.C
    # M(x, y, z) = M(y, x, z) = M(z, y, x)
    def commutativity(self, majority_list) :
        
        combinations = self.combinations #copy of the combinations dict that belongs to the class
        
        majority_list_copy = majority_list
        
        print("original majority list " + str(majority_list))
        
        #choose a random majority function from the input string
        majority_selection = str(get_random_from_list(majority_list))
        
        while len(majority_selection) == 1 :
            majority_selection = str(get_random_from_list(majority_list)) #If a 1 is chosen then the majority is reselected
            
        print("getrandom from list " + str(majority_selection))
            
        majority_selection = random_section(majority_selection)
        majority_selection_copy = majority_selection
            
        print('majority selection: ', majority_selection)
        
        #choose a random dictionary of values to apply to the string
        dict_selection = get_random_from_list(combinations)
        print('dict_selection: ', dict_selection)
        
        #replace chars with the values from the dict one section at a time while randomising the positions of the chars in the section
        #a control is kept for comparisson so the law of commutativity is preserved
        
        first_char = majority_selection[0]
        last_char = majority_selection[-1]
        
        control_majority = majority_selection
        final_string = majority_selection
        
        replacement_list = []
        count = 2 #count is incremented each time a new innersection is randomised and the number inserted into the string to keep track of location

        while first_char == '⟨' and last_char == '⟩':
            
            print("final string 2: ", final_string)
            
            #randomise the locations of the non-bracket variables
            inner_selection = str(get_inner_bracketed_section(majority_selection))
            control_inner_selection = str(get_inner_bracketed_section(majority_selection))
            final_inner_selection = str(get_inner_bracketed_section(final_string))
            bracketed_inner_selection = "⟨" + inner_selection + "⟩"
            control_bracketed_inner_selection = "⟨" + control_inner_selection + "⟩"
            print("finalinnerselcted", final_inner_selection)
            
            #replace the characters of the strings with the values from the randomised dictionary
            randomised_inner_selection = randomise_string(check_chars(inner_selection, dict_selection))
            random_final_inner_selection = randomise_string(final_inner_selection)
            replaced_inner_selection = check_chars(control_inner_selection, dict_selection)
            print('replaced char string: ', randomised_inner_selection)
            
            majority_of_selection = find_majority_number(randomised_inner_selection) # find the majority number of the 3 bits
            control_majority_of_selection = find_majority_number(replaced_inner_selection)
            print('majority number: ', majority_of_selection)
            
            if bracketed_inner_selection in majority_selection :
                majority_selection = majority_selection.replace(bracketed_inner_selection, majority_of_selection)
                control_majority = control_majority.replace(control_bracketed_inner_selection, control_majority_of_selection)
                
                if count <= 9 :
                    final_string = final_string.replace("⟨" + final_inner_selection + "⟩", str(count))
                    count = count + 1
                    
                elif count > 9 :
                    replacements = {
                    '10': '!',
                    '11': '£',
                    '12': '$',
                    '13': '%',
                    '14': '^',
                    '15': '&',
                    '16': '*',
                    '17': '-',
                    '18': '_',
                    '19': '+',
                    '20': '=',
                    '21': '~',
                    '22': '#',
                    '23': '?',
                    '24': '/',
                    '25': ',',
                    '26': '<',
                    '27': '>',
                    '28': '.',
                    '29': '@'
                    # Add more replacements as needed
                    }
                    
                    final_string = final_string.replace("⟨" + final_inner_selection + "⟩", replacements.get(str(count)))
                    count = count + 1
                
                replacement_list.append("⟨" + random_final_inner_selection + "⟩")
                print("replacement_list :", replacement_list)
                print('new majority function : ', majority_selection)
                print('control majority function : ', control_majority)
                print("final string 1: ", final_string)
                
                first_char = majority_selection[0]
                last_char = majority_selection[-1]
                
        
        replaced_string = ""
        replaced_string = (replace_numbers_with_indices(replacement_list))
        print("replaced_string : ", replaced_string)
        replaced_string = replaced_string[- 1]
        print('replaced_string : ', replaced_string)
        
        if replaced_string != "" :
            print(majority_list_copy)
            print(majority_selection)
            final_majority_list = replace_substring_in_list(majority_list_copy, majority_selection_copy, replaced_string)
            
            # print("replaced majority with commutative law replacement" + str(majority_list))
            return process_string(final_majority_list), True

        else:
            print("string does not obey the law of Commutativity")
            return process_string(majority_list), False