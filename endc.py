import random
from datetime import date
import smtplib,ssl

#Creating My own list of valid charecters 
avc="z!a1y@b2x#c3w$d4ve5u^f6t&g7s*h8ri9qj0p-k_o=l+n|m, Z!A1Y@B2X#C3W$D4VE5U^F6T&G7S*H8RI9QJ0P-K_O=L+N|M, "

class EnDec: #Creates a main class 

    #Now let us create a menu for the user to select if he wants to ENCODE,DECODE or SEND MAILs
    def choice(self):
        
        print("Press 1 to Encode")
        print("Press 2 to decode")
        print("Press 3 to mail")
        print("Press 4 to exit")
        
        c=int(input(""))
        return c
    
    #Function for text input and to check if the enterd charecter is in AVC(valid charecter list which we alredy created)
    def textInput(self):
        
        testing=True
        idx=0           #for indexes in AVC
        
        while testing:
            msg=input("Enter message ")
            
            for i in msg:
                if i in avc:
                    if idx==len(msg)-1: #To check if it is the last charecter of entered msg and exits the loop
                        testing=False
                else:
                    print("Invalid charecter found at index ",msg.index(i))
                    break

                idx+=1 #updates the index of avc   
            return msg
    #fun begins here
    #for encoding a msg
    def encode(self,msg):
        
        enmsg=''
        
        for i in msg:
            
            c=msg[msg.index(i)]                 #extracts the charecter for string
            x=random.randint(1,90)              #genrates a random number 
            ec=avc.index(c)+x                   #locates c in avc and then adds a random number to its index
            
            #Now let us circulate avc so that new index dose not exceeds its length
            if(ec>(len(avc)-1)):
                ec=ec-(len(avc))

            enmsg+=avc[ec]                      #now adding that charecter at new index to encoded string 
        return enmsg

    #Function to decode a string
    def decode(self,msg,pw):
        
        pw=pw-ed.pin()                          #extracts the seed from pin (will discuss the pin in next function)
        random.seed(pw)                         #sets the seed to random function
        demsg=''
        
        for i in msg:
            
            c=msg[msg.index(i)]
            x=random.randint(1,90)              #same patren of random numbers will be genrated as the seed is same
            dc=avc.index(c)-x                   #gets orignal index of ch in avc
            if(dc<0):
                dc=dc+(len(avc))
            demsg+=avc[dc]
        return demsg

    #creates a password for encoded msg
    def pin(self):
        today = str(date.today())
        dt=int(today[-2:])                      #extracts day form today's date
        random.seed(dt)                         #set todays date to be the seed
        pin=random.randint(1111,9800)           #genrates a random 4 digit number
        return pin
    
    def mail (self,enmsg,pin):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = ""  # Enter your address
        receiver_email = input("Enter email adress :")  # Enter receiver address
        password = input("Password : ") # Enter your Password
        message = """\
        Subject: Hi there

        This message is sent from Python 
           """+enmsg+" pin : "+str(pin)+"""\
               
               only valid for today
               """
        print(message)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return receiver_email

ed=EnDec()
c=ed.choice()
ic=0            #to count incorrect choices

#creates a cli menu
while(c!=4):

    msg=ed.textInput()

    #setting up random function for encoding or decoding      
    s=random.randint(1,100)
    random.seed(s)

    if c==1:
        enmsg=ed.encode(msg)
        print(enmsg)
        pin=ed.pin()
        key=s+pin           #creates a password by adding two random numbers
        print ("your key is : ",key)
        c=ed.choice()

    elif c==2:
        pw=int(input("Enter your key to decode "))
        demsg=ed.decode(msg,pw)
        print(demsg)
        c=ed.choice()
    
    elif c==3:
        key=int(input("Enter the key to the msg "))
        rm=ed.mail(msg,key)
        print("Mail Sent to ",rm)
        c=ed.choice()
    else:
        #takes record of incorrect inputs
        ic+=1
        if ic==3:   #exits after 3 incorrect inputs
            c=4
        else:
            c=ed.choice()