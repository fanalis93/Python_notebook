def read_integers(filename):
    with open(filename) as f:
        return map(int, f)
res = read_integers('F:/Programming Problems/sensordata.txt')
print(list(res))