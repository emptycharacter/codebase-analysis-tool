import random  # Unused import


def small_function():
    print("This function is fine.")


def large_function():
    print("This function is too long!")
    for i in range(100):
        print(i)  # Simulating a very large function


def very_complex_function(x):
    if x > 0:
        for i in range(x):
            if i % 2 == 0:
                print(i)
            else:
                if i % 3 == 0:
                    print(f"Divisible by 3: {i}")
                else:
                    for j in range(i):
                        print(j)  # Deep nesting makes it complex
