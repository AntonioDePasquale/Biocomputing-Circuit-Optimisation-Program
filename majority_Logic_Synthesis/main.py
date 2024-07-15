from boolean_expression import BooleanExpression
from majority_expression import MajorityExpression
from simulated_annealing import SimulatedAnnealing
from transformations import *

"""
The main class that is used to instantiate the other classes and organise the program processes
"""
class MainClass :
    
    def __init__(self):
        self.minterms = []
        self.dontcare_terms = []

    def get_integer_list_input(self, prompt):
        while True:
            try:
                input_str = input(prompt)
                input_list = [int(x) for x in input_str.split()]
                return input_list
            except ValueError:
                print("Please enter a valid list of integers.")

    def get_minterms_input(self):
        self.minterms = self.get_integer_list_input("Enter the minterms (space-separated integers): ")

    def get_dontcare_terms_input(self):
        self.dontcare_terms = self.get_integer_list_input("Enter the don't care terms (space-separated integers): ")

    def prompt_user_input(self):
        self.get_minterms_input()
        self.get_dontcare_terms_input()

    def display_terms(self):
        print("Minterms:", self.minterms)
        print("Don't Care Terms:", self.dontcare_terms)
        
    def create_boolean_expression(self):
        boolean_expr = BooleanExpression(self.minterms, self.dontcare_terms)
        return boolean_expr
    

if __name__ == "__main__":
    
    input_handler = MainClass()
    input_handler.prompt_user_input()
    
    boolean_expression = input_handler.create_boolean_expression()
    
    implicant_string = boolean_expression.generate_implicant_string()
    print('Implicant String: ', implicant_string)
    
    minimized_expression = boolean_expression.generate_expression(implicant_string)
    print('Minimized Boolean Expression: ', minimized_expression)
    
    majority_expression_class = MajorityExpression(minimized_expression)
    substituted_expression, majority_expression = majority_expression_class.generate_majority()
    print('majority expression: ', substituted_expression)
    print('working majority: ', majority_expression)
    
    # Instantiate each of the transformation classes
    commutativity_class = Commutativity()
    associativity_class = AssociativityLaw()
    majority_class = MajorityLaw()
    distributivity_class = DistributivityLaw()
    
    # test string for simulated annealing class
    simulated_annealing_test_string = ['⟨⟨⟨⟨JK0⟩H⟨J1K⟩⟩⟨⟨G0V⟩⟨G0⟨⟨q0d⟩⟨q0d⟩j⟩⟩A⟩⟨C⟨⟨b0J⟩0f⟩C⟩⟩⟨1⟨⟨T⟨1f1⟩C⟩F0⟩⟨⟨Q0C⟩⟨Q0C⟩j⟩⟩⟨⟨D0C⟩⟨D0⟨D0C⟩⟩1⟩⟩']
    
    # Instantiate the simulated annealing class and test the simulated_annealing function
    simulated_annealing_class = SimulatedAnnealing(commutativity_class, associativity_class, majority_class, distributivity_class, simulated_annealing_test_string)
    
    simulated_annealing_class.simulated_annealing()
    
    #Testing the 5 law functions
    
    # Example strings for each test case
    example_MajList = ['⟨1⟨A0c⟩⟨b0D⟩⟩'] #breaks under certain conditions
    example_Majority_Law_List = ['⟨C⟨⟨b0J⟩0f⟩C⟩'] #working 1
    example_Associativity_Law_List = ['⟨⟨D0C⟩⟨D0⟨B0c⟩⟩1⟩'] #working 3
    example_Distributivity_Law_List = ['⟨XY⟨UVZ⟩⟩'] #breaks under certain conditions
    example_Distributivity_Law_List2 = ['⟨⟨G0V⟩⟨G0U⟩A⟩'] #working 2
    
    # # Commutativity test
    # majority_expression = commutativity_class.commutativity(exampleMajList)
    # print('commutativity majority expression: ', majority_expression)
    
    # # Associativity test
    # majority_expression = associativity_class.associativity(exampleAssociativityLawList)
    # print('associativity majority expression: ', majority_expression)
    
    # # Majority test
    # majority_expression = majority_class.majority(exampleMajorityLawList)
    # print('associativity majority expression: ', majority_expression)
    
    # # Distributivity depth reduction test
    # majority_expression = distributivity_class.distributivity_depth_reduction(exampleDistributivityLawList)
    # print('distributivity depth reduction majority expression: ', majority_expression)
    
    # # Distributivity size reduction test
    # majority_expression = distributivity_class.distributivity_size_reduction(exampleDistributivityLawList2)
    # print('distributivity size reduction majority expression: ', majority_expression)
    
    