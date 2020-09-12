import math
print("Hello World")
for i in list(range(10,100,5)):
    print("%d * %d = %d" % (i, i, i*i))
a="I'm %(name)s. I'm %(age)d year old" % {'name':'Vamei', 'age':99}
print(a)
print(type(a))
print(math.e)