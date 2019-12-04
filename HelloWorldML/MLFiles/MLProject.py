import numpy as np #matematiksel işlemlerde kullancağımız kütüphane
from sklearn.linear_model import LinearRegression as lr #Sklearn linner regresyon modeli
import pandas as pd # verileri düzenlemek için kullanılan kütüphane
import matplotlib.pyplot as plt  #grafik çizdirmek için kullanılan kütüphane

class main():
    def __init__(self):
        super().__init__()
        readdata()

def readdata():  # verileri çekip düzenleyeceğimiz metod
    data = pd.read_csv("dataset.csv")
    x= data["m2"] #dataset csv içindeki başlıklar
    y= data["price"] #dataset csv içindeki başlıklar
    x= x.values.reshape(6,1) #verisetini yeniden boyutlandırıyoruz (6 adet x satırı  olduğu için)
    y=y.values.reshape(6,1) #verisetini yeniden boyutlandırıyoruz (6 adet x satırı  olduğu için)
    linear_regression(x,y)  #kendi oluşturduğumuz lineer regresyon metodunu çağırıyoruz

def linear_regression(x,y):
    lineerreg  = lr()  #sklearn lineer regresyon modelini 'lineerreg' adıyla kullancağız
    lineerreg.fit(x,y)  # örneğin veri üzerinde öğrenmesi fit fonksiyonuyla yapılıyor
    lineerreg.predict(x)  #tahmin fonksiyoru
    m=lineerreg.coef_ #eğim
    b=lineerreg.intercept_ #b değeri
    plt.scatter(x, y) # matplotlib ile noktaları gösterme
    plt.plot(x,lineerreg.predict(x),c="red") # doğruyu çizdirme
    plt.show() # çizilen grafiği göster


main()