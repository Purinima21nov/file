f=open("people1-exercise.txt","w")
f.writelines(["rishabh - meerut\n",
"imtiyaz - delhi\n",
"nilima - cochin\n",
"rati - shimla\n",
"ayishah - delhi\n",
"raghu - shimla\n",
"naseer - kanpur\n",
"karthikeyan - delhi\n",
"salma - jaipur\n",
"deepti - shimla\n"])
f.close()
k=open("people1-exercise.txt","r")
count=0
for i in k:
    count=count+1
print(count)    
k.close()
