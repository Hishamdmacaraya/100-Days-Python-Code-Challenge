print('Welcome to Grade Estimator for Outlier.org Astronomy')
print('Disclaimer: This is not an official version.')
print()
print('Instruction: Type your grade (%) in the promt. Type "0" if not yet graded.')

print()
close_reading_essay = float(input('What is your close essay grade? '))/100*16 
print('Close Reading Essay =',close_reading_essay, '%', 'out 16%')

print()
lens_essay = float(input('What is your lens essay grade? '))/100*20 
print('Lens Essay =', lens_essay, '%', 'out 20%')

print()
research_essay = float(input('What is your research essay grade? '))/100*25 
print('Research Essay =', research_essay, '%', 'out 25%')

print()
participation = float(input('What is your participation grade? '))/100*5 
print('Participation =', participation, '%', 'out 20%')

print()
quiz1 = float(input('What is your total quiz 1 grade? '))
quiz2 = float(input('What is your total quiz 2 grade? '))
quiz3 = float(input('What is your total quiz 3 grade? '))
quiz4 = float(input('What is your total quiz 4 grade? '))
quiz5 = float(input('What is your total quiz 5 grade? '))
quiz6 = float(input('What is your total quiz 6 grade? '))
quiz7 = float(input('What is your total quiz 7 grade? '))
quiz8 = float(input('What is your total quiz 8 grade? '))
quiz9 = float(input('What is your total quiz 9 grade? '))
quiz10 = float(input('What is your total quiz 10 grade? '))
quiz11 = float(input('What is your total quiz 11 grade? '))
quiz12 = float(input('What is your total quiz 12 grade? '))
quiz13 = float(input('What is your total quiz 13 grade? '))
quiz14 = float(input('What is your total quiz 14 grade? '))
print()
quizzes = round(((quiz1 + quiz2 + quiz3 + quiz4 + quiz5 + quiz6 + quiz7 + quiz8 + quiz9 + quiz10 + quiz11 + quiz12 + quiz13 + quiz14)/14 / 100*14), 2)
print('Total Quizes =', quizzes, '%', 'out 14%')

print()
pre_writing1 = float(input('What is your total pre-writing 1 grade? '))
pre_writing2 = float(input('What is your total pre-writing 2 grade? '))
pre_writing3 = float(input('What is your total pre-writing 3 grade? '))
pre_writing4 = float(input('What is your total pre-writing 4 grade? '))
pre_writing5 = float(input('What is your total pre-writing 5 grade? '))
pre_writing6 = float(input('What is your total pre-writing 6 grade? '))
pre_writing7 = float(input('What is your total pre-writing 7 grade? '))
pre_writing8 = float(input('What is your total pre-writing 8 grade? '))
pre_writing9 = float(input('What is your total pre-writing 9 grade? '))
pre_writing10 = float(input('What is your total pre-writing 10 grade? '))
pre_writing11 = float(input('What is your total pre-writing 11 grade? '))
print()
pre_writing = round(((pre_writing1 + pre_writing2 + pre_writing3 + pre_writing4 + pre_writing5 + pre_writing6 + pre_writing7 + pre_writing7 + pre_writing8 + pre_writing9 + pre_writing10 + pre_writing11)/11 /100*14), 2)                  
print('Total Quizes =', pre_writing, '%', 'out 20%')

total_grade = close_reading_essay + research_essay + lens_essay + participation + quizzes + pre_writing
print()
print('Your Total Grade is: ', total_grade)
