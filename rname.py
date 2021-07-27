import os
path = "..\Jujutsu Kaisen\\"
newpath ="JujutsuKaisenRNamed\\"
season = "01E"
for filename in os.listdir(path):
    for i in range(1,10):
        if (("("+str(i)[0]+(")")) in filename) or (("_"+str(i)[0]+("_")) in filename):
            old = path + filename
            new = newpath+("Jujusu Kaisen S" + season + "0"+ str(i)+".mp4")
            os.rename(old,new);
            break
    for i in range(10,25):
        if (("("+str(i)+(")")) in filename) or (("_"+str(i)+("_")) in filename) or ((("Ep"+str(i))) in filename):
            old = path + filename
            new = newpath+("Jujusu Kaisen S" + season + str(i)+".mp4")
            os.rename(old,new);
            break