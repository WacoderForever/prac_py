from vectors import *

def perimeter(vector_list):
    distances = [length(subtract(vector_list[i],vector_list[(i+1)%len(vector_list)]))
                for i in range(0,len(vector_list))]
    return sum(distances)

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
(-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
(-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)]

print(f"The perimeter is {perimeter(dino_vectors)}\n")
