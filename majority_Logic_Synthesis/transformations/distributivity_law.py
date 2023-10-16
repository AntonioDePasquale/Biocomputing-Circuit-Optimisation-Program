from auxillary_functions import *

class DistributivityLaw :
    
    # Distributivity Ω.D
    # M(x, y, M(u, v, z)) = M(M(x, y, u), M(x, y, v), z)
    # Distributivity from left to right enables depth reduction
    def distributivity_depth_reduction(self, majority_list):
        
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
        
        sections_to_distribute = []
        other_sections = []
        final_sections_list = []
        
        for i in range(len(split_majority)):
                
            if len(split_majority[i]) > 3 :
                sections_to_distribute.append(split_majority[i])
                
        chosen_distribution = ''
        if len(sections_to_distribute) > 0 :
            chosen_distribution = random.choice(sections_to_distribute)
            print('chosen_inner_swap: ', chosen_distribution)
        
        if chosen_distribution != '' :
            for section in split_majority :
                if section != chosen_distribution :
                    other_sections.append(section)
                    
            print('sectionToDistribute: ', chosen_distribution)
            print('other_sections: ', other_sections)
            
            split_distribution = split_sections(chosen_distribution)
            print('split_distribution: ', split_distribution)
            
            selected_items = random.sample(split_distribution, 2)
            print('selected_items: ', selected_items)
            
            remaining_item = [item for item in split_distribution if item not in selected_items][0]
            print('remaining_item: ', remaining_item)

            other_section_string = []
            other_section_string.append(f"⟨{''.join(other_sections)}⟩")
            print('other_section_string: ', other_section_string)
            other_sections_string = remove_brackets(process_string(other_section_string)[0])
            print('other_sections_string: ', other_sections_string)
            
            for section in selected_items :
                if len(section) <= 3 :
                    new_section = '⟨' + remove_brackets(section) + other_sections_string + '⟩'
                    final_sections_list.append(new_section)
                
                else :
                    new_section = '⟨' + section + other_sections_string + '⟩'
                    final_sections_list.append(new_section)
                
            final_sections_list.append(remaining_item)
            print('final_sections_list: ', final_sections_list)
            
            final_majority_string.append(f"⟨{''.join(final_sections_list)}⟩")
            print('final_majority_string: ', final_majority_string)
            
        if len(final_majority_string) == 1 and final_majority_string[0] != process_string(majority_list)[0] :
            final_majority_string = replace_substring_in_list(majority_list_copy, majority_selection_copy, final_majority_string[0])
            return process_string(final_majority_string), True
        
        else :
            #print("string section does not obey the law of Distributivity")
            return process_string(majority_list_copy), False
        
    # M(x, y, M(u, v, z)) = M(M(x, y, u), M(x, y, v), z)
    # Distributivity from right to left enables size reduction
    def distributivity_size_reduction(self, majority_list):
        
        final_majority_string = []
        
        majority_list_copy = majority_list
        
        #choose a random majority function from the input string
        majority_selection = str(get_random_from_list(majority_list))
        
        while len(majority_selection) == 1 :
            majority_selection = str(get_random_from_list(majority_list)) #If a 1 is chosen then the majority is reselected
            
        majority_selection = random_section(majority_selection)
        majority_selection_copy = majority_selection
        
        ##split the majoirty selection lists and then check the Distributivity law with each of the sections against one another
        split_majority = split_sections(majority_selection)
        
        removed_section_list = []
        new_list_1 = []
        new_list_2 = []
        new_list_3 = []
        
        for i in range(len(split_majority)):
            for j in range(i + 1, len(split_majority)):
                
                split_list_1 = split_sections(split_majority[i])
                split_list_2 = split_sections(split_majority[j])
    
                if len(split_list_1) >= 3 and len(split_list_2) >= 3 and two_identical_sections(split_list_1, split_list_2) == True :
                    new_list_1, new_list_2, removed_section_list = remove_matching_items(split_list_1, split_list_2)
                    
                    first_removal = process_string([f"⟨{''.join(split_list_1)}⟩"])
                    
                    second_removal = process_string([f"⟨{''.join(split_list_2)}⟩"])
                    
                    new_list_3 = split_majority
                    new_list_3.remove(first_removal[0])
                    new_list_3.remove(second_removal[0])
                    break
            
        distributed_list = process_string([f"⟨{''.join(new_list_1 + new_list_2 + new_list_3)}⟩"])
        
        final_list = process_string([f"⟨{''.join(removed_section_list + distributed_list)}⟩"])
        
        if len(final_list) == 1 and final_list[0] != process_string(majority_list)[0] and final_list[0] != '⟨⟩' :
            final_majority_string = replace_substring_in_list(majority_list_copy, majority_selection_copy, final_list[0])
            print("string section does obey the law of Distributivity")
            return process_string(final_majority_string), True
        
        else :
            #print("string section does not obey the law of Distributivity")
            return process_string(majority_list), False
        
                