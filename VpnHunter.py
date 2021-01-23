import glob
import re
import ipinfo

def ip4(ip):
    f = open("vpn-ipv4.txt","r")
    #print(ip)
    #f=open("a.txt",'r')
    x = f.readline()
    x = f.readline()
    while True:
        x = f.readline().rstrip('\n')
       # print(x)
        if not x:
            break
        if str(x) == str(ip):
            #print("found")
            return 1
        t = 0 
        m=0
        ##print(x)
        for z in range(len(x)):
            #print(".")
            
            if x[z] ==".":
                m=1+m
            if (m ==3 and x[:t] == ip[:t]):
               # print(x[:z])
                if(x[z-1]=="."):
                    t= z-1
                if (x[z]=="/"):
                   # print(x[:z])
                    if(ip[t+1:] >= x[t+1:z] and ip[t+1:] <= x[z+1:]):
                        #print(x[t+1:z],x[z+1:],ip[t+1:])
                        return 1 , "Found in VPN database"
                    else:
                        break
                
            if(x[:z]!= ip[:z]):
                break
        ##print("............")
    return 0 , "Not Found in VPN database"

#print(ip4("2.56.92.29"))            


def apnsearch(apn , filex):
    f = open(filex,"r")
    while True:
        x = f.readline().rstrip('\n')
        if not x:
            break
        if(x == apn):
            return 1
    return 0


def asn(asp):
    flocation = "asn"
    description = None
    if(asp.isdigit()== False):
        return -1 , "Invald ASN"
    for i in glob.glob("asn/*.txt"):
        if(apnsearch(asp,i) == 1):
            description = "This APN is Malacious  Found In " +(i[len(flocation)+1 : -4]) + " Database"
            return 1 , description

def asnFind(asp):
    access_token = 'ce25dd1fca9a9b' #9c47a5274b06eb

    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(asp)
    x=details.org.split(" ")
    x= x[0][2:]
    print(x)
    return x


def check(Ip):  
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex, Ip)):  
        #print(Ip) 
        return 0
    else:
        return 1
