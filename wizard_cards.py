import toml

from src import tui
import src.singleton as sgt
from src.objects import Card


class CardWizardUi:
    def __init__(self, parent):
        self.parent = parent

        # Title
        self.frame_title = tui.LabelFrame(parent)
        self.frame_title.pack()
        self.label_title = tui.Label(self.frame_title, align="center")
        self.label_title.text = "Create and modify cards"
        self.label_title.pack()

        tui.Frame(parent).pack()

        # Menu
        self.frame_menu = tui.Frame(parent)
        self.frame_menu.pack()
        self.entry = tui.Entry(self.frame_menu)
        self.entry.pack()

        tui.Frame(parent).pack()

        # Card
        self.frame_card = tui.LabelFrame(parent, text="Card")
        self.frame_card.pack(fill=True)

        #   Required parameters
        self.frame_required = tui.LabelFrame(self.frame_card, text="Required")
        self.frame_required.pack()
        self.entry_iid = tui.Entry(self.frame_required, "ID: ")
        self.entry_iid.pack()
        self.entry_name = tui.Entry(self.frame_required, "Name: ")
        self.entry_name.pack()
        self.entry_cost = tui.Entry(self.frame_required, "Cost: ")
        self.entry_cost.pack()
        self.entry_description = tui.Entry(self.frame_required, "Description: ")
        self.entry_description.pack()
        self.choice_obtainable = tui.ChoiceLine(self.frame_required, "Obtainable:")
        self.choice_obtainable.pack()
        self.entry_damage = tui.Entry(self.frame_required, "Damage: ")
        self.entry_damage.pack()
        self.entry_armor = tui.Entry(self.frame_required, "Armor: ")
        self.entry_armor.pack()

        tui.Frame(self.frame_card).pack()

        frame = tui.Frame(self.frame_card)
        frame.pack()

        self.frame_buff = tui.LabelFrame(frame, text="Buff")
        self.frame_buff.grid(0, 0)
        self.entry_strenght = tui.Entry(self.frame_buff, "Strenght: ")
        self.entry_strenght.pack()
        self.entry_resistance = tui.Entry(self.frame_buff, "Resistance: ")
        self.entry_resistance.pack()
        self.entry_thorn = tui.Entry(self.frame_buff, "Thorn: ")
        self.entry_thorn.pack()

        self.frame_debuff = tui.LabelFrame(frame, text="Debuff")
        self.frame_debuff.grid(0, 1)
        self.entry_burn = tui.Entry(self.frame_debuff, "Burn: ")
        self.entry_burn.pack()
        self.entry_poison = tui.Entry(self.frame_debuff, "Poison: ")
        self.entry_poison.pack()
        self.entry_weakness = tui.Entry(self.frame_debuff, "Weakness: ")
        self.entry_weakness.pack()

        self.frame_effect = tui.LabelFrame(frame, text="Effects")
        self.frame_effect.grid(0, 2)
        self.entry_heal = tui.Entry(self.frame_effect, "Heal: ")
        self.entry_heal.pack()
        self.entry_energy = tui.Entry(self.frame_effect, "Energy: ")
        self.entry_energy.pack()
        self.entry_hurt = tui.Entry(self.frame_effect, "Hurt: ")
        self.entry_hurt.pack()
        self.entry_draw = tui.Entry(self.frame_effect, "Draw: ")
        self.entry_draw.pack()
        self.choice_bash = tui.ChoiceLine(self.frame_effect, "Bash: ")
        self.choice_bash.pack()

        # Init values for choices
        self.choice_obtainable.add_labels("True", "False")
        self.choice_bash.add_labels("True", "False")

        # Init focus and focus cycle
        self.entry.focus_next = self.entry_iid
        self.entry_iid.focus_next = self.entry_name
        self.entry_name.focus_next = self.entry_cost
        self.entry_cost.focus_next = self.entry_description
        self.entry_description.focus_next = self.choice_obtainable
        self.choice_obtainable.focus_next = self.entry_damage
        self.entry_damage.focus_next = self.entry_armor
        self.entry_armor.focus_next = self.entry_strenght
        self.entry_strenght.focus_next = self.entry_resistance
        self.entry_resistance.focus_next = self.entry_thorn
        self.entry_thorn.focus_next = self.entry_burn
        self.entry_burn.focus_next = self.entry_poison
        self.entry_poison.focus_next = self.entry_weakness
        self.entry_weakness.focus_next = self.entry_heal
        self.entry_heal.focus_next = self.entry_energy
        self.entry_energy.focus_next = self.entry_hurt
        self.entry_hurt.focus_next = self.entry_draw
        self.entry_draw.focus_next = self.choice_bash
        self.choice_bash.focus_next = self.entry

    def setup_card(self, card:Card):
        self.entry_iid.text = card.iid
        self.entry_name.text = card.name
        self.entry_cost.text = card.cost
        self.entry_description.text = card.description
        self.choice_obtainable.select_item(card.obtainable)
        self.entry_damage.text = card.base_damage
        self.entry_armor.text = card.base_armor
        self.entry_strenght.text = card.strenght
        self.entry_resistance.text = card.resistance
        self.entry_thorn.text = card.thorn
        self.entry_burn.text = card.burn
        self.entry_poison.text = card.poison
        self.entry_weakness.text = card.weakness
        self.entry_heal.text = card.heal
        self.entry_energy.text = card.energy
        self.entry_hurt.text = card.hurt
        self.entry_draw.text = card.draw
        self.choice_bash.select_item(card.bash)



class CardWizard(tui.Tui):
    def __init__(self):
        super().__init__()

        self.file_cards = "resources/cards.toml"
        self.load_cards()

        self.current = self._all_cards[0]

        self.ui = CardWizardUi(self)

    def run(self):
        self.ui.entry.focus_set()
        self.ui.setup_card(self.current)

        while True:
            self.update()

            if self.ui.entry.text == "exit":
                break

    # Methods: load and save the cards

    def load_cards(self):
        self._all_cards = list()
        for iid, data in toml.load("resources/cards.toml").items():
            card :Card= Card.from_dict(iid, data)
            self._all_cards.append(card)

    def save_cards(self):
        with open("test_cards.toml", "w") as fid:
            toml.dump(self._all_cards, fid)


if __name__ == "__main__":
    app = CardWizard()
    app.run()
