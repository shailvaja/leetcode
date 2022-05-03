#get 2 combinations from list using recursion
def two_combination(list):
    output = []
    for x in range(len(list)):
        def recurse(x, list):
            if len(list) == 0:
                return 
            output.append([x, list[0]])
            recurse(x, list[1:])    
        recurse(list[x], list[x+1:])
    print(output)
        


two_combination([1,2,3,4,5, 6,7])

