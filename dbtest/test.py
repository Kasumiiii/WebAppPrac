import sys
from student import Student
from db_util import get_session

session = get_session()
student = Student()

if len(sys.argv) > 1:
    student.name = sys.argv[1]
    session.add(student)
    session.commit()

students = session.query(Student).all()
for student_object in students:
    print(f'{student_object.student_id} : {student_object.name}')

"""
target = session.query(Student).filter(Student.name=="tanaka").first()
target.name = 'yamada'
session.commit()
"""
session.close()