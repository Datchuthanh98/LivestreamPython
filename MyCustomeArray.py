import time

from DataModel import DataModel

class MyCustomeArray:
  def __init__(self):
    self.maxCapacity = 1000000
    self.size = 0
    self.offset = None
    self.currentPostion = 0
    self.array = [None]* self.maxCapacity

  def add(self, data):
      if self.offset == None :
        self.offset = -data.position
      arrayPosition = data.position + self.offset
      if arrayPosition >= self.currentPostion:
        self.array[arrayPosition] = data
        self.size +=1


  def take(self):
      if self.size == 0:
        return None
      self.size -=1
      tmp = self.array[self.currentPostion]
      self.currentPostion +=1
      return tmp

  def getSize(self):
    return self.size