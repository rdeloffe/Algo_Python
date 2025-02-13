def add(a,b) :
    return a + b
print("Sans Lambda")
print (add(1,2))
# OU (Version Lambda)
add_lambda = lambda a,b : a + b  

print("Avec Lambda")
print(add_lambda(1,2))

###############################################

#map()
nums = [1,2,3,4]
result = list(map(lambda x : x * 2,nums))
print(result)