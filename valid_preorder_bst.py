def is_valid_preorder(preorder):
    stack = []
    lower_bound = float('-inf')
    
    for value in preorder:
        if value < lower_bound:
            return False
        
        while stack and value > stack[-1]:
            lower_bound = stack.pop()
        
        stack.append(value)
    
    return True

# Test cases
preorder1 = [5, 2, 1, 3, 6]  
preorder2 = [5, 2, 6, 1, 3]  

print(is_valid_preorder(preorder1))  
print(is_valid_preorder(preorder2)) 
