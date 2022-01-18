from cac_lop import Result,Part_Learning,Subject, Majors,Student
import pickle
class Student_Viewer():
    lit = []
    def nhapdulieusv(self) -> Student:

            name = input("Họ tên: ")
            sdt = input("Số điện thoai: ")
            email = input("Dia chi email: ")
            mssv = input("Ma so sinh vien: ")
            svn = int(input("sinh viên năm: "))

            mn = input(" mã ngành: ")
            tn = input(" tên ngành: ")

            mmh = input(" mã môn học : ")
            tmh = input(" tên môn học : ")

            stc = int(input("số tín chỉ: "))
            st = int(input("số tiết: "))

            dkt = float(input(" điểm kiểm tra: "))
            dtb = float(input(" điểm Tb: "))

            f = Result(dkt, dtb)
            t = Part_Learning(stc, st, f)
            r = Subject(mmh, tmh, t)

            e = Majors(mn, tn)
            sv = Student(name, sdt, email, mssv, svn, e, r)
            self.lit.append(sv)
            sv._name = name
            sv._sdt = sdt
            sv._email = email
            sv._mssv = mssv
            sv._svn = svn
            sv._mn = mn
            sv._tn= tn
            sv._tmh = tmh
            sv._mmh=mmh
            sv._stc= stc
            sv._st = st
            sv._dtb = dtb
            sv._dkt = dkt

            return sv
    def showSinhVien(self,lit):
        print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("Name", "sdt", "email", "mssv", "svn","mn", "tn", "mmh","tmh","stc","st","dkt","dtb"))
        if (lit.__len__() > 0):
            for sv in lit:
                print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(sv._name,sv._sdt,sv._email,sv._mssv,sv._svn,sv._mn, sv._tn, sv._mmh,sv._tmh,sv._stc,sv._st,sv._dkt,sv._dtb))
        print("\n")
    def sap_xep(self):
        self.lit.sort(key=lambda x: x._name,reverse=False)
    def tim_kiem(self,lit):
        listsv=[]
        for sv in self.lit :
            if lit == sv._name:
                listsv.append(sv)
            return listsv


def main():
    svView = Student_Viewer()
    list1 = []
    print("mời nhập số lượng sinh viên :")
    n = int(input())
    for i in range(n):
        print("người thứ ", i + 1)
        sv = svView.nhapdulieusv()
        list1.append(Student.outputStudent(sv),)
        print(Student.outputStudent(sv))
    chenk = 1
    while chenk != 0:
        print("Nhập 1: Hiện Danh sách Sinh Viên  ")
        print("Nhập 2: Xắp xếp sinh viên")
        print("nhập 3: Tìm Kiếm Sinh Viên")
        print("nhập 4: luu tệp sinh viên")
        print("nhập bất kỳ để kết thúc")
        chenk = int(input())

        if chenk == 1:
            print(" Danh Sách Sinh Viên")
            print((list1))
            print("\n")
            svView.showSinhVien(svView.lit)
        elif chenk == 2:
            print('XẮP Xếp Sinh Viên Theo Tên')
            svView.sap_xep()
            svView.showSinhVien(svView.lit)
            print("\n")
            n1 = sorted(list1, reverse=False)
            print(n1)
            print("\n")
        elif chenk == 3:
            print('tìm kiếm SINH VIÊN theo tên')
            name = input("nhập tên cần tìm :")
            if (svView.tim_kiem(name)):
                svView.showSinhVien(svView.tim_kiem(name))
            else:
                print("Không  tìm thấy Sinh viên")

        elif chenk == 4 :
            print("lưu Và Mở tệp SINH VIÊN ")
            s = open("Student", "wb")
            pickle.dump(list1, s)
            s.close()
            print("Mở tệp")
            s = open("Student", "rb")
            print("Student\n", pickle.load(s))
            s.close()
        else:
            break
if __name__ == '__main__':
    main()
