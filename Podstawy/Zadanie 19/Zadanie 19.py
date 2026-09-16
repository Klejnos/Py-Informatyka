import os;x=33;i=0
while x<255:
    print("kod znaku",x,"\t",chr(x),"\t\t","kod znaku",x+1,"\t",chr(x+1),"\t\t","kod znaku",x+2,"\t",chr(x+2));x+=3;i+=1
    if i==20:input("Naciśnij Enter, aby kontynuować...");os.system("cls");i=0