from pro import total,creation,will, cumcolor
import random 
class Players:
    def __init__(self, name, deck_of_player):
        self.name = name
        self.deck_of_player = []

    def deck_of_table(self, deck_table):
        self.deck_table = []
        

    def Distribute_of_deck(self):
        random.shuffle(total)
        for i in range(7):
            card1 = total.pop(0)
            self.player_deck.append(card1)
        card_table = total.pop(0)
        self.deck_table.append(card_table)
        
    def Behavior_of_deck(self):
        # score = 0
        # while score == 500:
        for ve in will:
            for ve_c in creation:
                if ve == self.deck_table[0] or ve_c == self.deck_table[0]:
                    take = (input('Introduce el nombre de la carta que quitar sacar:'))
                    for leng in range(len(self.deck_of_player)):
                        for walk in self.deck_of_player:
                            if walk == take:
                                self.deck_of_player.pop(leng)
                                self.deck_table.append(take)
                for n_c in range(len(self.deck_table)):
                    if deck_table[0] == deck_of_player[0][e] or deck_table[1] == deck_of_player[0][e]:
                        take = (input('Indroduce la carta que quieres sacar:'))
                        re = deck_of_player.pop(0)
                        self.deck_table.append(re)
    
    
    def Mov_of_player(self, Player):
        colors_spe = ['Blue', 'Red', 'Yellow','Green']
        score = 0
        while score == 500:
            take = input('Enter the card your want:')
            if take == 'change_of_color':
                for i in range(0, len(self.deck_of_player)):
                    if self.deck_of_player[i] == take:
                        dele = self.deck_of_player.pop(i)
                        self.deck_table.append(dele)
                        take = input('Enter a color:')
                        for colors in colors_spe:
                            if colors in take:
                                self.deck_table.append(take)
            if take == 'change_of_color+4':
                for i in range(0, len(self.deck_of_player)):
                    if self.deck_of_player[i] == take:
                        dele = self.deck_of_player.pop(i)
                        self.deck_table.append(dele)
                        take = input('Enter a color')
                        
                        











# player1 = Players()
# player1.esa()







#                 else:
#                     if deck_of_player[0][walk] == deck_table[0]:

#                     self.deck_of_player in self.deck_of_table[0]:
# self.deck_of_player.remove(deck_of_table[0])
