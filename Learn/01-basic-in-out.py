""" hash is used for single-line comment and
triple double-quotations for multi-line comment """

 #! Output
print("Hello Python") # adds a line break by default
print("This is the", end=' ') # specifying line end to not add line break
print("S", "T", "A", "R", "T", sep='-') # specifying separator

 #! Variable
# format: "variable-name = value" (detects type automatically based on value)
number = 100
fraction = 1.1
fact = True
words = 'Anything & Everything'
line = f"A number {number} is not {fraction} or {words}..."
# using f"..." to use other variables inside a string variable
print(line)
print(number + fraction) # direct arithmatic operation
print(number,fraction) # comma adds a space in between by default
print("Let's say"  ,  words+'!') # plus appends strings
# spacing before/after comma/quotes/variable does't matter 
print(type(fact)) # checking data type of a variable

 #! Input
print('Enter something')
input() # will take any input even if not parameterized
# can have text before input without print():
input('Enter anything: ') # Don't have space after the string by default

n1 = input('Enter 1st Number: ') # taking  input while declaring variable
n2 = input('Enter 2nd Number: ') 
print(n1,'+',n2,'=',n1+n2) # by default input is taken as string type

n1 = int(n1) # overriding variable & then typecasting
n3 = float(n2) # making new varible to typecast
print(n1,'+',n3,'=',n1+n3)
print(n1,'+',n3,'=',str(n1)+str(n3)) # typecast without changing/assigning variable
