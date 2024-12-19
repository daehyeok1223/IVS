class GameMachine :
    def __init__(self):
        self.coin = 0

    def input_coin(self, cnt):
        if self.coin > 10:
            return
        if self.coin + cnt > 5:
            print('코인이 너무 많습니다')
        else:
            self.coin += cnt
    
    def show_status(self):
        print(f'남아있는 코인은 {self.coin}입니다')
    
    def play_game(self):
        if self.coin > 0:
            print('게임 재밌다')
            self.coin -= 1
        else: 
            print('코인이 부족합니다')
            return
gm = GameMachine()
gm.input_coin(5)
gm.show_status()
gm.play_game()
gm.play_game
gm.input_coin(3)
gm.show_status()
