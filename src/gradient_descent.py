import math

def f(x):
  return x**2+2*x+1

class GradientDescent:
  def __init__(self, f, initial_point):
    self.point = initial_point
    self.f = f

  def compute_gradient(self, delta):
    p = self.point
    print('self', p+0.5*delta)
    deriv = (self.f(p+0.5*delta)-self.f(p-0.5*delta))/delta
    return deriv
  
  
  # def descend(self, alpha, delta, num_steps):
  #   #

  





# def g(x):
#   return (x**2+math.cos(x))/(math.e**math.sin(x))

# def f3(x):
#   return 1-x**2

# def gradient_descent(f,x0,alpha=0.1,delta=0.0001,iterations=2):
#   for iteration in range(iterations):
#     deriv = (f(x0+0.5*delta)-f(x0-0.5*delta))/delta
#     x0 = x0-alpha*deriv
#   return f(x0)


# def f2(x,y):
#   return 1+x**2+y**2

# def g2(x,y):
#   return 1+x**2+2*x+(y**2)-(9*y)

# def gradient_descent2(f,initial_point,alpha=0.01,delta=0.000001,num_iterations=10000):
#   x_point = initial_point[0]
#   y_point = initial_point[1]
#   for iteration in range(num_iterations): 
#     deriv_x = (f(x_point+0.5*delta, y_point)-f(x_point-0.5*delta, y_point))/delta
#     deriv_y = (f(x_point, y_point+0.5*delta)-f(x_point, y_point-0.5*delta))/delta
#     x_point = x_point-alpha*deriv_x
#     y_point = y_point-alpha*deriv_y
#   return f(x_point, y_point)
