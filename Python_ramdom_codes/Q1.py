def full_pyramid(rows):
    
    for i in range(rows):
        print(' '*(rows-i-1) + '*'*(2*i+1))

def inverted_pyramid(rows):
    
    for i in reversed(range(rows)):
        print(' '*(rows-i-1) + '*'*(2*i+1))
# main code

inverted_pyramid(5)
full_pyramid(5)
print("BowTie(5)\n")

inverted_pyramid(6)
full_pyramid(6)
inverted_pyramid(6)
full_pyramid(6)
print("Candy(6)\n")

inverted_pyramid(3)
full_pyramid(3)
inverted_pyramid(3)
full_pyramid(3)
print("Candy(3)\n")

inverted_pyramid(4)
full_pyramid(4)
print("Bowtie(4)\n")
    