class Myfraction():
       def __init__(self, p, q = 1):
              self.p = p
              if q == 0:
                     print("分母不能为0")
                     raise ValueError
              else:
                     self.q = q

       def __add__(self, r):
              return Myfraction(self.p * r.q + self.q * r.p, self.q * r.q)

       def __sub__(self, r):
              return Myfraction(self.p * r.q - self.q * r.p,  self.q * r.q)

       def __mul__(self, r):
              return Myfraction(self.p * r.p, self.q * r.q)
  
       def __truediv__(self, r):
              return Myfraction(self.p * r.q, self.q * r.p)
                                
                            

       def __str__(self):
              
              def yuefen(a,b):
                     j = 0
                     if a > b:
                            min = b
                            max = a
                     else:
                            min = a
                            max = b

                     for i in range(1,min + 1):
                            if max % i == 0 and min % i == 0:
                                   j = i
                                   
                     a, b = a // j, b // j
                     if b == 1:
                            return '%s' % (a)
                     else:
                            return '%s/%s' % (a,b)

              return yuefen(self.p,self.q)



r1 = Myfraction(10)
r2 = Myfraction(1, 5)
print(f"r1 = {r1} , r2 = {r2}")
print(f"r1 + r2 = {r1+r2}")
print(f"r1 - r2 = {r1-r2}")
print(f"r1 * r2 = {r1*r2}")
print(f"r1 / r2 = {r1/r2}")
