from auxillary_functions import *

class MajorityLaw :
    
    # Majority Ω.M
    # M(X, Y, Y) = Y; M(X, x, Z ) = Z
    def majority(self, majority_list) :
        
        majority_list_copy = majority_list
        
        #choose a random majority function from the input string
        majority_selection = str(get_random_from_list(majority_list))
        
        while len(majority_selection) == 1 :
            majority_selection = str(get_random_from_list(majority_list)) #If a 1 is chosen then the majority is reselected
            
        majority_selection = random_section(majority_selection)
        majority_selection_copy = majority_selection
        
        ##split the majoirty selection lists and then check the majoity law with each of the sections against one another
        def split_majority(majority_selection):
            split_majority = split_sections(majority_selection)
            
            indices_to_remove = []  # List to store indices of sections to be removed
            indices_to_keep = [] # List to store indices of sections that will be kept in the list
            
            for i in range(len(split_majority)):
                for j in range(i + 1, len(split_majority)):
                    
                    first_balanced_list = find_balanced_sections(split_majority[i])
                    second_balanced_list = find_balanced_sections(split_majority[j])
                    
                    modified_sections_1 = ["".join(sorted(remove_brackets(section))) for section in first_balanced_list]
                    modified_sections_2 = ["".join(sorted(remove_brackets(section))) for section in second_balanced_list]
                    
                    
                    if modified_sections_1 == modified_sections_2:
                        indices_to_keep.append(j)  # Mark index to be keep
                        
                        #remove all other indices from the list
                        split_majority = [split_majority[index] for index in indices_to_keep]
                        
                        return split_majority
                    
                    inverted_sorted_sections_1 = ["".join(sorted(remove_brackets(invert_string(section)))) for section in first_balanced_list]
                    
                    inverted_sorted_sections_2 = ["".join(sorted(remove_brackets(invert_string(section)))) for section in second_balanced_list]
                    
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
            print("string does obey the law of Majority")
            return process_string(final_majority_list), True
        
        else :
            #print("string does not obey the law of Majority")
            return process_string(majority_list), False