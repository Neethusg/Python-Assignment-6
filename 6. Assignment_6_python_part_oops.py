

# Question 1

class CourseDetails:
    def __init__(self, course_code: str, course_name: str, credit_hours: int):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_details(self):
        return f"{self.course_code}: {self.course_name} ({self.credit_hours} credit hours)"

class CoreCourse:

    def __init__(self, details: CourseDetails, required_for_major: bool):
        self.details = details
        self.required_for_major = required_for_major

    def display_info(self):
        requirement_status = "Required" if self.required_for_major else "Not Required"
        return f"{self.details.display_details()} - {requirement_status} for major"

class ElectiveCourse:

    def __init__(self, details: CourseDetails, elective_type: str):
        self.details = details
        self.elective_type = elective_type

    def display_info(self):
        return f"{self.details.display_details()} - Elective Type: {self.elective_type}"


if __name__ == "__main__":
    cs101_details = CourseDetails("CS101", "Introduction to Computer Science", 3)
    hist201_details = CourseDetails("HIST201", "World History", 3)

    core_course = CoreCourse(cs101_details, True)
    elective_course = ElectiveCourse(hist201_details, "liberal arts")

    print(core_course.display_info())
    print(elective_course.display_info())

