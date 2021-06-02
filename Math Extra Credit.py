def main():
    print("i Cubed:")
    Google_Sheets_Output(i_cubed())
    print("\n\n(n(n+1)/2)^2:")
    Google_Sheets_Output(n_n_one_squared())
    print("\n\nOne Fifth:")
    Google_Sheets_Output(one_fifth())
    print("\n\nFour Sevenths:")
    Google_Sheets_Output(four_sevenths())
    print("\n\nFibonacci Sequence:")
    Google_Sheets_Output(Fibonacci_Sequence())
    print("\n\nFibonacci Ratio:")
    Google_Sheets_Output(Fibonacci_Ratio(Fibonacci_Sequence()))

def i_cubed():
    i_array = []
    for i in range(1,101):
        if(i != 1):
            i_array.append(i**3 + i_array[i-2])
        else:
            i_array.append(i**3)
    return i_array

def n_n_one_squared():
    n_array = []
    for n in range(1,101):
        n_array.append(int(((n*(n+1))/2)**2))
    return n_array

def one_fifth():
    i_array = []
    for i in range(1,101):
        if(i != 1):
            i_array.append((1/5)**i + i_array[i-2])
        else:
            i_array.append((1/5)**i)
    return i_array

def four_sevenths():
    i_array = []
    for i in range(1,101):
        if(i != 1):
            i_array.append(15*(-4/7)**i + i_array[i-2])
        else:
            i_array.append(15*(-4/7)**i)
    return i_array

def Fibonacci_Sequence():
    fibonacci = [1,1]
    for i in range(98):
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
    return fibonacci

def Fibonacci_Ratio(fibonacci_sequence):
    ratio = []
    for i in range(len(fibonacci_sequence)-1):
        ratio.append(float(fibonacci_sequence[i] / fibonacci_sequence[i+1]))
    return ratio

def Google_Sheets_Output(array):
    for i in range(len(array)):
        print(array[i])
        
if __name__ == "__main__":
    main()
