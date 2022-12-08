x = 0
y=0
while(True):
   print("Do you want to move the character(yes/no)")
   if input()=="no":
       break
   else:
       print("Where do you want to move character(left,right,top,bottom)")
       str = input()
       if(str == "left"):
           x-=1
           print(x,y,"\n")
       elif (str == "right"):
            x+=1
            print(x,y,"\n")
       else :
            if(str == "top"):
                y+=1
                print(x,y,"\n")
            else:
                y-=1
                print(x,y,"\n")
       