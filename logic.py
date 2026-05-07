import math
import sys
import math
import re


class Calculator:
    def __init__(self):
        self.priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        
        self.functions = {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "exp": math.exp, "log": math.log, "sqrt": math.sqrt
        }

    def _get_precedence(self, a):
        return self.priority.get(a, 0)

    def _tokenize(self, expression):
        return re.findall(r'\d+\.?\d*|[a-z]+|[\+\-\*\/\(\)\^]', expression.lower())

    def NPI(self, expression):
        stock = []
        res = []
        tokens = self._tokenize(expression)

        for token in tokens:
            if token.replace('.', '', 1).isdigit():
                res.append(token)
            
            elif token in self.functions:
                stock.append(token)
                
            elif token == "(":
                stock.append(token)
            elif token == ")":
                while stock and stock[-1] != "(":
                    res.append(stock.pop())

                if not stock: return "Error" 
                stock.pop() 

                if stock and stock[-1] in self.functions:
                    res.append(stock.pop())

            elif token in self.priority:
                while (stock and stock[-1] != "(" and 
                       self._get_precedence(stock[-1]) >= self._get_precedence(token)):
                    res.append(stock.pop())
                stock.append(token)

        while stock:
            if stock[-1] == "(": return "Error"
            res.append(stock.pop())
        return res

    def resultat(self, rpn_tokens):
        if rpn_tokens == "Error": return "Error"
        stack_values = []
        
        try:
            for token in rpn_tokens:
                if token.replace('.', '', 1).isdigit():
                    stack_values.append(float(token))

                elif token in self.functions:
                    val = stack_values.pop()
                    stack_values.append(self.functions[token](val))
                    
                elif token in self.priority:
                    b = stack_values.pop()
                    a = stack_values.pop()

                    if token == '+': stack_values.append(a + b)
                    elif token == '-': stack_values.append(a - b)
                    elif token == '*': stack_values.append(a * b)
                    elif token == '/': stack_values.append(a / b)
                    elif token == '^': stack_values.append(a ** b)
            
            return stack_values[0] if stack_values else 0
        except Exception:
            return "Error"

    def interface(self, expression):
        rpn = self.NPI(expression)
        result = self.resultat(rpn)
        
        if result == "Error":
            sys.stderr.write("Invalid Expression\n")
            return "Error"
        return result
