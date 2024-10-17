#SridharacharyaJi
n=input('Equation=')                                                                                                          #entering eq. in string as variables can't be taken in int
if 'xx' not in n:                                                                                                                   #checking equation
    print('The given equation is not quadratic. Please check the equation before entering again')
else:
        E=n.split('x')                                                                                                              #taking number out for required calculations in a list
        x=E[0]                                                                                                                      #coefficient of x^2
        if '**' in x:
            X=eval(x)                                                                                                             #checking if it contains any value in root
        elif x=='' or x=='+':
            X=1
        elif x=='-':
            X=-1                                                                                                                    #if string is empty giving it 1 or if it contains '-' giving it -1
        else:
            X=float(x)                                                                                                             #if everything fine converting it in float for calculation
        if len(E)==3:                                                                                                               #if len is 3 it may be containing one empty string
            if E[-2]=='':
                Y=0                                                                                                                 #checking condition and if string found empty giving it 0 for calc. as 'x' was not even present therefore 0
        elif len(E)==4:
            y=E[2]
            if y=='+':                                                                                                              #if string is having either '+' or '-' it should be given +1 or -1 as splitting was done on the basis of x''
                Y=1
            elif y=='-':
                Y=-1
            else:
                if '**' in y:                                                                                                         #checking if it contains any value in root
                    Y=eval(y)
                else:
                    Y=float(y)                                                                                                   #if it consists of values converting it into float for calc.
        if E[-1]=='':
            Z=0                                                                                                                    #taking out constant value and if string found empty giving it 0
        else:
            z=E[-1]
            if '**' in z:                                                                                                           #checking if it contains any value in root
                Z=eval(z)
            else:
                Z=float(z)                                                                                                       #converting into float
        D=Y**2-4*X*Z
        O=-Y-D**(1/2)                                                                                                        #calc.
        I=O/(2*X)
        print(I)                                                                                                                   #first req.value
        H=-Y+D**(1/2)                                                                                                       #calc.
        J=H/(2*X)
        print(J)                                                                                                                   #second req. value
