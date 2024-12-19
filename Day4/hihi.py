class Person:
    def walk(self):
        print("사람이 걷는다")
class SuperMan(Person):
    def fly(self):
        print('난다')#상속으로 walk사용 가능
    def walk(self):
        print('슈퍼맨이 걷는다')#overriding(재정의)