minimizer = GradientDescent(f=single_variable_function, initial_point=[0])
assert minimizer.point == [0]
ans = minimizer.compute_gradient(delta=0.01)
[-2.000] # rounded to 5 decimal places
minimizer.descend(alpha=0.001, delta=0.01, num_steps=1)
assert minimizer.point == [0.002]

minimizer = GradientDescent(f=two_variable_function, initial_point=[0,0])
minimizer.point == [0,0]
minimizer.compute_gradient(delta=0.01)
[-2.000, 3.000]
minimizer.descend(alpha=0.001, delta=0.01, num_steps=1)
minimizer.point
[0.002, -0.003]

minimizer = GradientDescent(f=three_variable_function, initial_point=[0,0,0])
minimizer.point
[0,0,0]
minimizer.compute_gradient(delta=0.01)
[-2.000, 3.000, -4.000]
minimizer.descend(alpha=0.001, delta=0.01, num_steps=1)
minimizer.point
[0.002, -0.003, 0.004]

minimizer = GradientDescent(f=six_variable_function, initial_point=[0,0,0,0,0,0])
minimizer.point
[0,0,0,0,0,0]
minimizer.compute_gradient(delta=0.01)
[-2.000, 3.000, -4.000, 1.000, 2.000, 3.000]
minimizer.descend(alpha=0.001, delta=0.01, num_steps=1)
minimizer.point
[0.002, -0.003, 0.004, -0.001, -0.002, -0.003]