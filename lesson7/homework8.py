import random
 
#decimal guessing game
 

r = random.randint(25,455)
 
number = input("please enter a decimal")
number = int(number)
 
print(r)
print(number)
 
if number == r:
    print('win')
else:
    print('no')
 
 
 
# gold price close 60 days (daily)
 
moving_average=[1811.50,1818.14,1842.20,1871.60,1887.75,1902.74,1942.59,1958.90,1971.28,1956.92,1977.40,1977.28,2019.73,2038.85,2063.85,2036.41,2027.65,1912.34,1916.54,1954.42,1946.08,1985.64,2002.83,1929.43,1947.76,1942.22,1929.32,1928.60,1954.93,1930.01,1965.91,1968.10,1970.70,1943.26,1931.09,1934.46,1929.28,1932.25,1947.00,1946.53,1940.93,1957.06,1954.39,1959.57,1944.79,1951.72,1912.75,1900.48,1863.63,1868.20,1862.13,1881.64,1898.34,1886.29,1906.31,1900.87,1913.85,1878.72,1885.79]
total=sum(moving_average)
size=(len(moving_average))
print(total/size)
print(2063.85-1797.65)
 
import statistics
median = statistics.median(moving_average)
print(median)
 
print("mode of given data set is % s" %(statistics.mode(moving_average)))
 
moving_average2=[1943.25,1940.93,1811.50]
total2=sum(moving_average2)
size2=(len(moving_average2))
print(total2/size2)
median = statistics.median(moving_average2)
print(median)
print("mode of given data set is % s" %(statistics.mode(moving_average2)))