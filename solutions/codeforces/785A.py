'''
Anton and Polyhedrons
'''
polyhedrons = {
    'Icosahedron': 20,
    'Cube': 6,
    'Tetrahedron': 4,
    'Dodecahedron': 12,
    'Octahedron': 8,
}
n = int(input())
total = 0
for i in range(n):
    name = input()
    total += polyhedrons[name]
print(total)