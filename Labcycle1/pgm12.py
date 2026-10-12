color=[]
n=int(input("enter total number of colors:"))
print("enter colors:")
for i in range(n):
    ch=input()
    color.append(ch)
print(f"First Color is:{color[0]}\n Last color is:{color[-1]}")
