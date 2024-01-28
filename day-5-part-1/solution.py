
from collections import Counter

def main():
    # Initialize variables
    seeds = []
    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []
    current_map = None
    answer = 100000000000

    # Open the file and read line by line
    with open("input.txt", 'r') as file:

        for line in file:
            # Check for the map headers
            if 'seeds' in line:
                seeds = line[6:].split()
            if 'seed-to-soil map' in line:
                current_map = 'seed-to-soil'
            elif 'soil-to-fertilizer map' in line:
                current_map = 'soil-to-fertilizer'
            elif 'fertilizer-to-water map' in line:
                current_map = 'fertilizer-to-water'
            elif 'water-to-light map' in line:
                current_map = 'water-to-light'
            elif 'light-to-temperature map' in line:
                current_map = 'light-to-temperature'
            elif 'temperature-to-humidity map' in line:
                current_map = 'temperature-to-humidity'
            elif 'humidity-to-location map' in line:
                current_map = 'humidity-to-location'
            elif current_map != None:
                # Split the line into values and convert them to integers
                values = list(map(int, line.split()))
                # Append the values to the appropriate map
                if current_map == 'seed-to-soil' and values:
                    seed_to_soil_map.append(values)
                elif current_map == 'soil-to-fertilizer' and values:
                    soil_to_fertilizer_map.append(values)
                elif current_map == 'fertilizer-to-water' and values:
                    fertilizer_to_water_map.append(values)
                elif current_map == 'water-to-light' and values:
                    water_to_light_map.append(values)
                elif current_map == 'light-to-temperature' and values:
                    light_to_temperature_map.append(values)
                elif current_map == 'temperature-to-humidity' and values:
                    temperature_to_humidity_map.append(values)
                elif current_map == 'humidity-to-location' and values:
                    humidity_to_location_map.append(values)
    
    for seed in seeds:
        soil = 0
        for rule in seed_to_soil_map:
            if int(seed) >= rule[1] and int(seed) <= rule[1] + rule[2]:
                soil = rule[0] + int(seed) - rule[1]
                break
        if soil == 0:
            soil = int(seed)

        fertilizer = 0
        for rule in soil_to_fertilizer_map:
            if soil >= rule[1] and soil <= rule[1] + rule[2]:
                fertilizer = rule[0] + soil - rule[1]
                break
        if fertilizer == 0:
            fertilizer = soil

        water = 0
        for rule in fertilizer_to_water_map:
            if fertilizer >= rule[1] and fertilizer <= rule[1] + rule[2]:
                water = rule[0] + fertilizer - rule[1]
                break
        if water == 0:
            water = fertilizer

        light = 0
        for rule in water_to_light_map:
            if water >= rule[1] and water <= rule[1] + rule[2]:
                light = rule[0] + water - rule[1]
                break
        if light == 0:
            light = water

        temperature = 0
        for rule in light_to_temperature_map:
            if light >= rule[1] and light <= rule[1] + rule[2]:
                temperature = rule[0] + light - rule[1]
                break
        if temperature == 0:
            temperature = light

        humidity = 0
        for rule in temperature_to_humidity_map:
            if temperature >= rule[1] and temperature <= rule[1] + rule[2]:
                humidity = rule[0] + temperature - rule[1]
                break
        if humidity == 0:
            humidity = temperature
            
        location = 0
        for rule in humidity_to_location_map:
            if humidity >= rule[1] and humidity <= rule[1] + rule[2]:
                location = rule[0] + humidity - rule[1]
                break
        if location == 0:
            location = humidity 

        if answer > location:
            answer = location

    print(answer)

    
    


main()
