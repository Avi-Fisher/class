from abc import ABC, abstractmethod


class A():

    @abstractmethod
    def __init__(self,name):

        self.name = name



class B(A):

    def print(self):
        print("fjkdhjh")


a1 = B("avi")
a1.print()
