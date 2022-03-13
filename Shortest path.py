city = ['Rabat to Sueca', 'Sueca to Rudow', 'Rudow to Mosu', 'Mosu to Le Plessis Trevise',
        'Le Plessis Trevise to Kang Dong', '  Kang Dong to Nezahualcoyotl', 'Nezahualcoyotl to Lindenwold',
        'Lindenwold to Queanbeyan', 'Queanbeyan to Saint Chamond', ' Saint Chamond to Cheektowaga',
        'Cheektowaga to Tirupati', 'Tirupati to Snezhinsk', 'Snezhinsk to Glazov', 'Glazov to Gaoyou', 'Gaoyou to Nola',
        'Nola to Rutigtiano', 'Rutigtiano to Colombo', 'Colombo to Meckenheim',
        'Meckenheim to Hamburg', 'Hamburg to Rabat', ]
Distance_in_km = [1063, 2656, 1352, 1841, 61, 1634, 151, 285, 146, 11, 380, 2547, 2524, 97, 6999, 63, 105, 244, 502,
                  30, ]

temp = 0
print('the largest distance !!')
for i in range (len(Distance_in_km)):
     if temp < Distance_in_km[i]:
         temp = Distance_in_km[i]
print(temp)
print('The index number of largest distance !!')
x = Distance_in_km.index(temp)
print(x)
add2= 0
add1 = 0
print('The shortest route !!')
for t in range (x+1,len(city)):
    print(city[t],Distance_in_km[t])
    add1 = add1+Distance_in_km[t]

for j in range(0,x):
    print(city[j],Distance_in_km[j])
    add2= add2+Distance_in_km[j]

total_distance = add1 + add2
print('Total Distance !!', total_distance)



