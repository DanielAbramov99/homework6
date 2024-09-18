sum_city: int = 0
for temp in range(1, 5 + 1):
    city_temp: int = int(input("enter city temperatures:"))
    while city_temp < -50 or city_temp > 45:
        city_temp: int = int(input("illegal parameter,try again:"))
    print(f"city number {temp} temperature is:{city_temp}")
    sum_city += city_temp
else:
    avg_temp = sum_city / 5
    print(f"the average temperature across 5 cities is: {avg_temp}!")
