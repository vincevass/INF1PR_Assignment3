#INF1PR Subtask8.1
def find_largest_square(n):
    
    m = 0
    
    while (m + 1)**2 <= n:
        m = m + 1
        
    q = m**2
    return q


userInput = int(input("Enter a natural number n ≥ 0: "))
    
if userInput >= 0:
        result = find_largest_square(userInput)
        
        print(f"The largest square number less than or equal to {userInput} is: {result}")
else:
     print("An error has occured...")

# it looks like I learned how to use git today

