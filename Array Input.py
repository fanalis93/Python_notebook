## Breakline will take the element or series of elementts as list
# Method 1
array=list(map(int,input().split()))
print(array)

#or 
s = [int(x) for x in input().split()]


# Method 2
array = []
inp=input().split()
for i in inp:
	array.append(int(i))
print(array)

## Take input until range while breaking line after each input
n = 6 #number of elements
array = [int(input()) for i in range(n)]
print(array)