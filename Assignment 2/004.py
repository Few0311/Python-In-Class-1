print("Data input are integer!.")
k1 = int(input("Enter the starting kilometer : "))
k2 = int(input("Enter the ending kilometer : "))
time = int(input("Enter the time in hour : "))
print()
distance = k2 - k1
average_speed = distance / time
print("The distance is : ",distance,"km")
print("The average speed is : ",average_speed,"km/h")
