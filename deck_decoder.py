import re
class DeckDecoder:
    BasicEnergyMap = {
        "Grass": "G",
        "Fire": "R",
        "Water": "W",
        "Lightning": "L",
        "Psychic": "P",
        "Fighting": "F",
        "Darkness": "D",
        "Metal": "M"
    }
    BasicEnergyP = re.compile("[0-9]+ (%s) Energy [0-9]+"%("|".join(BasicEnergyMap.keys())))
    SectionP = re.compile("(Pokémon|Trainer|Energy) \([0-9]+\)")

    def __init__(self, deck_file):
        self.deck_file = deck_file
        self.cards = []
        with open(self.deck_file, 'r') as deck_content:
            section = ""
            for line in deck_content.readlines():
                if not line.strip():
                    continue
                m = self.SectionP.match(line.strip())
                if line and m:
                    section = m.groups()[0]
                    continue
                split = line.strip().split()
                while True:
                    copies = int(split[0])
                    match_res = self.BasicEnergyP.match(line.strip())
                    if match_res:
                        card_idx_in_seriers = self.BasicEnergyMap[match_res.groups()[0]]
                        seriers_name = "BRS"
                        break
                    seriers_name = split[-2]
                    card_idx_in_seriers = split[-1]
                    break
                print(line, copies, seriers_name, card_idx_in_seriers)
                self.cards.append((copies, seriers_name, card_idx_in_seriers))

            
        