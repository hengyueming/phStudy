print("hello world")

x = 3
y = 5

print(x + y)

answer = "you are the best"

print(y , answer)

if y > 0 :
    print(answer + "+++the number is", y)
    y -= 1
else:
    print(y + "the truth");

while x > 0:
    print("x going down :", x)
    x -= 1;


arrays =[1,2,3,4]
index = [0,1,1,0]
new_array = []
new_array1 = []
sums = 0

for i in range(0, len(arrays)):
    sums += arrays[i]
    new_array.append(sums)

print(new_array)


for u in range(0,len(index)):
    new_array1.insert(index[u],arrays[u])

print(new_array1)