##Using filter() function with a conditional lambda function (with if else)
listofNum = [1,3,33,12,34,56,11,19,21,34,15]
listofNum = list(filter(lambda x : x > 10 and x < 20, listofNum))
print('Filtered List : ', listofNum)