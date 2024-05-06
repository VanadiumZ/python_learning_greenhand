# 学生信息类：
# -学生信息：姓名，家乡，电话，课程及成绩
# -学生信息的输入，获取
# -学生课程成绩的评价
# -学生信息的输出
# 所有的input均要考虑覆写和原先空值的情况

class Student():

    def __init__(self, name, hometown='None', phone='None'):
        self.__name = name
        self.__hometown = hometown
        self.__phone = str(phone)
        self.__courses = {}

    def input_hometown(self, hometown):
        if self.__hometown != 'None':
            print("Warning: the exsiting hometown {0} is being changed into {1}.".format(self.__hometown, hometown))
        self.__hometown = hometown

    def input_phone(self, phone):
        if self.__phone != 'None':
            print("Warning: the exsiting phone number {0} is being changed into {1}".format(self.__phone, phone))
        self.phone = str(phone)

    def input_course_score(self, course, score):
        if score >= 0 and score <= 100:
            if self.__courses.get(course, -1) != -1:
                print("Warning: The exsiting {0} grade {1:.2f} is being changed into {2:.2f}.".format(
                    course, self.__coursess.get(course, -1), score))
            self.__course[course] = score
        else:
            print("Please input one valid course score!")

    def get_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone
    
    def get_hometown(self):
        return self.__hometown
    
    def get_course_grade(self, course):
        try:
            if self.__courses[course] >= 90:
                return 'A'
            elif self.__courses[course] >= 60:
                return 'B'
            else:
                return 'C'
        except:
            print("Course {0} doesn't exist.".format(course))

    def print_student_info(self):
        print('Name: {0}'.format(self.__name))
        print('Hometown: {0}'.format(self.__hometown))
        print('Phone: {0}'.format(self.__phone))
        if len(self.__courses) > 0:
            for course, score in self.__courses.items():
                print('Course {0}'.format(course, score))


# 创建研究生类来继承
# 继承self,name,hometown,phone
# 写入学生发表文章和本科专业信息输入
# 写入上述的信息获取
# 课程成绩覆盖，信息输出覆盖
            
class Graduate(Student):
    
    def __init__(self, name, hometown='None', phone='None'):
        super(Graduate, self).__init__(name, hometown, phone)
        self.__bachelor_major = 'None'
        self.__publication = []

    def input_paper(self, papers):
        #识别传入的paper数据类型
        if isinstance(papers, list):
            self.__publication = self.__publication + papers
        elif isinstance(papers,str):
            self.__publication.append(papers)
        else:
            print("Please organise the papers in str or list types!")

    def input_bachelor_major(self, major):
        self.__bachelor_major = major

    def get_publication(self):
        return self.__publication
    
    def get_bachelor_major(self):
        return self.__bachelor_major
    
    def get_course_grade(self, course):
        try:
            if self._Student__courses[course] >= 90:
                return 'A'
            elif self._Student__courses[course] >= 60:
                return 'B'
            else:
                return 'C'
        except:
            print("Course {0} doesn't exsit.".format(course))


    def print_student_info(self):
        print('Name: {0}'.format(self._Student__name))
        print('Hometown: {0}'.format(self._Student__hometown))
        print('Phone: {0}'.format(self._Student__phone))
        if len(self.__publication) > 0:
            for course, score in self._Student__courses.items():
                print('Course {0}: {1:.2f}'.format(course,score))

        if len(self.__publication) > 0:
            print('Publication:')
            for paper in self.__publication:
                print("{0:11} {1}".format('', paper))
