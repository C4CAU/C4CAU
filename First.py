brand =  'GibHub'
cararc1 = 'interesting'
caract2 = 'complex'
project = 1

no = False 
yes = True
run = yes


def time(project):
  if project == 1:
    return 'first'
  elif project <= 5:
    return 'almost first'
  else:
    return 'not the first'

if run:
  print('Hello World from Py!')
  print(f'Just my {time(project)} simple test in {brand},')
  print(f'But... \nI\'m plaining in doing some more {carac2} and {carac2}')
