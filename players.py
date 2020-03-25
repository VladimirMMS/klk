from pro import total,creation,will, cumcolor
import random 
class Players:
    def __init__(self, name):
        self.name = name
        self.deck_of_player = []
        self.score = 0
        self.deck_table = []
        

    def Distribute_of_deck(self):
        random.shuffle(total)
        for i in range(7):
            card1 = total.pop(0)
            self.deck_of_player.append(card1)
        card_table = total.pop(0)
        self.deck_table.append(card_table)


    def Behavior_of_deck(self):
        for ve in will:
            if ve == self.deck_table[0]:
                take = (input('Introduce el nombre de la carta que quitar sacar:'))
                for leng in range(len(self.deck_of_player)):
                    for walk in self.deck_of_player:
                        if walk == take:
                            self.deck_of_player.pop(leng)
                            self.deck_table.append(take)
            else:
                for n_c in range(len(self.deck_of_player)):
                    if deck_table[0] == deck_of_player[0][n_c] or deck_table[1] == deck_of_player[0][n_c]:
                        take = (input('Indroduce la carta que quieres sacar:'))
                        re = deck_of_player.pop(n_c)
                        self.deck_table.append(re)
                        
                    


    def Mov_of_player(self):
        colors_spe = ['Blue', 'Red', 'Yellow','Green']
        self.score = 0
        while self.score == 500:
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
                        for colors in colors_spe:
                            if colors in take:
                                self.deck_table.append(take)



PlayerList = []


def input_player():
  check = '234'
  inputopcion = input("Entre numero de player:")
  if len(inputopcion) != 1:
      print("NO es valida")
  while inputopcion not in check:
    print("NO es valida")
    inputopcion = input("Entre numero de player:")
  return int(inputopcion)

def creator_of_player():
  verify_entre = input_player()
  for v_p in range(verify_entre):
    input_name = input("Entre nombre player{}:".format(v_p + 1))
    if len(input_name) == 0 or len(input_name) > 20:
      print("El nombre no es valido, vuelve a internar")
      input_name = input("Entre nombre player{}:".format(v_p + 1))
    PlayerList.append(input_name)
  return PlayerList

input_player()
creator_of_player()


if len(PlayerList) == 4:
  Player1 = Players(PlayerList[0])
  print(Player1.name)
  Player2 = Players(PlayerList[1])
  print(Player2.name)
  Player3 = Players(PlayerList[2])
  print(Player3.name)
  Player4 = Players(PlayerList[3])
  print(Player4.name)
if len(PlayerList) == 3:
  Player1 = Players(PlayerList[0])
  print(Player1.name)
  Player2 = Players(PlayerList[1])
  print(Player2.name)
  Player3 = Players(PlayerList[2])
  print(Player3.name)
if len(PlayerList) == 2:
  Player1 = Players(PlayerList[0])
  print(Player1.name)
  Player2 = Players(PlayerList[1])
  print(Player2.name)













# player1 = Players()
# player1.esa()







#                 else:
#                     if deck_of_player[0][walk] == deck_table[0]:

#                     self.deck_of_player in self.deck_of_table[0]:
# self.deck_of_player.remove(deck_of_table[0])
