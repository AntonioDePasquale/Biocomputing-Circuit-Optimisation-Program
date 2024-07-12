from quine_mccluskey.qm import QuineMcCluskey

class BooleanExpression:

    """
    The first step of the process.
    1.  Minimisation with the Quine-McCluskey Algorithm to get a boolean expression:
    This class involves finding all the prime implicants of a function and using the Quine McCluskey algorithm to find the essential prime implicants.
    This results in a minimised version of the original Boolean function.
    """

    #constructor for BooleanExpression which takes two lists of integers for the minimum terms and dont care terms
    def __init__(self, min_terms, max_terms):
        self.min_terms = min_terms
        self.max_terms = max_terms
        
    # Uses the QuineMcCluskey class simplify function to generate a string of prime implicants
    def generate_implicant_string(self):
        # Instantiates the QuineMcCluskey class
        qm = QuineMcCluskey()

        # Takes a list of min terms and dont care terms, returning the extracted prime implicants
        qm_implicants = qm.simplify(self.min_terms, self.max_terms)
        
        return qm_implicants
        
    # Takes a simplified string of prime implicants returned from the simplify function and returns a minimal Quine-McCluskey expression
    def generate_expression(self, implicant_string):
        variables = set()
        expressions = []

        for implicant_string in implicant_string:
            expression = []
            for i, char in enumerate(implicant_string):
                
                if char == '1':
                    expression.append(chr(65 + i))  # Convert index to variable (A, B, C, ...)
                    variables.add(chr(65 + i))
                    
                if char == '-':
                    i = i + 1
                    
                elif char == '0':
                    expression.append(chr(65 + i) + "'")  # Convert index to NOT variable (A', B', C', ...)
                    variables.add(chr(65 + i))

            expressions.append(" AND ".join(expression))  # Join the expressions with the "AND" operator

        return " OR ".join(expressions)  # Join the expressions with "OR" operator
    
    