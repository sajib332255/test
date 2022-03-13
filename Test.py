city = ['Rabat to Sueca', 'Sueca to Rudow', 'Rudow to Mosu', 'Mosu to Le Plessis Trevise',
        'Le Plessis Trevise to Kang Dong', '  Kang Dong to Nezahualcoyotl', 'Nezahualcoyotl to Lindenwold',
        'Lindenwold to Queanbeyan', 'Queanbeyan to Saint Chamond', ' Saint Chamond to Cheektowaga',
        'Cheektowaga to Tirupati', 'Tirupati to Snezhinsk', 'Snezhinsk to Glazov', 'Glazov to Gaoyou', 'Gaoyou to Nola',
        'Nola to Rutigtiano', 'Rutigtiano to Colombo', 'Colombo to Meckenheim',
        'Meckenheim to Hamburg', 'Hamburg to Rabat', ]
Distance_in_km = [1063, 2656, 1352, 1841, 61, 1634, 151, 285, 146, 11, 380, 2547, 2524, 97, 6999, 63, 105, 244, 502,
                  30, ]

temp = 0
# find the largest value and total cost of path
for i in range(len(Distance_in_km)):
    if temp < Distance_in_km[i]:
        temp = Distance_in_km[i]

# find the index of the largest city
print('the shortest route!!')
x = Distance_in_km.index(temp)

add = 0
add1 = 0
for t in range(x+1,len(city)):
 print(city[t], Distance_in_km[t])
 add = add+Distance_in_km[t]

 if t == 19:
     for w in range (0,x):
         print(city[w], Distance_in_km[w])
         add1 = add1+Distance_in_km[w]


print('total distance',add+add1)





