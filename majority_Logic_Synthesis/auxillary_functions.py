import transformations
import re
import itertools
import random

#removes the outer brackets surrounding a string
def remove_brackets(string):
    if len(string) < 2:
        return string

    first_char = string[0]
    last_char = string[-1]

    if first_char == '⟨' and last_char == '⟩':
        return string[1:-1]
    else:
        return string

#code to select the inner bracketed section of a string
def get_inner_bracketed_section(input_string):
    stack = []
    inner_sections = {}
    for i, char in enumerate(input_string):
        if char == '⟨':
            stack.append(i)
        elif char == '⟩':
            if stack:
                start = stack.pop()
                inner_sections[start] = input_string[start + 1:i]
            else:
                raise ValueError("Unbalanced brackets in the input string.")
    if stack:
        raise ValueError("Unbalanced brackets in the input string.")
    
    innermost_start = max(inner_sections.keys())
    return inner_sections[innermost_start]


#finds each inner bracketed section of the input string and adds them to a list
def find_balanced_sections(input_string):
    sections = []
    start = input_string.find("⟨")
    while start != -1:
        depth = 1
        end = start + 1
        while depth > 0 and end < len(input_string):
            if input_string[end] == "⟨":
                depth += 1
            elif input_string[end] == "⟩":
                depth -= 1
            end += 1

        if depth == 0:  # If we found a balanced pair
            sections.append(input_string[start:end])
        
        # Continue searching for the next pair
        start = input_string.find("⟨", start + 1)

    return sections


#finds a randomised section from the list of sections
def random_section(input_string):
    sections = find_balanced_sections(input_string)
    if not sections:
        return ""

    return random.choice(sections)


#function to select randomly from a list
#use random.randint() to get a random index number
def get_random_from_list(list) :
    rand_index = random.randint(0, len(list)-1)
    random_item = list[rand_index]
    
    return random_item


#function to check the chars of a string against the dict
def check_chars(input_string, combinations):
    result = ""
    for char in input_string:
        if char in combinations:
            result += str(combinations[char] ^ (not char.isupper()))  # Flipping the bit for lowercase characters
        elif char.upper() in combinations:
            result += str(combinations[char.upper()] ^ 1)  # Flip the bit for the uppercase version
        else:
            result += char

    return result


def find_majority_number(string):
    # Count the occurrences of 0 and 1 in the string
    count0 = string.count('0')
    count1 = string.count('1')

    # Return the majority number based on the counts
    if count0 > count1:
        return '0'
    elif count1 > count0:
        return '1'
    
                
#function to randomise the locations of chars in a 3 char string
def randomise_string(string):
    
    # Convert the string to a list to shuffle its characters
    char_list = list(string)
    
    # Randomly shuffle the characters
    randomised_chars = random.sample(char_list, len(char_list))
    
    # Convert the list back to a string
    randomised_string = "".join(randomised_chars)
    return randomised_string

            
# function that replaces chars 3-9 in a string with the index in the list which is that number -2
# eg 3 in a string will be replaced by index 1 in the list
def replace_numbers_with_indices(lst):
    
    replacements = {
    '!': '10',
    '£': '11',
    '$': '12',
    '%': '13',
    '^': '14',
    '&': '15',
    '*': '16',
    '-': '17',
    '_': '18',
    '+': '19',
    '=': '20',
    '~': '21',
    '#': '22',
    '?': '23',
    '/': '24',
    ',': '25',
    '<': '26',
    '>': '27',
    '.': '28',
    '@': '29'
}
     
    for i, string in enumerate(lst):
        count = i + 1
        print("count:", count)
        
        for j, char in enumerate(string):
                
            if char.isdigit() and '2' <= char <= '9':
                lst[i] = lst[i].replace(char, lst[int(char) - 2])
                print("Replaced " + str(i) + " : " + lst[i])
                
            if char == '!' or char == '£' or char == '$' or char == '%' or char == '^' or char == '&' or char == '*' or char == '-' or char == '_' or char == '+' or char == '=' :
                lst[i] = lst[i].replace(char, lst[int(replacements.get(char)) - 2])
                print("Replaced " + str(i) + " : " + lst[i])
                
    return lst


