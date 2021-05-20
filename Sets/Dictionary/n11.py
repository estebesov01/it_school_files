# Есть список Южноамериканских стран
# СПИСОК №2
# в котором Суринам встречается два раза. 
# Необходимо написать программу,
# которая удалит дублирующуюся запись, 
# и возвратит в результате список.
south_american_countries = ['Argentina', 'Bolivia', 
'Brazil', 'Chile', 'Colombia', 'Ecuador', 
'Guyana', 'Paraguay', 'Peru', 'Suriname', 
'Suriname', 'Uruguay', 'Venezuela']
south_american_countries = list(set(south_american_countries))
print(south_american_countries)
