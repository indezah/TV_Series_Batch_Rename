import os

season = "01E"
for filename in os.listdir("..\Jujutsu Kaisen"):
    for i in range(1,10):
        if (("("+str(i)[0]+(")")) in filename) or (("_"+str(i)[0]+("_")) in filename):
            print("Jujusu Kaisen " + season + "0"+ str(i))
            break
    for i in range(10,25):
        if (("("+str(i)+(")")) in filename) or (("_"+str(i)+("_")) in filename) or ((("Ep"+str(i))) in filename):
            print("Jujusu Kaisen S" + season + str(i))
            break
