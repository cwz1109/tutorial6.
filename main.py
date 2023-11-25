print("# # # f(x) = -x^2 + 3x - 2 from a=1 to b=2 # # #")
# def the function
def f(x):
    y = -x**2+(3*x)-2
    return y
x=1# set the x
# make a cycle
while x<2.1:
    print("When x =",x,"=> f(x) =",f(x))
    x+=0.1
print("# # # Example of Trapezium Rule Values # # #")
print("First Height:",f(x=1))
print("Last Height:",f(x=2))
# add every f(x) together
MiddleSum=0
for x in range(11,20):
    MiddleSum+=f(x/10)
print("Middle Sum:",MiddleSum)
# define the function to solve the approximate integration
def T():
    y=(0.1/2)*(f(x=1)+f(x=2)+2*MiddleSum)
    return y
print("Integration is approximately",T())
# set the Truevalue
Truevalue = 1/6
print("True value of integration is",Truevalue)
# calculate the %error
def error():
    y = ((Truevalue-T())*100)/Truevalue
    return y
print("Therefore the error is",error(),"%")

quit()
