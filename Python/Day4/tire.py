class Mtire:
    def run(self):
        print('런')

class Stire(Mtire):
    def ran(self):
        print('랜')

class Dtire(Mtire):
    def run(self):
        print('런런')#overriding(재정의)
    def ron(self):
        print('론')
a = Mtire()
b = Stire()
c = Dtire()

a.run()
b.ran()
c.run()
c.ron()