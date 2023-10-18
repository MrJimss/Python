# Created on iPhone.
class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def area(self):
    	return self.width*self.height
    def __add__(self,other):
    	return Shape(self.width +other. width, self. height + other.height)
	def __gt__ (self,other):
		return (self.area()> other.area()
