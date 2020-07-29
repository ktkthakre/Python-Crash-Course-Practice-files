#declaring list
city = ['tokyo','vegas','new york','california','paris']

#accessing elements
print(city[0].title())

#accessing in f-string
print(f"\n{city[0].title()} is the biggest city in Japan")

#changing elements
city[1] = 'rio'
print(city)

#adding elements

#appending method
city.append('berlin')
print(city)

#insert() method
city.insert(3, 'sydney')
print(city)

#removing elements

#del method
del city[4]
print(city)

#pop() method
city.pop()
print(city)
city.pop(0)
print(city)

#remove() method - to remove using value
city.remove('paris')
print(city)

#organising list

#temperory sort
print(sorted(city))
print(city)

#temperory alphabetical sort
print(sorted(city, reverse = True))
print(city)

#permanet sort
city.sort()
print(city)

#length of list
print(len(city))