#checks the items in a list then matches a substring to replace it with a modified version of that string
def replace_substring_in_list(lst, old_substring, new_substring):
    new_list = []
    for item in lst:
        if old_substring in item:
            modified_item = item.replace(old_substring, new_substring)
            new_list.append(modified_item)
        else:
            new_list.append(item)
    return new_list


#funtion that splits a string into its constituent parts that make up the majority string
def split_sections(input_str):
    input_str = remove_brackets(input_str)
    sections = []
    current_section = ""
    bracket_depth = 0

    for char in input_str:
        if char == '⟨':
            if bracket_depth >= 1:
                current_section += char
            bracket_depth += 1
        elif char == '⟩':
            bracket_depth -= 1
            if bracket_depth == 0:
                sections.append(current_section)
                current_section = ""
            else:
                current_section += char
        else:
            if bracket_depth >= 1:
                current_section += char
            else:
                sections.append(char)
                
    for i, section in enumerate(sections):
        if len(section) >= 1:     #may have to change to 3
            sections[i] = '⟨' + section + '⟩'

    return sections


#function that inverts a string, 1 becomes 0, lowercase becomes uppercase and vice versa
def invert_string(input_str):
    result = []
    invert_dict = {'0': '1', '1': '0'}

    for char in input_str:
        if char.isalpha():
            if char.islower():
                result.append(char.upper())
            elif char.isupper():
                result.append(char.lower())
        elif char in invert_dict:
            result.append(invert_dict[char])
        else:
            result.append(char)

    return ''.join(result)


#function that removes brackets surrounding single chars
def process_string(input_list):
    input_str = input_list[0]
    output = []
    i = 0

    while i < len(input_str):
        if i + 2 < len(input_str):
            section = input_str[i:i+3]

            if section[0] == '⟨' and section[2] == '⟩':
                output.append(section[1])
                i += 3
            else:
                output.append(section[0])
                i += 1
        else:
            output.append(input_str[i])
            i += 1

    return [''.join(output)]


# function that checks two lists to see if they have two macthing items in both lists then removes them, removed ites are added to thier own list
def remove_matching_items(list1, list2):
        removed_chars = []
        temp_list1 = list1.copy()
        temp_list2 = list2.copy()

        for item1 in list1:
            if item1 in temp_list2:
                removed_chars.append(item1)
                temp_list1.remove(item1)
                temp_list2.remove(item1)

        return temp_list1, temp_list2, removed_chars
    

#function that checks two lists to see if they have two macthing items in each list and returns True if so, False otherwise    
def two_identical_sections(list1, list2):
    identical_count = 0

    for item1 in list1:
        if item1 in list2:
            identical_count += 1
            if identical_count > 2:
                return False

    return identical_count == 2

#function that checks a single list to see if there are any duplicates returning True if so, False otherwise
def has_duplicate(list):
    seen = set()
    
    for item in list:
        if item in seen:
            return True
        seen.add(item)
        
    return False

# Function to reconstruct a list of balanced sections that were created from the find_balanced_sections function
def reconstruct_balanced_sections(full_string, replacement_string, replacement_index):
    first_char = full_string[0]
    last_char = full_string[-1]
    
    replacement_list = []
    count = 2 #count is incremented each time a new innersection is randomised and the number inserted into the string to keep track of location
    
    
    while first_char == '⟨' and last_char == '⟩':
        final_string = full_string
        final_inner_selection = str(get_inner_bracketed_section(final_string))
    
        if count <= 9 :
                final_string = final_string.replace("⟨" + final_inner_selection + "⟩", str(count))
                count = count + 1
                print('final_string, what is going on 1 : ' + final_string)
                
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
            print('final_string, really wtf... : ' + final_string)
            count = count + 1
        
        replacement_list.append("⟨" + final_inner_selection + "⟩")
        print("replacement_list :", replacement_list)
        
        first_char = full_string[0]
        last_char = full_string[-1]
        
    replaced_string = ""
    replaced_string = (replace_numbers_with_indices(replacement_list))
    print("replaced_string : ", replaced_string)
    replaced_string = replaced_string[- 1]
    print('replaced_string : ', replaced_string)







