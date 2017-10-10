lines = open("input.txt").read().splitlines()
lines2= open("input2.txt").read().splitlines()
for i in range(len(lines)):
    if(lines[i]!=lines2[i]):
        print(str(i+1)+" "+str(lines[i])+" "+str(lines2[i])+ " "+"\n")
