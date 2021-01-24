import glob
import re
import os
import ipinfo

def ip4(ip):
    if(check(ip) == 0):
        return -1, "Invalid  Data Inserted"
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
            return (1 , "Found in VPN database")
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
                        return (1 , "Found in VPN database")
                    else:
                        break
                
            if(x[:z]!= ip[:z]):
                break
        ##print("............")
        
    d , y = ip4Local(ip)
    return (d , y)



def ip4LocalAdd(ip):
    
    f = open("vpn-ipv4Local.txt","a+")
    f.write(ip)
    f.write("\n") #adding new line character 
    print("%s Added to the ip database"%ip)
    f.close()
 
    
    
def ip4Local(ip):
    if os.path.exists("vpn-ipv4Local.txt"):
        f = open("vpn-ipv4Local.txt","r")
        while True:
            x = f.readline().rstrip('\n')
            if not x:
                break
            if str(x) == str(ip):
                return (1 , "Found in Local Custom VPN database")
    return (0 , "Not Found in Local VPN database")
    
            


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
    else:
        return 0 , "IP is Not using VPN"

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
        return 1
    else:
        return 0

#TODO
        #Postgress server for  Centralised database 
        #optimise false positives 
        #recheck from diffrent api 
        #refine result 
        
        