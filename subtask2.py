#INF1PR Subtask8.2
def process_sequence():
    n = 0
    s = 0
    m = 0
    a = 0

    print("Enter natural numbers one by one (enter -1 to finish)")

    while True:
        try:
            # "read x"
            x_input = input(f"Enter a number (current count {n}): ")
            x = int(x_input)
            
            if x == -1:
                break
            
            if n == 0:

                m = x
            else:

                if x < m:
                    m = x
            

            s = s + x
            n = n + 1
            
        except ValueError:
            print("Please enter a valid integer.")

    if n == 0:
        m = -1
        a = -1
    else:

        a = s / n

    print("-" * 20)
    print(f"Count (n): {n}")
    print(f"Sum (s):   {s}")
    print(f"Min (m):   {m}")
    print(f"Mean (a):  {a}")

if __name__ == "__main__":
    process_sequence()

    # it looks like I learned how to use git today