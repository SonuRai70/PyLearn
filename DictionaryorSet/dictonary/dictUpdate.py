student = {
    "name" : 'sonu rai',
    "class" : '12th',
    "rollNo" : '230425'
}
student.update({"city" : 'jehanabad'})
print(student)
student.update({"age":'23'})
print(student)
student.update({"position" : 'Director'})
print(student)
new_city={"city":'purnea',"name":'Sonu Rai'}    #after update the original name will change.
student.update(new_city)
print(student)