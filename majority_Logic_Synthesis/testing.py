from auxillary_functions import *

# Majority Ω.M
# M(X, Y, Y) = Y; M(X, x, Z ) = Z
def majority(self, majority_list) :
    
    majority_list_copy = majority_list
    
    print("original maj list " + str(majority_list))
    
    #choose a random majority function from the input string
    majority_selection = str(get_random_from_list(majority_list))
    
    while len(majority_selection) == 1 :
        majority_selection = str(get_random_from_list(majority_list)) #If a 1 is chosen then the majority is reselected
        
    print("getrandom from list " + str(majority_selection))
        
    majority_selection = random_section(majority_selection)
    majority_selection_copy = majority_selection
        
    print('majority selection: ', majority_selection)
    
    ##split the majoirty selection lists and then check the majoity law with each of the sections against one another
    def split_majority(majority_selection):
        split_majority = split_sections(majority_selection)
        print('split_sections:', split_majority)
        
        indices_to_remove = []  # List to store indices of sections to be removed
        indices_to_keep = [] # List to store indices of sections that will be kept in the list
        
        for i in range(len(split_majority)):
            for j in range(i + 1, len(split_majority)):
                
                first_balanced_list = find_balanced_sections(split_majority[i])
                print("beforeBalanced1:", first_balanced_list)
                second_balanced_list = find_balanced_sections(split_majority[j])
                print("beforeBalanced2:", second_balanced_list)
                
                modified_sections_1 = ["".join(sorted(remove_brackets(section))) for section in first_balanced_list]
                print("afterBalanced1:", modified_sections_1)
                modified_sections_2 = ["".join(sorted(remove_brackets(section))) for section in second_balanced_list]
                print("afterBalanced2:", modified_sections_2)
                
                
                if modified_sections_1 == modified_sections_2:
                    indices_to_keep.append(j)  # Mark index to be keep
                    
                    #remove all other indices from the list
                    split_majority = [split_majority[index] for index in indices_to_keep]
                    
                    return split_majority
                
                inverted_sorted_sections_1 = ["".join(sorted(remove_brackets(invert_string(section)))) for section in first_balanced_list]
                print("inverted1: ", inverted_sorted_sections_1)
                
                inverted_sorted_sections_2 = ["".join(sorted(remove_brackets(invert_string(section)))) for section in second_balanced_list]
                print("inverted2: ", inverted_sorted_sections_2)
                
                if inverted_sorted_sections_1 == modified_sections_2 or inverted_sorted_sections_2 == modified_sections_1:
                    indices_to_remove.append(i)  # Mark index to be removed
                    indices_to_remove.append(j)  # Mark index to be removed
                    
                    # Remove marked sections in reverse order to avoid shifting issues
                    for index in reversed(indices_to_remove):
                        del split_majority[index]
                        
                    return split_majority
        
        return split_majority

    new_majority_list = split_majority(majority_selection) #new list that has been shortened according to the majority law or unchanged
    
    if len(new_majority_list) == 1 and len(majority_selection_copy) >= 5:
        replaced_string = new_majority_list[0]
        
        final_majority_list = replace_substring_in_list(majority_list_copy, majority_selection_copy, replaced_string)
        return process_string(final_majority_list), True
    
    else :
        print("string does not obey the law of Majority")
        return process_string(majority_list), False
    
# Associativity Ω.A
# M(x, u, M(y, u, z))
# = M(z, u, M(y, u, x))
# = M(y, u, M(z, u, x))

