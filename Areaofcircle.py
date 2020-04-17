
Totalpoints = 100
Score = 60
per = Score/Totalpoints
Studentname = "XXX"
Grade = " "

if 100 >= Score >= 90:
    Grade = "A")
elif 90 > Score >= 80:
    Grade = "B"
elif 80 > Score  >= 70:
    Grade = "C"
else:
    Grade = "D"

print("The {} grade is: {} ".format(Studentname, Grade))


