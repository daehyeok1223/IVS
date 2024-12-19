class Zergling:
    def __init__(self):
        self.hp = 20
        self.mana = 50
    
    def run(self):
        print("뛴다")
        self.hp += 1
        self.mana += 1

    def show_stats(self):
        print(self.hp,self.mana)
    
z1 = Zergling()
z2 = Zergling()

z1.run()
z1.show_stats()
for _ in range(5):
    z2.run()
z2.show_stats()
        



#저글링의 체력, 마나, 공격력 등은 필드,
#저글링의 공격하는 행동 , 뛰는 행동 등은 메서드 라고할 수 있다.