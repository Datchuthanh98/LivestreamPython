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
      if arrayPosition == self.maxCapacity:
            if self.currentPostion ==0 or self.currentPostion < self.maxCapacity/10:
                  self.maxCapacity *=2
                  #overflow
                  if self.maxCapacity < 0:
                      print("Array capacity overflows")
                  arrayTemp = [None]*self.maxCapacity
                  arrayTemp[0:self.maxCapacity/2]=self.array[0:self.maxCapacity/2]
                  self.array =arrayTemp
            else:
                  #queue is not full
                  self.array[0:self.maxCapacity-self.currentPostion] = self.array[self.currentPostion:self.maxCapacity-self.currentPostion]
                  self.offset -= self.currentPostion
                  arrayPosition -= self.currentPostion
                  self.currentPostion = 0

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