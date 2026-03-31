students = {
    "Rahul": 85,
    "Amit": 92,
    "Neha": 88
}
topStudent = ""
max_marks = 0

for name,marks in students.items():
    if marks>max_marks:
        max_marks = marks
        topStudent = name
        
print("Top Students ", topStudent)
print("max marks ",max_marks)
    
