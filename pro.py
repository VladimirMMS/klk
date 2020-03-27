class Deck:
    def __init__(self,color,number,ability, ability_well):
        self.color = color
        self.number = number
        self.ability = ability
        self.ability_well = ability_well



class Table:
    def __init__(self):
        self.decks = [] 
    
    def creation_of_card(self):
        colors = ['Blue', 'Red', 'Yellow','Green']
        colors_argu = []
        number_argu = []
        for color_0 in colors:
            for n in range(0,10):
                colors_argu.append(color_0)
                number_argu.append(n)
                self.decks.append([color_0, n])
        for color_1 in colors:
            for n in range(1,10):
                colors_argu.append(color_1)
                number_argu.append(n)
                self.decks.append([color_1, n])
        return [colors_argu,number_argu]
        
    def creation_of_special_deck(self):
        colors_spe = ['Blue', 'Red', 'Yellow','Green']
        abilities = ['Cancelation','Direction', 'sum_tow']
        ability_special = []
        for color in colors_spe:
            for ability in abilities:
                ability_special.append([color,ability])
                self.decks.append([color,ability])
        for color in colors_spe:
            for ability in abilities:
                ability_special.append([color,ability])
                self.decks.append([color,ability])
        return ability_special
    def creation_of_willcard(self):
        ability_willcard = ['change_of_color', 'change_of_color+4','change_of_color', 'change_of_color+4','change_of_color', 
                                'change_of_color+4','change_of_color', 'change_of_color+4']
        ability_will = []
        for ability_w in ability_willcard:
            ability_will.append([ability_w])
            self.decks.append([ability_w])
        return ability_will
    
jugador = Table()
num_color = jugador.creation_of_card()
creation = jugador.creation_of_special_deck()
will = jugador.creation_of_willcard()
total = jugador.decks

cumcolor = []
for p in range(0,len(num_color[0])):
    st = ""
    st += str(num_color[0][p])
    st +=  " " + str(num_color[1][p])
    cumcolor.append(st)
    st = ""
    












# class Deck_special:
#     def __init__(self,ability,color):
#         self.color = color
#         self.ability = ability

# class Table_s:
#     deck_spe = []



    


# mesa_s = Table_s()
# mesa_s.creation_of_special_deck()
# for deck_s in mesa_s.deck_spe:
#     print(deck_s.ability, deck_s.color)
    
# class Deck_willcard:
#     def __init__(self,ability):
#         self.ability = ability

# class Table_w:
#     def __init__(self):
#         self.deck_will = []
    


# mesa_w = Table_w()
# mesa_w.creation_of_willcard()
# for deck_w in mesa_w.deck_will:
#     print(deck_w.ability)







