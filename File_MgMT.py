def count_lines(file):
    with open(file, 'r') as f:
        return len(f.readlines())
def city_dat():
    with open('city.txt', 'r') as f:
        for city in f:
            print(city.strip())
def pop_thresh():
    with open('city.txt', 'r') as f:
        for line in f:
            part = line.split()
            city_name = part[0]
            population = float(part[1])
            if population > threshold:
                print(city name)
def sum_area():
    with open('city.txt', 'r') as f:
        for line in f:
            part = line.split()
            area = part[2]
            total_area += area
