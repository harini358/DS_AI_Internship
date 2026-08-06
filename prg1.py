name=input("enter your name:")
marks=[]
while True:
    mark=input("enter the marks:")
    if mark == "done":
        break
    marks.append(int(mark))
print("Name",name)
print("Marks",marks)
print("Avg marks",sum(marks)/len(marks))

def grade(avg):
    if avg>=90:
        return "A+"
    elif avg>=80:
        return "A"
    elif avg>=70:
        return "B"
    elif avg>=60:
        return "C"
    elif avg>=50:
        return "D"
    else:
        return "F"
print("Grade",grade(sum(marks)/len(marks)))
