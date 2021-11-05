eng2uz = dict()
eng2uz2 = {}
student = { 'name': 'Alokhon',
            'id': '11776',
            'course': 'BIS'}
eng2uz['one'] = 'bir'


print(eng2uz)
print(eng2uz2)
print(student)
print(student['name'])
print(len(student))
print('one' in eng2uz)
print('name' in eng2uz2)
print('Alokhon' in student['name'])

values = student.values()
print('module' in values)

myFinalMarks = {'CSF': 75,
                'FunPro': 80,
                'WT': 85}
#rtest