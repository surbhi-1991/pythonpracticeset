p1= "Make a lot of money" 
p2= "buy now"
p3= "subscribe thi"
p4= "click this"

message= input("Enter your comments:")

if((p1 in message) or(p2 in message) or(p3 in message) or(p4 in message)):
    print("Enter comment is spam")
else:
    print("This comment is not spam")