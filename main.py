class Student:
    def __init__(self, name, surname, age, group, money, moni, marks):
        self.name = name
        self.surname = surname
        self.age = age
        self.group = group
        self.money = money
        self.moni = moni
        self.marks = marks

    def info(self):
        print(f"Student {self.name} {self.surname}")



    def mon(self):
        self.money = float(input("Веддіть свій заробіток на даний момент:"))
        if (self.money) < 500:
                print("заробляй гроші, і краще вчися")
        elif (self.money) > 1000:
            print("Ти успішний в заробітку грошей")
        else:
            print("Ти можеш навчатися і заробляти гроші забажанням")
        print(f'money = {self.money}')
    def mone(self):
        self.moni = float(input("Веддіть свій заробіток за місяць:"))
        print(f'money = {self.money + self.moni * 12 - 1250}')
        if (self.money + self.moni * 12) > 12000:
            print("Ви проживете 1 рік сміло")
        else:
            print("Ви маєте більше старатися, бо в вас не вийде прожити 1 рік")

    def average(self):
        return sum(self.marks) / len(self.marks)

student1 = Student(
    "Vlad",
    "Gesshin",
    27,
    "Hg17",
    0,
    0,
    [5, 8, 7, 9, ],

)
student2 = Student(
    "Valentin",
    "Bobyk",
    23,
    "HG13",
    0,
    0,
    [10, 12, 11, 7, 1, 3, 9, 7, 6, 8, 12, 12, 10],

)
student1.info()
student1.mon()
student1.mone()
print(student1.average())
student2.info()
student2.mon()
student2.mone()
print(student2.average())
