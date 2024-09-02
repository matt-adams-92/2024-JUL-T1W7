# Scope - global and local

fname = "Matt"                       # global scope
lname = "Adams"                      # global scope

# pure functions
def greet():
    fname = "First"                  # local scope
    lname = "Last"                   # local scope
    print(fname)
    print(lname)

print(fname)                         # global scope
print(lname)                         # global scope
greet()                              # local scope