# VpnHunter
Hashcode 2020 Hackathon  -- Team -- Genesys V1

## INTRODUCTION

There is no proper way for Detection of *VPN*  with 100% accuracy using methods such as Port scanning Pinging. <br>
Hence rather than using this traditional approach this program relays on finding data consisting of known IP's used by VPN providers in colabration with another curcial  parameters such as ASN records to predict the chance of a IP being used a VPN . <br>
*Our Aim is to create a dynamic database of IP’s that are used by VPN Providers and then block them by linking the database to our network router and blocking any traffic associated with these ips* .<br>

In order make it effective , we would create a system that would add IP’s to this database based on different parameters such as ISP , Hostname and suspicious activities cross check  for the false positives and false negative using help from already established industry tools initially. 

>More the data , More accuracy , Less false positives



## Installation

- Git clone the repositary / Download the repositary

- Navigate to the Project folder 

- Install the required library using
 
 	`pip install -r requirements.txt`

- Run the Flask server using 

	`run server.py`

- Browse api 
 	
    `http://127.0.0.1:5000/ip/<insert ip> `

##  API Output 

The api on being called will return json having two parameters
>vpn  and response 

Value of vpn is an int ranging from 0-1

> 0 -- not vpn for sure , 1 --  vpn for sure , 1 -- error

Response contains data extra meta information

## Online Implementation and Initial POC

Live demo -- [https://vpnhunter.herokuapp.com/](https://vpnhunter.herokuapp.com/)

Introduction Video and POC [https://youtu.be/i8B6V3DS7v8](https://youtu.be/i8B6V3DS7v8)
