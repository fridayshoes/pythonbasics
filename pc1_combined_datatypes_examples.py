# Example 1: Student Record System

# Process student records with mixed types

# Objective: Process student records with mixed data types
# Outcome: Calculates averages and status for each student



students = [
    {"id": 101, "name": "Alice", "grades": (85, 92, 78)},
    {"id": 102, "name": "Bob", "grades": (76, 88, 91)}
]

for student in students:
    print(f"\nProcessing {student['name']} (ID: {student['id']})")
    total = 0
    for grade in student['grades']:
        total += grade
    
    avg = total / len(student['grades'])
    print(f"Average grade: {avg:.1f}")
    
    if avg >= 90:
        status = "A"
    elif avg >= 80:
        status = "B"
    else:
        status = "C"
    print(f"Status: {status}")


# Processing Alice (ID: 101)
# Average grade: 85.0
# Status: B

# Processing Bob (ID: 102)
# Average grade: 85.0
# Status: B





# Example 2: Sensor Data Processor

# Analyze mixed sensor data

# Objective: Process mixed sensor data
# Outcome: Computes min/max/avg for each sensor type


sensor_data = [
    ("temp", 22.4), 
    ("pressure", 1013), 
    ("temp", 23.1), 
    ("humidity", 45.7),
    ("pressure", 1012)
]

readings = {"temp": [], "pressure": [], "humidity": []}
for data_type, value in sensor_data:
    if data_type in readings:
        readings[data_type].append(value)

results = {}
for data_type, values in readings.items():
    if values:
        results[data_type] = {
            "min": min(values),
            "max": max(values),
            "avg": sum(values)/len(values)
        }

print("Sensor Summary:")
for data_type, stats in results.items():
    print(f"{data_type.capitalize()}:")
    print(f"  Min: {stats['min']}, Max: {stats['max']}, Avg: {stats['avg']:.1f}")


# Sensor Summary:
# Temp:
#   Min: 22.4, Max: 23.1, Avg: 22.8
# Pressure:
#   Min: 1012, Max: 1013, Avg: 1012.5
# Humidity:
#   Min: 45.7, Max: 45.7, Avg: 45.7