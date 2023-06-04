from abc import ABC, abstractmethod

class Figury(ABC):
    @abstractmethod
    def pole(self):
        pass
    @abstractmethod
    def obwod(self):
        pass

class Kwadrat(Figury):
   def __init__(self, bok_a):
      self.bok_a = bok_a
   def pole(self):
      return self.bok_a ** 2 
   def obwod(self):
      return self.bok_a * 4    
    

class Prostokat(Figury):
   def __init__(self, bok_a, bok_b):
      self.bok_a = bok_a
      self.bok_b = bok_b
   def pole(self):
      return self.bok_a * self.bok_b
   def obwod(self):
      return self.bok_a * 2 + self.bok_b * 2  

class Romb(Figury):
   def __init__(self, bok_a, wysokosc):
      self.bok_a = bok_a
      self.wysokosc = wysokosc
   def pole(self):
      return self.bok_a * self.wysokosc
   def obwod(self):
      return self.bok_a * 4

class Rowoleglobok(Figury):
   def __init__(self, bok_a, bok_b, wysokosc):
      self.bok_a = bok_a
      self.bok_b = bok_b
      self.wysokosc = wysokosc
   def pole(self):
      return self.bok_a * self.wysokosc
   def obwod(self):
      return self.bok_a * 2 + self.bok_b * 2

class Trapez(Figury):
   def __init__(self, podstawa_a, podstawa_b, bok, wysokosc):
      self.podstawa_a = podstawa_a
      self.podstawa_b = podstawa_b
      self.bok = bok
      self.wysokosc = wysokosc
   def pole(self):
      return ((self.podstawa_a + self.podstawa_b)*self.wysokosc)/2
   def obwod(self):
      return self.podstawa_a + self.podstawa_b + self.bok * 2  

class Trojkat(Figury):
   def __init__(self, bok_a, bok_b, wysokosc):
      self.bok_a = bok_a
      self.bok_b = bok_b
      self.wysokosc = wysokosc
   def pole(self):
      return (self.bok_a * self.wysokosc) / 2
   def obwod(self):
      bok_c = ((self.bok_a ** 2) + (self.bok_b ** 2)) ** 0.5
      return self.bok_a + self.bok_b  + bok_c



