
# nur gerade Kubikzahlen i = 1-10
print( [i ** 3 for i in range(11) if i**3 % 2 == 0] )

# alle Teiler einer Zahl z außer 1 und z
def teiler(z):
    return [teiler for teiler in range(2, z) if z % teiler == 0]

print(teiler(123))
print(teiler(12345))
print(teiler(123456))

# alle Primzahlen zwischen 10000 10100
print( [e for e in range(10000,10101) if all(e % y != 0 for y in range(2, e))] )


# map filter reduce etc

print( list(filter(lambda i: i**3 % 2 == 0,map(lambda x: x**3, range(11)))))


def teiler_func(z):
    print(list(filter(lambda y: z % y == 0, range(2, z))))

teiler_func(123)