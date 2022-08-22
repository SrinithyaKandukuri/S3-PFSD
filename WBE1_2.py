


class Rectangle:
    a = 10
    b = 10
          def rectPeri(self):
              p=2 * (self.a + self.b)
                 print(p)
           def rectArea(self):
               A = self.a * self.b
               print(A)

from math import *
class Circle:
    r = 7
      def cirCir(self):
         c = 2 * math.pi * r
         print(c)
      def cirArea(self):
         a = math.pi * self.r * self.r
          print(a)

from math import *
class Triangle:
    a = 10
    b = 20
    c = 30
     s = (self.a + self.b + self.c) / 2
         def triPeri(self):
            p = s * 2
             print(p)
         def triArea(self):
              Area = math.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))
              print(Area)