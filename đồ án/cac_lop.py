class Majors():

    ID_majors: str
    majors_name: str

    def __init__(self, ma_nganh: str, ten_nganh: str) -> None:
        super().__init__()

        self.ID_majors = ma_nganh
        self.majors_name = ten_nganh

    def outputMajors(self) -> str:

        result = "; mã ngành: " + self.ID_majors + "; tên ngành: " + self.majors_name
        return result


class Result():

    checkpoint: float
    average_score: float

    def __init__(self, diem_kiem_tra: float, diem_tb: float) -> None:
        super().__init__()

        self.checkpoint = diem_kiem_tra
        self.average_score = diem_tb

    def outputResult(self) -> str:

        result = "; điểm kiểm tra: " + str(self.checkpoint) + "; điểm tb: " + str(self.average_score)
        return result


class Part_Learning():

    credit_number: int
    thym_number: int
    lesult: list[Result]

    def __init__(self, so_tin_chi: int, so_tiet: int, ket_qua: list[Result]) -> None:
        super().__init__()

        self.credit_number = so_tin_chi
        self.thym_number = so_tiet
        self.lesult = ket_qua

    def outputPart_Learning(self) -> str:
        result = "; số tín chỉ: " + str(self.credit_number) + "; số tiết : " + str(self.thym_number)  + self.lesult.outputResult()
        return result


class Subject():

    Subject_ID: str
    Subject_name: str
    part_Learning: list[Part_Learning]

    def __init__(self, ma_mon_hoc: str, ten_mon_hoc: str, hoc_phan: list[Part_Learning]) -> None:
        super().__init__()
        self.Subject_ID = ma_mon_hoc
        self.Subject_name = ten_mon_hoc
        self.part_Learning = hoc_phan

    def outputSubject(self) -> str:
        result = "; mã môn học : " + self.Subject_ID + "; tên môn học : " + self.Subject_name + self.part_Learning.outputPart_Learning()
        return result


class Person():

    name: str
    phone: str
    email: str

    def __init__(self, ten: str, sdt: str, email: str) -> None:
        super().__init__()

        self.name = ten
        self.phone = sdt
        self.email = email

    def outputPerson(self) -> str:

        result = "Họ tên: " + self.name + "; sđt: " + self.phone + "; email: " + self.email
        return result


class Student(Person):

    student_ID: str
    year_student: int
    majors: list[Majors]
    subject: list[Subject]

    def __init__(self, ten: str, sdt: str, email: str, ma_so_sv: str, sinh_vien_nam: int, nganh_hoc: list[Majors],mon_hoc: list[Subject]) -> None:
        Person.__init__(self, ten, sdt, email)

        self.studentID = ma_so_sv
        self.year_student = sinh_vien_nam
        self.majors = nganh_hoc
        self.subject = mon_hoc

    def outputStudent(self) -> str:

        result = self.outputPerson() + "; mã số SV: " + self.studentID + "; sinh viên năm : " + str(self.year_student) + self.majors.outputMajors() + self.subject.outputSubject()
        return result
