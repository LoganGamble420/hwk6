import numpy as np

#problem 1
def ellipse_func(x,a,b):
    '''reads in x,a,b and outputs the function of the ellipse '''
    return 4*b/a*np.sqrt(a**2 - x**2) #y=sqrt((1-x^2/a^2))*b

def ellipse_area(a,b):
    ''' easy method for finding area of ellipse used for error '''
    return np.pi*a*b

def integral(x,y):
    ''' function that computes the forward difference method '''
    area=[]
    for i in range(len(x[:-1])):
        side=y[i]
        side2=y[i+1]
        a= 0.5* (side+side2) * (x[i+1] - x[i])
        area.append(a)
    answer = 0
    for t in area:
        answer += t
    return answer

print('Evaluating area of ellipse using 1D sum integral: ')
xval=np.arange(0,2,.01)
yval=ellipse_func(xval,2,4)
answer = integral(xval,yval)
print(answer)

#problem 1.2

print('evaluating area of ellipse using numpys sneaky masked integral')
x=np.arange(-2,2,.01)
y=np.arange(-4,4,.01)
xs,ys=np.meshgrid(x,y)
a=2
b=4
mask = 1.0*(xs**2/a**2 + ys**2/b**2 <=1)
dx=.01
dy=.01
s_masked=np.sum(mask*dx*dy)
print(s_masked)
