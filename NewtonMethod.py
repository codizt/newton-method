def derive(coeffs):  # For finding the derivative of a polynomial
    outcoeff = []
    for i in range(len(coeffs)):
        if(i != 0):
            outcoeff.append(i*coeffs[i])
    return outcoeff


def calc(coeffs, x):  # For calculating f(x)
    s = 0
    for i in range(len(coeffs)):
        s += coeffs[i]*pow(x, i)
    return s


def rec(coeffs, x0):  # Newton Method Recurrence Formula
    x = x0 - calc(coeffs, x0)/calc(derive(coeffs), x0)
    return x


print("\n\n~~~ NEWTON RAPHSON METHOD ~~~\n\n")
deg = int(input("Enter the degree: "))
coeffs = []
for i in range(deg+1):
    if(i == 0):
        a = float(input("Enter the constant term: "))
        coeffs.append(a)
    else:
        cf = float(input(f"Enter the coffecient of x^{i}: "))
        coeffs.append(cf)

print("The equation is: \nf(x) = ", end="")
for i in range(len(coeffs)-1, -1, -1):
    if(coeffs[i] == 0):
        continue
    if(i == 0):
        print("(", coeffs[i], ")", " = 0", end="")
    else:
        print("(", coeffs[i], ")", "x^", i, " + ", end="")

choice = int(input(
    "\n\nx0 value - Enter choice: \n0: To skip\n1. Enter value \n2. Enter interval \nChoice: "))
x0 = 0

if(choice == 1):
    x0 = float(input("Enter the value of inital guess: "))
elif(choice == 2):
    l = float(input("Enter the lower bound: "))
    u = float(input("Enter the upper bound: "))
    x0 = (l+u)/2
else:
    x0 = 0

accuracy = int(input("Enter the accuracy of the root required: "))
delta = 5*pow(10, -(accuracy+1))

depth_limit = 100
depth = 0

iter_values = [float("inf"), x0]

while((((iter_values[-1] - iter_values[-2]) >= delta) or ((iter_values[-2] - iter_values[-1]) >= delta)) and depth < depth_limit):
    x0 = rec(coeffs, x0)
    iter_values.append(x0)
    depth += 1

print("The root by Newton Method is:", round(x0, accuracy+1), "\n\n")
