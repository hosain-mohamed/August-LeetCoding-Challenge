x = "USA"
def checkCapital(x : str)-> bool:
    if len(x) < 2 : return True
    if(not x[0].islower() and not x[1].islower()):
        for l in x[2:]:
            if l.islower():
                return False
        else : return True
    else :
        for l in x[1:]:
            if not l.islower():
                return False
        else : return True    
print(checkCapital(x))

challangeLink = 'https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3409/'



