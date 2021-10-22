# -*- coding: utf-8 -*-

class cola:
    
    def __init__(self,n):
        self.__L = []
        self.m = n
        
    def __len__(self):
        i = 0
        for v in self.__L:
            i += 1
        return i
        
    def entrar(self,x):
        if self.__L.__len__() < self.m:
            self.__L.append(x)
        else:
            return "Cola llena"
        
    def salir(self):
        if self.__L.__len__() == 0:
            return "Cola vacía"
        elif self.__L.__len__() > 0:
            a = self.__L[0]
            self.__L.pop(0)
            return a
    
    def __str__(self):
        s = ""
        for elementos in self.__L:
            s += elementos + " "
        return s
    
    def vacia(self):
        if self.__L == []:
            return True
        else:
            return False
    
    def llena(self):
        if self.__L.__len__() == self.m:
            return True
        else:
            return False
