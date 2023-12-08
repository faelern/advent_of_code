# seed to soil
# soil to fert
# fert to water
# water to light
# light to temp
# temp to humid
# humid to loc
from tqdm import trange
from tqdm import tqdm

file = open('input.txt', 'r')

maps = []

locs = []

i = -1
seeds = file.readline()
for line in file:
    if line == '#\n':
        maps.append([])
        i += 1
    maps[i].append(line[:-1])

for map in maps:
    map.pop(0)

seeds = seeds.split(' ')
seeds = [int(seed) for seed in seeds]
new_seeds = []

for i in range(0, len(seeds), 2):
    for x in trange(seeds[i], seeds[i] + seeds[i+1]):
        new_seeds.append(x)

print(len(new_seeds))


match = False
for seed in tqdm(new_seeds):
    start = seed

    for map in maps:
        match = False
        for dataset in map:
            if not match:
                data = dataset.split(' ')
                dest = int(data[0])
                source = int(data[1])
                rang = int(data[2])
                if 0 <= start - source <= rang - 1:
                    end = dest + start - source
                    match = True

        if not match:
            end = start
        start = end

    locs.append(end)

print(min(locs))


