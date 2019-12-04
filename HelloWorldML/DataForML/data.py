import  requests #HTTP Sorgularını yaparken kullancağımız kütüphane
from bs4 import BeautifulSoup# HTML Parser
import json  # verisetini oluşturmak için
import os # dosya işlemleri için
import csv # verisetini oluşturmak için

class main:
    def __init__(self):
        cname=input("classname")  #html parse ederken kullancağımız varsa class ismi
        element=input("element") #html parse ederken kullancağımız element ismi ("div","p"vs)
        wb = input("webaddresi") # sorgu yapacağımız ve parse edeceğimiz websitesi
        req(cname,element,wb) #sorgu yapacağımız metod
def req(cn,el,webaddress):
    r = requests.get(webaddress) #get metoduyla sayfadan html i çektik
    sc = r.status_code # web sitesinin bize verdiği cevap ("200","403","404" vs)
    content = r.content #html içeriği
    bsoup(cn,el,content) #htmli parse edeceğimiz metod
def bsoup(cn,et,rcont):
    soup= BeautifulSoup(rcont,"lxml") #BeautifulSoup kütüphanesini soup ile çağırıyoruz rcont html içeriğimiz
    dataset = soup.find_all(et,attrs={"class":cn}) #find all ile belirttiğimiz class ismine ve belirttiğimiz elemente sahip lanhtml içeriğinin tamamını alıyoruz
    m2list= {}
    sayac =0
    for i in dataset: #istediğimiz içerik içinde
        m2 = i.h4.text #h4 olanların texti ör:metrekare
        price = i.h3.text #h3 olanların texti ör:fiyat
        cur_path = os.path.dirname(__file__)
        new_path = os.path.relpath('..\\MLFiles\\dataset.csv', cur_path) #csv dosyasının pathini belirtiyoruz
        with open(new_path, 'a', newline='') as file:
            writer = csv.writer(file)
            if sayac==0: #ilk seferinde başlıkları yazdır
                writer.writerow(["SN", "m2", "price"])
            writer.writerow([sayac, m2, price]) #çektiğimiz içeriği csv ye yazdır

        #m2list[sayac]= {"0":m2,"1":price}
        sayac=sayac+1
    #createjson(m2list)

main()


