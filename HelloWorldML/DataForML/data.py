import  requests
from bs4 import BeautifulSoup
import json
import os
import csv

class main:
    def __init__(self):
        cname=input("classname")
        element=input("element")
        wb = input("webaddresi")
        req(cname,element,wb)
def req(cn,el,webaddress):
    r = requests.get(webaddress)
    sc = r.status_code
    content = r.content
    bsoup(cn,el,content)
def bsoup(cn,et,rcont):
    soup= BeautifulSoup(rcont,"lxml")
    dataset = soup.find_all(et,attrs={"class":cn})
    m2list= {}
    sayac =0
    for i in dataset:
        m2 = i.h4.text
        price = i.h3.text
        cur_path = os.path.dirname(__file__)
        new_path = os.path.relpath('..\\MLFiles\\dataset.csv', cur_path)
        with open(new_path, 'a', newline='') as file:
            writer = csv.writer(file)
            if sayac==0:
                writer.writerow(["SN", "m2", "price"])
            writer.writerow([sayac, m2, price])

        #m2list[sayac]= {"0":m2,"1":price}
        sayac=sayac+1
    #createjson(m2list)

main()


