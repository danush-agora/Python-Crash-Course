motorcycles = ["Honda","Ducati","Kawasaki","Aprilia","BMW","Triumph","Suzuki","Harley-Davidson"]
print(motorcycles)
# formatting the output using f-strings
print(f"{motorcycles[5]} was my first bike!!")
print(f"{motorcycles[1]} makes some of the most beautiful bikes, the italian charm I guess!!")
print(f"{motorcycles[4]} was my first liter bike!!")
print(f"{motorcycles[7]} is the most iconic bike in the world!!")
print(f"One day I'd like to own a {motorcycles[0]} Fireblade!!")

# Modifying Elements in a list
motorcycles[6] = "KTM"
print(motorcycles)

# Adding elements to the list
# Method 1: Using append()
motorcycles.append("Suzuki Hayabusa")
print(motorcycles)

# Method 2: Using insert()
motorcycles.insert(0,"Royal Enfield")
print(motorcycles)