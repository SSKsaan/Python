 #! Demo Functions
def Pout(para): print(para)
def take_list(*args): print(args)

print("TestModule Hit") # executes even when imported elsewhere

if __name__ == '__main__': # executes only when run directly, recommended
    print("This is being run directly")
# when imported elsewhere, __name__ is set to filename instead of '__main__'