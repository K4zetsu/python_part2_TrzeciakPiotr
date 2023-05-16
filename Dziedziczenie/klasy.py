
class Figury:
   def __init__(self, bok_A, bok_B, wysokosc):
      self.bokA = bok_A
      self.bokB = bok_B
      self.heigh = wysokosc
    
   def kwadrat(self):
       a = self.bokA
       b = self.bokB
       h = self.heigh
       wynik  = a * a
       return print("pole kwadratu wynosi:", wynik)
   def prostokat(self):
       a = self.bokA
       b = self.bokB
       wynik = a * b
       return print("pole prostokąta wynosi:", wynik)
   def romb(self):
       a = self.bokA
       h = self.heigh
       wynik = a * h
       return print("pole rombu wynosi:", wynik)
   def rownoleglobok(self):
       a = self.bokA
       h = self.heigh
       wynik = a * h
       return print("pole równoległoboku wynosi:", wynik)
   def trojkat(self):
       a = self.bokA
       h = self.heigh
       wynik = (a * h)/2
       return print("pole trójkąta wynosi:", wynik)
   def trapez(self):
       a = self.bokA
       b = self.bokB
       h = self.heigh
       wynik = ((a + b) * h) / 2
       return print("pole trapeza wynosi:", wynik)

class Obwody(Figury):
    
    def obwod_kwadratu(self):
       a  = self.bokA
       wynik  = 4 * a
       return print("obwod kwadratu wynosi:", wynik)
   
    def obwod_prostokata(self):
       a = self.bokA
       b = self.bokB
       wynik = 2 * a + 2 * b
       return print("obwod prostokąta wynosi:", wynik)
   
    def obwod_rombu(self):
       a = self.bokA
       wynik = 4 * a
       return print("obwód rombu wynosi:", wynik)
   
    def obwod_rownolegloboku(self):
       a = self.bokA
       b = self.bokB
       wynik = 2 * a + 2 * b
       return print("obwód równoległoboku wynosi:", wynik)
   
    def obwod_trojkata(self):
       a = self.bokA
       b = self.bokB
       c = ((a ** 2) + (b ** 2)) ** 0.5
       wynik = a + b + c
       return print("obwód trójkąta wynosi:", wynik)
   
    def obwod_trapezu(self):
       a = self.bokA
       b = self.bokB
       c = ((a - b) / 2) ** 2 + self.heigh ** 2
       c = c ** 0.5
       wynik = a + b + 2 * c
       return print("obwód trapezu wynosi:", wynik)
    


