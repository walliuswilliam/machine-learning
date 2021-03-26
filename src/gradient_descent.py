import math

def f(x):
  return x**2+2*x+1

class GradientDescent:
  def __init__(self, f, initial_point):
    self.point = initial_point
    self.f = f

  def compute_gradient(self, delta):
    p = self.point[0]
    deriv = (self.f(p+0.5*delta)-self.f(p-0.5*delta))/delta
    return [deriv]
  
  def descend(self, alpha, delta, num_steps):
    point = self.point
    for num in range(num_steps):
      derivative = self.compute_gradient(delta)
      point = point-alpha*derivative
    return self.f(point)
