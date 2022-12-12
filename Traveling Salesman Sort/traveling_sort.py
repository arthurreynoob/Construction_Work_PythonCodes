import csv
import itertools

# Read the CSV file and store the coordinates in a list
coords = []
with open('road_marks.csv', 'r') as csvfile:  
  reader = csv.reader(csvfile)
  for row in reader:
    coords.append((float(row[0]), float(row[1]), row[2], str(row[3])))


# Calculate the distance between two points
def distance(p1, p2):
  return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


# Find the shortest path that visits all points
new_list=[coords[0]]
list_length=len(coords)
i=1
for point in new_list:
    shortest_dist = float('inf')
    
    for j in range(1,len(coords)):
        computed_dist=distance(point,coords[j])
        if computed_dist<shortest_dist:
            shortest_dist=computed_dist
            new_point=coords[j]
            
            
    new_list.append(new_point)
    coords.remove(new_point)
    i+=1
    
    if i>=list_length:
        break
        



# Print the shortest path
print("Shortest path:")
for p in new_list:
  print(p)


# Sort the CSV file based on the shortest path
sorted_rows = [row for row in new_list]
with open('sorted_points_3.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)
  for row in sorted_rows:
    writer.writerow(row)