def associativity(self, majority_list):
    
    majority_list_copy = majority_list
    
    print("original maj list " + str(majority_list))
    
    #choose a random majority function from the input string
    majority_selection = str(get_random_from_list(majority_list))
    
    while len(majority_selection) == 1 :
        majority_selection = str(get_random_from_list(majority_list)) #If a 1 is chosen then the majority is reselected
        
    print("getrandom from list " + str(majority_selection))
        
    majority_selection = random_section(majority_selection)
    majority_selection_copy = majority_selection
        
    print('majority selection: ', majority_selection)
    
    ##split the majoirty selection lists and then check the Associativity law with each of the sections against one another
    
    single_swapable_section = []
    swapable_sections = []
    final_majority_string = []
    
    split_majority = split_sections(majority_selection)
    print('split_sections:', split_majority)
    
    #check to see if majority transforamtion needs to happen first
    if has_duplicate(split_majority) :
        print("string section needs to be transformed by the law of majority before associativity")
        
        return process_string(majority_list), False
    
    for i in range(len(split_majority)):
        for j in range(i + 1, len(split_majority)):
            
            first_compare = split_majority[i]
            print('first_compare: ', first_compare)
            second_compare = split_majority[j]
            print('second_compare: ', second_compare)
            
            if first_compare in split_sections(second_compare) and len(split_sections(second_compare)) == 3 :
                print('first_compare in second_compare: ', first_compare, second_compare)
                second_compare_split = split_sections(second_compare)
                print('second_compare_split: ', second_compare_split)
                
                for section in split_majority :
                    if section != first_compare and section != second_compare :
                        single_swapable_section.append(section)
                        print('swapable Section: ', single_swapable_section)
                
                for section in split_sections(second_compare) :
                    if section != first_compare :
                        swapable_sections.append(section)
                        print('swapableAppendedSections: ', swapable_sections)
                        
                chosen_inner_swap = random.choice(swapable_sections)
                print('chosen_inner_swap: ', chosen_inner_swap)
                
                chosen_outer_swap = single_swapable_section[0]
                print('chosen_outer_swap: ', chosen_outer_swap)
                
                new_inner_list = replace_substring_in_list(split_sections(second_compare), chosen_inner_swap, chosen_outer_swap)
                final_inner_string = []
                final_inner_string.append(f"⟨{''.join(new_inner_list)}⟩")
                final_inner_string = process_string(final_inner_string)
                print('final_inner_string: ', final_inner_string)
                
                new_outer_list = replace_substring_in_list(split_majority, chosen_outer_swap, chosen_inner_swap)
                print('new_outer_list: ', new_outer_list)
                
                final_majority_list = replace_substring_in_list(new_outer_list, second_compare, final_inner_string[0])
                print('final_majority_list: ', final_majority_list)
                
                final_majority_string.append(f"⟨{''.join(final_majority_list)}⟩")
                final_majority_string = process_string(final_majority_string)
                print('final_majority_string: ', final_majority_string)
                
            if second_compare in split_sections(first_compare) and len(split_sections(first_compare)) == 3 :
                print('second_compare in first_compare: ', second_compare, first_compare)
                first_compare_split = split_sections(first_compare)
                print('first_compare_split: ', first_compare_split)
                
                for section in split_majority :
                    if section != first_compare and section != second_compare :
                        single_swapable_section.append(section)
                        print('swapable section: ', single_swapable_section)
                
                for section in split_sections(first_compare) :
                    if section != second_compare :
                        swapable_sections.append(section)
                        print('swapable appended sections: ', swapable_sections)
                        
                chosen_inner_swap = random.choice(swapable_sections)
                print('chosen_inner_swap: ', chosen_inner_swap)
                
                chosen_outer_swap = single_swapable_section[0]
                print('chosen_outer_swap: ', chosen_outer_swap)
                
                new_inner_list = replace_substring_in_list(split_sections(first_compare), chosen_inner_swap, chosen_outer_swap)
                final_inner_string = []
                final_inner_string.append(f"⟨{''.join(new_inner_list)}⟩")
                final_inner_string = process_string(final_inner_string)
                print('final_inner_string: ', final_inner_string)
                
                new_outer_list = replace_substring_in_list(split_majority, chosen_outer_swap, chosen_inner_swap)
                print('new_outer_list: ', new_outer_list)
                
                final_majority_list = replace_substring_in_list(new_outer_list, first_compare, final_inner_string[0])
                print('final_majority_list: ', final_majority_list)
                
                final_majority_string.append(f"⟨{''.join(final_majority_list)}⟩")
                final_majority_string = process_string(final_majority_string)
                print('final_majority_string: ', final_majority_string)
                
    if len(final_majority_string) == 1 and final_majority_string[0] != process_string(majority_list)[0] :
        final_majority_list = replace_substring_in_list(majority_list_copy, majority_selection_copy, final_majority_string[0])
        return process_string(final_majority_list), True
    
    else :
        print("string section does not obey the law of Associativity")
        return process_string(majority_list), False
    
# M(x, y, M(u, v, z)) = M(M(x, y, u), M(x, y, v), z)
# Distributivity from right to left enables size reduction
def distributivity_size_reduction(self, majority_list):
    
    final_majority_string = []
    
    majority_list_copy = majority_list
    
    print("original maj list " + str(majority_list))
    
    #choose a random majority function from the input string
    majority_selection = str(get_random_from_list(majority_list))
    
    while len(majority_selection) == 1 :
        majority_selection = str(get_random_from_list(majority_list)) #If a 1 is chosen then the majority is reselected
        
    print("getrandom from list " + str(majority_selection))
        
    majority_selection = random_section(majority_selection)
    majority_selection_copy = majority_selection
        
    print('majority selection: ', majority_selection)
    
    ##split the majoirty selection lists and then check the Distributivity law with each of the sections against one another
    split_majority = split_sections(majority_selection)
    print('split_sections:', split_majority)
    
    removed_section_list = []
    new_list_1 = []
    new_list_2 = []
    new_list_3 = []
    
    for i in range(len(split_majority)):
        for j in range(i + 1, len(split_majority)):
            
            split_list_1 = split_sections(split_majority[i])
            print('split1 : ', split_list_1)
            split_list_2 = split_sections(split_majority[j])
            print('split2 : ', split_list_2)

            if len(split_list_1) >= 3 and len(split_list_2) >= 3 and two_identical_sections(split_list_1, split_list_2) == True :
                new_list_1, new_list_2, removed_section_list = remove_matching_items(split_list_1, split_list_2)
                
                first_removal = process_string([f"⟨{''.join(split_list_1)}⟩"])
                print('first_removal:', first_removal)
                
                second_removal = process_string([f"⟨{''.join(split_list_2)}⟩"])
                print('second_removal:', second_removal)
                
                new_list_3 = split_majority
                print('new_list_3: ', new_list_3)
                new_list_3.remove(first_removal[0])
                print('new_list_3: ', new_list_3)
                new_list_3.remove(second_removal[0])
                print('new_list_3: ', new_list_3)
                break
    
    print('new_list_1: ', new_list_1)
    print('new_list_2: ', new_list_2)
    print('removed_section_list: ', removed_section_list)
        
    distributed_list = process_string([f"⟨{''.join(new_list_1 + new_list_2 + new_list_3)}⟩"])
    print('distributed_list: ', distributed_list)
    
    final_list = process_string([f"⟨{''.join(removed_section_list + distributed_list)}⟩"])
    print('final_list: ', final_list)
    
    if len(final_list) == 1 and final_list[0] != process_string(majority_list)[0] and final_list[0] != '⟨⟩' :
        final_majority_string = replace_substring_in_list(majority_list_copy, majority_selection_copy, final_list[0])
        return process_string(final_majority_string), True
    
    else :
        print("string section does not obey the law of Distributivity")
        return process_string(majority_list), False