x = 10
try: # with try at least 1 of except or finally is required
    x //= 0
    print(x)
# if anything throws error here, will ignore try & go to except
except:
    print('Error Occured')
# won't come here if there're no errors in try
finally:
    print(x)
# will come here whether there's an error in try or not

print('End of Program')

"""
*Using this exception handling method (this is the absolute basics),
*even if some errors are found, the remaining correct code can run.
"""
