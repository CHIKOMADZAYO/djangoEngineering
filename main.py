from typing import List
from  abc import ABC, ABCMeta, abstractmethod
import time


class Person:

    def __init__(self,name:str, age:float, course:List,balance:float):        
        self.name=name
        self.age=age
        self.course=course

        self.__feeBalance=balance



    def  check_fee_balance(self):
        fee_balance= self.__feeBalance

        if fee_balance==0:
            # The logic here  
            pass

        print(f"Hi,{self.name} your fee balance is KES {fee_balance}")

        


student=Person(
    name="William",
    age=22,
    course=["Data Structure and Algorithm", "Analysis of Algorithms"],
    balance=1000

)


print(student.check_fee_balance())

    









        