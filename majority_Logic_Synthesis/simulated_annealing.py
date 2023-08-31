import random
import math
from transformations import *

class SimulatedAnnealing:

    def __init__(self, commutativity_class, associativity_class, majority_class, distributivity_class, initial_string):
        self.commutativity_class = commutativity_class
        self.majority_class = majority_class
        self.associativity_class = associativity_class
        self.distributivity_class = distributivity_class
        self.initial_string = initial_string
        
        self.modification_functions = [
        self.majority_class.majority,
        self.distributivity_class.distributivity_size_reduction,
        self.associativity_class.associativity,
        ]
        self.initial_temperature = 10.0
        self.cooling_rate = 0.995
        self.iterations = 1000
        

    def simulated_annealing(self):
        current_solution = self.initial_string
        best_solution = current_solution
        current_length = len(current_solution[0])
        best_length = current_length
        temperature = self.initial_temperature  # Move temperature initialization outside the loop
        
        print('initial string: ', current_solution)

        for _ in range(self.iterations):
            selected_function = random.choice(self.modification_functions)
            new_solution = selected_function(current_solution)
            changes_made = new_solution[1]
            print('changes made: ', changes_made)

            if changes_made:
                new_length = len((new_solution[0])[0])
                acceptance_prob = math.exp((current_length - new_length) / temperature)
                
                if new_length <= current_length or random.random() < acceptance_prob:
                    current_solution = new_solution[0]
                    current_length = new_length
                    
                    if new_length <= best_length:
                        best_solution = new_solution[0]
                        best_length = new_length
            
            temperature *= self.cooling_rate  # Move temperature cooling outside the loop
        
        print('original string: ', self.initial_string, ' | original length: ', len(self.initial_string[0]))
        print('best solution: ', best_solution, ' | current length: ', current_length, ' | best length: ', best_length)
        return best_solution