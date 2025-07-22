x = 10

try: # with try at least 1 of except or finally is required
    x //= 0
    print(x)
#? if anything throws error here, the entire try block will be skipped

except IndentationError: # catching specific errors
    print('Error Occured')
except (ZeroDivisionError, TypeError) as e: # catching within multiple errors
    print(f'Cannot Divide {x} by Zero ({e})')
except: # catching any error (unspecified)
    print('Error Occured') # after one error block is caught, rest are skipped
#? won't come to except blocks if there're no errors in try block

else: # optional
    print('No error with', x)
#? for code that should run only if there's no error in try block

finally: # optional, typically used for cleanup operations
    print('End of Program\n')
#? will execute this block whether there's an error in try block or not

if x > 0: # raising a custom exception
    raise ValueError(f'{x} is invalid just because I said so\n')