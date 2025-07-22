x = 10

try: # with try at least 1 of except or finally is required
    x //= 0
    print(x)
# if anything throws error here, the entire try block will be skipped

except ZeroDivisionError: # catches specific errors
    print(f'Cannot Divide {x} by Zero')
# won't come to except blocks if there're no errors in try block
except: # can catch any error
    print('Error Occured') # after one error block is caught, rest are skipped

else: # optional
    print('No error with', x)
# for code that should run only if there's no error in try block

finally: # optional, typically used for cleanup operations
    print('End of Program')
# will execute this block whether there's an error in try block or not
