# CSCI 1030U Practice Final Exam - Programming Question #3

def multiplyAllPairs(aList, bList):
    result = []
    for a in aList:
        for b in bList:
            result.append(a*b)
    return result 

list1 = [1,2,3]
list2 = [4,5,6]
print(multiplyAllPairs(list1, list2))
# output: [4, 5, 6, 8, 10, 12, 12, 15, 18]