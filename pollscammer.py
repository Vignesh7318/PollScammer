#author @Vignesh7318

import threading
from random import choice
from random import shuffle
import time
import os
import sys




try:
  import furl
except ImportError:
  print("Trying to Install required module: furl \n")
  os.system('python -m pip install furl')
import furl
try:
  import requests
except ImportError:
  print("Trying to Install required module: requests \n")
  os.system('python -m pip install requests')
try:
  import bs4
except ImportError:
  print("Trying to Install required module: Beautifulsoup \n")
  os.system('python -m pip install bs4')
from bs4 import BeautifulSoup
import requests



def get_choice():
    global uchoice
    print("Try to use proxy list since scraped proxies are not worth the shot")
    print("\n 1. Proxy list \n 2. Scrap proxy \n 3. exit ")
    uchoice=int(input("Enter your choice  "))
    return uchoice

def get_proxies(link):  
    response = requests.get(link)
    soup = BeautifulSoup(response.text,"lxml")
    https_proxies = filter(lambda item: "yes" in item.text,
                           soup.select("table.table tr"))
    for item in https_proxies:
        yield "{}:{}".format(item.select_one("td").text,
                             item.select_one("td:nth-of-type(2)").text)





def get_random_proxies():
    global proxies
    proxies = list(get_proxies('https://www.sslproxies.org/'))
    shuffle(proxies)
    return choice(proxies)



def proxyfile():
   s=open("proxy.txt","r")
   m=s.readlines()
   global l
   l=[]
   for i in range(0,len(m)-1):
      x=m[i]
      z=len(x)
      a=x[:z-1]
      l.append(a)
      l.append(m[i+1])
   s.close()
   


userentry=input("enter the url  ")
global url
url=str(userentry)

def request_skeleton(choiceid):
    
    global payload
    global head
    
    url=str(userentry)
    payload="{\n    \"choiceIds\": [\n        \"%s\"\n    ]\n}"% choiceid
    
    head = {
  'Content-Type': 'application/json'
}
    print(head)
    print(url)
    print(payload)
    print(choiceid)
    


def get_choice_id():
    f = furl.furl(url)
    splitter=str(f.path).split("/")
    voteid=splitter[1]
    print(voteid)
    global choice_id
    global api_url

    api_url="https://www.polltab.com/api/poll/%s/vote" %voteid
    r=requests.get(api_url)
    json=r.json()

    team_name=str(input("ENTER TEAM NAME "))
    choice=json["data"]["choices"]
    for i in range(len(choice)):
        print(choice[i])
        if(choice[i]['text']==team_name):
            print("match got")
            choice_id=choice[i]['choiceId']
        


def using_proxy():
  
  o=choice(l)
  proxy={}
  proxy['https']=o
  print("using",proxy)
  print(url)
  l.remove(o)
  
  
  
  req(proxy)
 
  time.sleep(1)
  print("Remaining proxies : ",len(l))
  scraplist.append(o)
  if(len(l)==0):
    sys.exit(1)
  


    

def scrapping():
  proxy={}
  c=get_random_proxies()#double check though not necessary

    



  
  proxy['https']=c
  print(proxy)
  req(proxy)
  print(proxy)
  print("Using this proxy ",proxy)
  r=requests.post(url=api_url, proxies=proxy,data=payload,headers=head,timeout=7)
  print(r.text)
  print(r.text.encode('utf8'))
  print(r.status)
  

  

def setup():
  
  print("Configuring the entries \n")
  get_choice()
  if uchoice==3:
    sys.exit(1)
  proxyfile()
  get_choice_id()
  request_skeleton(choice_id)
  print("Everything is good to go \n")
setup()


def req(proxyit):
  reques=requests.request("POST",url=api_url,proxies=proxyit,data=payload,headers=head,timeout=7)
  print(reques.text.encode('utf8'))
  print("displaying response")




     
        
        
while(1):
   try:
      if uchoice==1:
        using_proxy()
        
      if uchoice==2:
        scrapping()
   except:
      pass
