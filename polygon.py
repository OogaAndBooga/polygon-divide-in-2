import math as mt


class Polygon:
  verteces = []
  vrt = verteces
  fv = None
  mousefv = False

  edges = 0

  def __init__(self):
    pass

  def addVert(self, v):
    self.verteces.append(v)
    self.edges = len(self.vrt)

  def isNearStart(self, pos):
    if len(self.vrt) != 0:
      return mt.dist(pos, self.verteces[0]) < 10
    else:
      return False
