banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("fileques3.txt","w")
# f.writelines(banks_list)
# f.close()

for i in banks_list:
    f.write(i)
    f.write("\n")
    