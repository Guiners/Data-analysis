import pandas as pd
import matplotlib.pyplot as plt
import os
import scipy.stats as st
import numpy
os.getcwd()
os.listdir()
os.chdir('/Users/Robert/Desktop/Studia/III SEMESTR/Analiza i wizualizacja danych')
file = 'cars.csv'
data = pd.read_csv(file)



#data.info()
#help(pd.read_csv)#

#print(data.columns)
#print(data.columns[29])
#print(data[data.columns[29]])

#Klasa ze statystkykami
class Stats:
    def __init__(self, name):
        self.name = name
        self.srednia = 0
        self.mediana = 0
        self.dominata = 0
        self.odchylenie_przecietne = 0
        self.wariancja = 0
        self.odchylenie_standardowe = 0
        self.maximum = 0
        self.minimum = 0
        self.suma = 0
        self.odmienne_kategorie = 0
        self.ilosc_wartosci = 0
        self.lista = []
        self.listav2 = []
        self.wyniki = []

        #12 pozycji 11 zaczynajac od 0

    def liczenie(self, b = []):
        if len(b) != 0:
            for j in b:

                if j == 0:
                    self.srednia = round(data[self.name].mean(), 4)
                    self.lista.append(self.srednia)
                    self.listav2.append('srednia')

                if j == 1:
                    self.mediana = round(data[self.name].median(), 4)
                    self.lista.append(self.mediana)
                    self.listav2.append('mediana')

                elif j == 2:
                    self.dominata = round(data[self.name].mode(), 4)
                    self.lista.append(self.dominata)
                    self.listav2.append('dominata')

                elif j == 3:
                    self.odchylenie_przecietne = round(data[self.name].mad(), 4)
                    self.lista.append(self.odchylenie_przecietne)
                    self.listav2.append('odchylenie_przeciętne')

                elif j == 4:
                    self.wariancja = round(data[self.name].var(), 4)
                    self.lista.append(self.wariancja)
                    self.listav2.append('wariancja')

                elif j == 5:
                    self.odchylenie_standardowe = round(data[self.name].std(), 4)
                    self.lista.append(self.odchylenie_standardowe)
                    self.listav2.append('odchylenie_standardowe')

                elif j == 6:
                    self.maximum = round(data[self.name].max(), 4)
                    self.minimum = round(data[self.name].min(), 4)
                    self.lista.append(self.maximum)
                    self.listav2.append('maximum')
                    self.lista.append(self.minimum)
                    self.listav2.append('minimum')

                elif j == 7:
                    self.suma = round(data[self.name].sum(), 4)
                    self.lista.append(self.suma)
                    self.listav2.append('suma')

                elif j == 8:
                    self.odmienne_kategorie = round(data[self.name].unique(), 4)
                    self.lista.append(self.odmienne_kategorie)
                    self.listav2.append('odmienne_kategorie')

                elif j == 9:
                    self.ilosc_wartosci = round(data[self.name].count(), 4)
                    self.lista.append(self.ilosc_wartosci)
                    self.listav2.append('ilosc_wartosci')


    def pobieranie(self):
        return self.lista

#dlugosc_na_portalu
dlugosc_na_portalu = Stats('duration_listed')
dlugosc_na_portalu.liczenie([0,1,2,3,4,5,6])

#cena w dolcach
cena = Stats('price_usd')
cena.liczenie([0,1,2,4,5,6,7])

#ilość zdjec
zdjecia = Stats('number_of_photos')
cena.liczenie([0,1,2,3,4,5,6,7])

#pojemnosc silnika
pojemnosc = Stats('engine_capacity')
pojemnosc.liczenie([0,1,2,4,5,6])

#rok produkcji
rok = Stats('year_produced')
rok.liczenie([0,1,2,3,4,5,6])

#przebieg
przebieg = Stats('odometer_value')
przebieg.liczenie([0,1,2,3,4,5,6])

#liczba podbic
podbicia = Stats('up_counter')
podbicia.liczenie([0,1,2,3,4,5,6])





#Korelacja Pearsona dla ilości zdjęć i ilości dni na poltaru:

data['duration_listed'] = data['duration_listed'].astype(int)
data['number_of_photos'] = data['number_of_photos'].astype(int)
a = st.pearsonr(data["number_of_photos"], data["duration_listed"])
pearson_nop_dl = round(a[0],5)
pearson_nop_dl_rzet = round(a[1],10)
print("Korelacja Pearsona dla ilości zdjęć i ilości dni na poltaru aukcyjnym wynosi", pearson_nop_dl, ", a rzetelność wynosi", pearson_nop_dl_rzet )



#idk czy to sie do czegos przyda
#dupa = np.sort(data['number_of_photos'].unique())
#kupa = np.sort(data['duration_listed'].unique())
#print(dupa)
#print(kupa)

#nie wiem jak ugryść tak dużą ilość danych na tabeli
"""
plt.bar(data["number_of_photos"], data["duration_listed"])
plt.ylabel('Ilość dni na poltaru aukcyjnym')
plt.xlabel('Ilość zdjęć')
plt.show()"""