##
## EXERCISE -> change th 3rd order polynomial for the curve fit
##

# use the same data from above
x = np.linspace(-3*np.pi,3*np.pi,20)
noise = (np.random.random(20)*2 - 10) * 200
y = x**3-6*x**2 + noise

# must provide a model function, with independent variable as the first parameter
def m(x,a,b,c,d):
    return a + b*x + c*x**2 + d*x**3

# call scipy's curve fitting routine
c = curve_fit(m,x,y)

plt.plot(x,y,'ro',x,m(x,c[0][0],c[0][1],c[0][2],c[0][3]))