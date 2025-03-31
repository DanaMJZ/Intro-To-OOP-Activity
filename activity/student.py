# add your Student class here!
class Student:
    def __init__(self, name, grade, classes):
        
        self.name = name
        self.grade_level = grade
        self.classes = classes

    def add_class(self, class_name):
       
        return self.classes.append(class_name)

    def get_num_classes(self):
        
        return len(self.classes)