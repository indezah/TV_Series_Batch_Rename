import os
print("RNamer - Batch File Renamer by indezah(Nisura Indisa)\n")

print("READY...Press 1 to begin")
in1=str(input())
if in1=="1":
    print("Copy your folder into the into the root and enter its name:")
    oldfolder=input()
    path = oldfolder + "\\"
    season = "01E"
    for filename in os.listdir(path):
        for i in range(1,10):
            if (("("+str(i)[0]+(")")) in filename) or (("_"+str(i)[0]+("_")) in filename):
                old = path + filename
                new = path+("Jujusu Kaisen S" + season + "0"+ str(i)+".mp4")
                os.rename(old,new);
                break
        for i in range(10,25):
            if (("("+str(i)+(")")) in filename) or (("_"+str(i)+("_")) in filename) or ((("Ep"+str(i))) in filename):
                old = path + filename
                new = path+("Jujusu Kaisen S" + season + str(i)+".mp4")
                os.rename(old,new);
                break
else:
    print("Exiting now...")