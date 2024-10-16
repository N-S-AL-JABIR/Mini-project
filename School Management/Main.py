from Class_room import ClassRoom
from Person import Teacher, Student
from Schools import School
from Subjects import Subject

school = School("abcd", "dhaka")

eight = ClassRoom("Eight")
nine = ClassRoom("nine")
ten = ClassRoom("ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim = Student("Rahim", eight)
fokir = Student("Fokir", nine)
kahim = Student("Kahim", nine)
jakir = Student("Jakir", ten)

school.student_admission(rahim)
school.student_admission(fokir)
school.student_admission(kahim)
school.student_admission(jakir)

abdul = Teacher("abduk khan")
babdul = Teacher("babduk khan")
kabdul = Teacher("kabduk khan")

bang = Subject("Bangla", abdul)
phy = Subject("Physics", babdul)
enb = Subject("English", kabdul)
Kang = Subject("Kangla", abdul)

eight.add_subject(bang)
eight.add_subject(phy)
eight.add_subject(enb)
eight.add_subject(Kang)

nine.add_subject(bang)
nine.add_subject(phy)
nine.add_subject(Kang)

ten.add_subject(bang)
ten.add_subject(enb)
ten.add_subject(phy)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)
