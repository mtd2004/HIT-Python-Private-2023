class Job:
    def __init__(self, job_id, job_name, industry, salary):
        self.job_id = job_id
        self.job_name = job_name
        self.industry = industry
        self.salary = salary

    def evaluate(self):
        pass

class AI(Job):
    def __init__(self, job_id, job_name, industry, salary, python_skill, ml_skill, deep_skill, math_skill):
        super().__init__(job_id, job_name, industry, salary)
        self.python_skill = python_skill
        self.ml_skill = ml_skill
        self.deep_skill = deep_skill
        self.math_skill = math_skill

    def evaluate(self):
        avg_skill = (self.python_skill + self.ml_skill + self.deep_skill + self.math_skill) / 4
        if avg_skill > 9.0:
            return "Rất phù hợp"
        elif avg_skill > 7.0:
            return "Phù hợp"
        elif avg_skill > 5.0:
            return "Tạm được"
        elif avg_skill > 3.0:
            list_skills = []
            if self.python_skill < 4.0:
                list_skills.append("Python")
            if self.ml_skill < 4.0:
                list_skills.append("Machine Learning")
            if self.deep_skill < 4.0:
                list_skills.append("Deep Learning")
            if self.math_skill < 4.0:
                list_skills.append("Mathematics")
            return f"Cần bổ sung kiến thức về: {', '.join(list_skills)}"
        else:
            return "Cần học lại kiến thức cơ bản"

class Backend(Job):
    def __init__(self, job_id, job_name, industry, salary, sql_skill, oop_skill, api_skill, java_skill):
        super().__init__(job_id , job_name , industry , salary)
        # self.job_id = job_id
        # self.job_name = job_name
        # self.industry = industry
        # self.salary = salary
        self.sql_skill = sql_skill
        self.oop_skill = oop_skill
        self.api_skill = api_skill
        self.java_skill = java_skill

    def evaluate(self):
        avg_skill = (self.sql_skill + self.oop_skill + self.api_skill + self.java_skill) / 4
        if avg_skill > 9.0:
            return "Rất phù hợp"
        elif avg_skill > 7.0:
            return "Phù hợp"
        elif avg_skill > 5.0:
            return "Tạm được"
        elif avg_skill > 3.0:
            list_skills = []
            if self.sql_skill < 4.0:
                list_skills.append("SQL")
            if self.oop_skill < 4.0:
                list_skills.append("OOP")
            if self.api_skill < 4.0:
                list_skills.append("API")
            if self.java_skill < 4.0:
                list_skills.append("Java")
            return f"Cần bổ sung kiến thức về: {', '.join(list_skills)}"
        else:
            return "Cần học lại kiến thức cơ bản"

class Frontend(Job):
    def __init__(self, job_id, job_name, industry, salary, html_skill, css_skill, nodejs_skill, ux_skill, ui_skill):
        super().__init__(job_id, job_name, industry, salary)
        self.html_skill = html_skill
        self.css_skill = css_skill
        self.nodejs_skill = nodejs_skill
        self.ux_skill = ux_skill
        self.ui_skill = ui_skill

    def evaluate(self):
        avg_skill = (self.html_skill + self.css_skill + self.nodejs_skill + self.ux_skill + self.ui_skill) / 5
        if avg_skill > 9.0:
            return "Rất phù hợp"
        elif avg_skill > 7.0:
            return "Phù hợp"
        elif avg_skill > 5.0:
            return "Tạm được"
        elif avg_skill > 3.0:
            list_skills = []
            if self.html_skill < 4.0:
                list_skills.append("HTML")
            if self.css_skill < 4.0:
                list_skills.append("CSS")
            if self.nodejs_skill < 4.0:
                list_skills.append("Node.js")
            if self.ux_skill < 4.0:
                list_skills.append("UX")
            if self.ui_skill < 4.0:
                list_skills.append("UI")
            return f"Cần bổ sung kiến thức về: {', '.join(list_skills)}"
class Fullstack(Backend, Frontend):
    def __init__(self, job_id, job_name, industry, salary, sql_skill, oop_skill, api_skill, java_skill, html_skill, css_skill, nodejs_skill, ux_skill, ui_skill):
        Backend.__init__(self, job_id, job_name, industry, salary, sql_skill, oop_skill, api_skill, java_skill)
        Frontend.__init__(self, job_id, job_name, industry, salary, html_skill, css_skill, nodejs_skill, ux_skill, ui_skill)

    def evaluate(self):
        backend_avg = (self.sql_skill + self.oop_skill + self.api_skill + self.java_skill) / 4
        frontend_avg = (self.html_skill + self.css_skill + self.nodejs_skill + self.ux_skill + self.ui_skill) / 5
        avg_skill = (backend_avg + frontend_avg) / 2
        if avg_skill > 9.0:
            return "Rất phù hợp"
        elif avg_skill > 7.0:
            return "Phù hợp"
        elif avg_skill > 5.0:
            return "Tạm được"
        elif avg_skill > 3.0:
            list_skills = []
            if backend_avg < 4.0:
                list_skills.extend(["SQL", "OOP", "API", "Java"])
            if frontend_avg < 4.0:
                list_skills.extend(["HTML", "CSS", "Node.js", "UX", "UI"])
            return f"Cần bổ sung kiến thức về: {', '.join(list_skills)}"
        else:
            return "Cần học lại kiến thức cơ bản"

if __name__ == '__main__':
    ai_job = AI("J001", "AI Developer", "AI", 1000, 9.5, 8.0, 7.5, 9.0)
    frontend_job = Frontend("J002", "Frontend Developer", "Web Development", 800, 8.5, 9.0, 7.0, 8.0, 8.5)
    backend_job = Backend("J003", "Backend Developer", "Web Development", 900, 8.0, 8.5, 9.0, 7.5)
    fullstack_job = Fullstack("J004", "Full Stack Developer", "Web Development", 1200, 7.5, 8.0, 8.5, 8.0, 8.0, 8.5,8.0, 8.0, 8.5)

    # In thông tin và đánh giá của các đối tượng
    print("Thông tin và đánh giá của AI Developer:")
    print(ai_job.__dict__)
    print("Đánh giá:", ai_job.evaluate())

    print("Thông tin và đánh giá của Frontend Developer:")
    print(frontend_job.__dict__)
    print("Đánh giá:", frontend_job.evaluate())

    print("Thông tin và đánh giá của Backend Developer:")
    print(backend_job.__dict__)
    print("Đánh giá:", backend_job.evaluate())

    print("Thông tin và đánh giá của Full Stack Developer:")
    print(fullstack_job.__dict__)
    print("Đánh giá:", fullstack_job.evaluate())
