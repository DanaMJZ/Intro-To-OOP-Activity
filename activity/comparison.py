# add your get_student_with_more_classes function here!
def get_student_with_more_classes(claire, samara):
    if samara.get_num_classes() > claire.get_num_classes():
       return samara
    else:
       return claire