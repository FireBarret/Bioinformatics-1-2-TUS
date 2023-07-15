def fizzbuzz(x):
    for n in range(1,x+1):
        print_value = ''
        if n % 3 == 0: 
            print_value+= 'fizz'
        if n % 5 == 0: 
            print_value+= 'buzz'
        if len(print_value) ==0:
            print_value += str(n)
        print(print_value)
fizzbuzz(100)            

    