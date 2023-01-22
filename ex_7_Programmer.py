class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        if self.language == new_language:
            return f"{self.name} already knows {new_language}"
        if self.language != new_language and skills_needed > self.skills:
            needed_skills = skills_needed - self.skills
            return f"{self.name} needs {needed_skills} more skills"
        if self.language != new_language and skills_needed <= self.skills:
            current_language = self.language
            self.language = new_language
            return f"{self.name} switched from {current_language} to {new_language}"
programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
