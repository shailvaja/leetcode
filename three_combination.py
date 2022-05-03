#get 3 combinations from list using recursion
def three_combination(list):
    output = []
    def recurse(x,y , list):
                if len(list) == 0:
                    return 
                output.append([x,y, list[0]])
                recurse(x, y, list[1:])
    for x in range(len(list)):
        for y in range(x+1,len(list)):
                
            recurse(list[x], list[y], list[y+1:])
    print(output)
        


three_combination([1,2,3,4,5, 6,7])