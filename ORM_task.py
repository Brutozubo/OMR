from peewee import *

conn = SqliteDatabase('db1.sqlite')

class Students(Model):
	id = PrimaryKeyField(column_name = 'id')
	name = CharField(column_name = 'name')
	lastname = CharField(column_name = 'lastname')
	age = IntegerField(column_name = 'age')
	city = CharField(column_name = 'city')

	class Meta:
		database = conn

class Courses(Model):
	id = PrimaryKeyField(column_name = 'id')
	name = CharField(column_name = 'name')
	time_start =CharField(column_name = 'time_start')
	time_end =CharField(column_name = 'time_end')

	class Meta:
		database = conn

class Student_Courses(Model):
    student_id = ForeignKeyField(Students)
    courses_id = ForeignKeyField(Courses)

    class Meta:
        database = conn

Students.create_table()
Courses.create_table()
Student_Courses.create_table()


#st=[
#	{'id':1, 'name':'Max', 'lastname':'Brooks','age': 24,'city': 'Spb'},
#	{'id':2, 'name':'John', 'lastname':'Stones','age': 15,'city':'Spb'},
#	{'id':3, 'name':'Andy', 'lastname':'Wings','age': 45,'city': 'Manhester'},
#	{'id':4, 'name':'Kate', 'lastname':'Brooks','age': 34,'city': 'Spb'}
# ]
#Students.insert_many(st).execute()

#cour=[
#    {'id':1,'name':'python','time_start':'21.07.21','time_end':'21.08.21'},
#    {'id':2,'name':'java','time_start': '13.07.21', 'time_end':'16.08.21'}
# ]
#Courses.insert_many(cour).execute()

#StCour = [
#    {'student_id': 1, 'course_id': 1},
#    {'student_id': 2, 'course_id': 1},
#    {'student_id': 3, 'course_id': 1},
#    {'student_id': 4, 'course_id': 2}
# ]
#Student_Courses.insert_many(StCour).execute()


over_30 = Students.select().where(Students.age > 30)
for i in over_30:
    print('Students over 30 are: ', i.name)

python_student = Students.select().join(Student_Courses).where(Student_Courses.courses_id == 1)
for j in python_student:
    print('Students learning Python are: ', j.name)

python_student_spb = Students.select().join(Student_Courses).where(Student_Courses.courses_id == 1, Students.city == 'Spb')
for k in python_student_spb:
    print('Students from Spb learning Python are: ', k.name)

conn.commit()
conn.close