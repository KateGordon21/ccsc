import sys
"""
Robert and his F-1 buddies have started college this Fall. Unfortunately, they were late in choosing
courses and found that already S students have enrolled for different courses before them. Each course has
an associated number with it ranging from 1 to N. The conditions for choosing courses are as follows:
They will choose the course i (1 <= i <= N), for which the value of v is minimum. Here, v =
y*z where z is the number of students already enrolled in the course i, and y is the sum of IQ of the last
two students who enrolled in that course. If a single student has applied for a course, then the value
of y will be that student's IQ. If no student has enrolled for that course, then value of y will be 0. If the
value of v is same for two courses, then they will choose the course with the minimum course number.
You need to find which courses Robert and his friends should take after following the above conditions.
"""

def assign_students(courses, students):
    output_log = []
    for i in range(len(students)):
        # Find next minimum v, then assign student
        next_course = find_min_v(courses)
        courses[next_course].append(students[i])
        output_log.append(next_course+1)
    
    return output_log

def find_min_v(courses):
    min_v = sys.maxsize
    next_course = None
    for course in courses:
        if len(courses[course]) == 0:
            return course
        elif len(courses[course]) == 1:
            if courses[course][0] < min_v:
                min_v = courses[course][0]
                next_course = course
        else:
            v = len(courses[course]) * (courses[course][-1] + courses[course][-2])
            if v < min_v:
                min_v = v
                next_course = course
    return next_course

if __name__ == "__main__":
    # Gathering input
    n, f, s = input().split()
    n, f, s = int(n), int(f), int(s)

    s_iq_list = input().split()
    for i in range(len(s_iq_list)):
        s_iq_list[i] = int(s_iq_list[i])
        
    f_iq_list = input().split()
    for i in range(len(f_iq_list)):
        f_iq_list[i] = int(f_iq_list[i])

    # Initialize courses
    courses = dict()
    for i in range(n):
        courses[i] = []

    # Assigning s students to courses
    for i in range(s):
        courses[i].append(s_iq_list[i])

    # Now, assign each f student to a course
    log = assign_students(courses, f_iq_list)

    for i in range(len(log)-1):
        print(log[i], end=" ")
    print(log[-1])