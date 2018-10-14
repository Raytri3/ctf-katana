import socket               
import time
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
s = socket.socket()         
port = 9002               
s.connect(('216.165.2.33', port))
print s.recv(1024)
rec=s.recv(1024)
print rec
X=symbols('x')
rec=rec.split("\n")
eq=rec[0].split("=")
while True:
   var=parse_expr(eq[0])
   var2=parse_expr(eq[1])
   equ=Eq(var,var2)
   print equ
   sol=float(solve(equ)[0])
   #time.sleep(1)
   print sol
   
   s.send(str(sol)+"\n".encode())
   #time.sleep(1)
   rec=s.recv(2048)
   print rec
   rec=rec.split("\n")
   eq=rec[1].split("=")
s.close()