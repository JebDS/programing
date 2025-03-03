n=int(input())
for i in range(n, 1, -1):
    print(str(i), "bottles of beer on the wall,", str(i), "bottles of beer.")
    if i>2:
        print("Take one down and pass it around,", str(i-1), "bottles of beer on the wall."+'\n')
    else: print("Take one down and pass it around,", str(i-1), "bottle of beer on the wall."+'\n')

print("1 bottle of beer on the wall, 1 bottle of beer.")
print("Take one down and pass it around, no more bottles of beer on the wall.")
print()
print("No more bottles of beer on the wall, no more bottles of beer.")
if n==1: print("Go to the store and buy some more,", str(n), "bottle of beer on the wall.")
else: print("Go to the store and buy some more,", str(n), "bottles of beer on the wall.")