from auxillary_functions import *

"""
The function for the associativity transformation as outlined below that is used in the optimisation of majority logic.

# Associativity Ω.A
    # M(x, u, M(y, u, z))
    # = M(z, u, M(y, u, x))
    # = M(y, u, M(z, u, x))

The rule of associativity demonstrates that the order in which the majority function is applied can be rearranged without altering the result 
if both the outer and inner majority functions share a variable (in this case u is shared).
This rule showcases how a majority function within a majority function can be reshaped, emphasizing the flexible nature of majority logic.
"""

class AssociativityLaw :
    
    # Associativity Ω.A
    # M(x, u, M(y, u, z))
    # = M(z, u, M(y, u, x))
    # = M(y, u, M(z, u, x))

    def associativity(self, majority_list):
        
        majority_list_copy = majority_list
        
        #choose a random majority function from the input string
        majority_selection = str(get_random_from_list(majority_list))
        
        while len(majority_selection) == 1 :
            majority_selection = str(get_random_from_list(majority_list)) #If a 1 is chosen then the majority is reselected
            
        majority_selection = random_section(majority_selection)
        majority_selection_copy = majority_selection
        
        ##split the majoirty selection lists and then check the Associativity law with each of the sections against one another
        
        single_swapable_section = []
        swapable_sections = []
        final_majority_string = []
        
        split_majority = split_sections(majority_selection)
        
        #check to see if majority transforamtion needs to happen first
        if has_duplicate(split_majority) :
            print("string section needs to be transformed by the law of majority before associativity")
            
            return process_string(majority_list), False
        
        for i in range(len(split_majority)):
            for j in range(i + 1, len(split_majority)):
                
                first_compare = split_majority[i]
                second_compare = split_majority[j]
                
                if first_compare in split_sections(second_compare) and len(split_sections(second_compare)) == 3 :
                    
                    for section in split_majority :
                        if section != first_compare and section != second_compare :
                            single_swapable_section.append(section)
                    
                    for section in split_sections(second_compare) :
                        if section != first_compare :
                            swapable_sections.append(section)
                            
                    chosen_inner_swap = random.choice(swapable_sections)
                    
                    chosen_outer_swap = single_swapable_section[0]
                    
                    new_inner_list = replace_substring_in_list(split_sections(second_compare), chosen_inner_swap, chosen_outer_swap)
                    final_inner_string = []
                    final_inner_string.append(f"⟨{''.join(new_inner_list)}⟩")
                    final_inner_string = process_string(final_inner_string)
                    
                    new_outer_list = replace_substring_in_list(split_majority, chosen_outer_swap, chosen_inner_swap)
                    
                    final_majority_list = replace_substring_in_list(new_outer_list, second_compare, final_inner_string[0])
                    
                    final_majority_string.append(f"⟨{''.join(final_majority_list)}⟩")
                    final_majority_string = process_string(final_majority_string)
                    
                if second_compare in split_sections(first_compare) and len(split_sections(first_compare)) == 3 :
                    
                    for section in split_majority :
                        if section != first_compare and section != second_compare :
                            single_swapable_section.append(section)
                    
                    for section in split_sections(first_compare) :
                        if section != second_compare :
                            swapable_sections.append(section)
                            
                    chosen_inner_swap = random.choice(swapable_sections)
                    
                    chosen_outer_swap = single_swapable_section[0]
                    
                    new_inner_list = replace_substring_in_list(split_sections(first_compare), chosen_inner_swap, chosen_outer_swap)
                    final_inner_string = []
                    final_inner_string.append(f"⟨{''.join(new_inner_list)}⟩")
                    final_inner_string = process_string(final_inner_string)
                    
                    new_outer_list = replace_substring_in_list(split_majority, chosen_outer_swap, chosen_inner_swap)
                    
                    final_majority_list = replace_substring_in_list(new_outer_list, first_compare, final_inner_string[0])
                    
                    final_majority_string.append(f"⟨{''.join(final_majority_list)}⟩")
                    final_majority_string = process_string(final_majority_string)
                    
        if len(final_majority_string) == 1 and final_majority_string[0] != process_string(majority_list)[0] :
            final_majority_list = replace_substring_in_list(majority_list_copy, majority_selection_copy, final_majority_string[0])
            print("string section does obey the law of Associativity")
            return process_string(final_majority_list), True
        
        
        else :
            #print("string section does not obey the law of Associativity")
            return process_string(majority_list), False