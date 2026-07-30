#tuple is immutable meaning it cant be changed so it must be converted to a list for changes
t=(12,13,16,15)
t=list(t) #changes to list
t[2]=14
t=tuple(t) #changes to tuple
print(t)


