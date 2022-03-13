city = ['Rabat','Sueca','Rudow','Mosu',' Le Plessis Trevise',' Kang Dong','Nezahualcóyotl','Lindenwold','Queanbeyan',' Saint Chamond','Cheektowaga','Tirupati','Snezhinsk','Glazov','Gaoyou','Nola','Rutigliano','Colombo','Meckenheim','Hamburg',]
print(city)
Distance_in_km = [1063 ,2656 ,1352 ,1841 ,61 ,1634 ,151 ,285 ,146 ,11 ,380 ,2547 ,2524 ,97 ,6999 ,63 ,105 ,244 ,502 ,30 ,]
print(Distance_in_km)

temp = 0

for i in range(len(Distance_in_km)):
    if temp < Distance_in_km[i]:
        temp = Distance_in_km[i]
print(temp)

