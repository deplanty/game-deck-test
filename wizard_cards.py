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
        self.button_new = tui.Button(self.frame_menu, "New")
        self.button_new.grid(0, 0)
        self.button_edit = tui.Button(self.frame_menu, "Edit")
        self.button_edit.grid(0, 1)
        self.button_prev = tui.Button(self.frame_menu, "  <  ")
        self.button_prev.grid(0, 2)
        self.button_next = tui.Button(self.frame_menu, "  >  ")
        self.button_next.grid(0, 3)
        self.button_quit = tui.Button(self.frame_menu, "Quit")
        self.button_quit.grid(0, 4)

        tui.Frame(parent).pack()

        # Card
        self.frame_card = tui.LabelFrame(parent, text="Card")
        self.frame_card.pack(fill=True)

        #   Buttons
        frame_buttons = tui.Frame(self.frame_card)
        frame_buttons.pack()
        self.button_valid = tui.Button(frame_buttons, "  Ok  ")
        self.button_valid.grid(0, 0)
        self.button_cancel = tui.Button(frame_buttons, "Cancel")
        self.button_cancel.grid(0, 1)

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
        #   Cycle over menu buttons
        self.button_new.focus_next = self.button_edit
        self.button_edit.focus_next = self.button_prev
        self.button_prev.focus_next = self.button_next
        self.button_next.focus_next = self.button_quit
        self.button_quit.focus_next = self.button_new
        # Cycle over button parameters
        self.button_valid.focus_next = self.button_cancel
        self.button_cancel.focus_next = self.entry_iid
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
        self.choice_bash.focus_next = self.button_valid

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
        self.card_new = None

        self.current = 0

        self.ui = CardWizardUi(self)
        self.ui.button_new.pressed.connect(self._on_button_new_pressed)
        self.ui.button_edit.pressed.connect(self._on_button_edit_pressed)
        self.ui.button_prev.pressed.connect(self._on_button_prev_pressed)
        self.ui.button_next.pressed.connect(self._on_button_next_pressed)
        self.ui.button_quit.pressed.connect(self._on_button_quit_pressed)
        self.ui.button_valid.pressed.connect(self._on_button_valid_pressed)
        self.ui.button_cancel.pressed.connect(self._on_button_cancel_pressed)

    def run(self):
        self.ui.button_new.focus_set()
        self.setup_card_current()

        self.action = ""
        while True:
            self.update()

            if self.action == "quit":
                break

    # Events

    def _on_button_new_pressed(self):
        next_iid = max(card.iid for card in self._all_cards) + 1
        self.card_new = Card(next_iid)
        self.ui.setup_card(self.card_new)
        self._on_button_edit_pressed()

    def _on_button_edit_pressed(self):
        self.ui.entry_iid.focus_set()

    def _on_button_prev_pressed(self):
        self.current -= 1
        if self.current < 0:
            self.current = len(self._all_cards) - 1

        self.setup_card_current()

    def _on_button_next_pressed(self):
        self.current += 1
        if self.current >= len(self._all_cards):
            self.current = 0

        self.setup_card_current()

    def _on_button_quit_pressed(self):
        self.action = "quit"
        self.save_cards()

    def _on_button_valid_pressed(self):
        # If it's a new card, save it
        if self.card_new:
            card = self.ui_to_card()
            self._all_cards.append(card)
            self.card_new = None
        # If it's an existing card, update it
        else:
            card = self.ui_to_card()

        self.ui.button_new.focus_set()

    def _on_button_cancel_pressed(self):
        self.ui.button_new.focus_set()

        # If its a new card, discard it
        if self.card_new:
            self.card_new = None
        # Reset to the current card
        self.setup_card_current()

    # Methods

    def setup_card_current(self):
        self.ui.setup_card(self._all_cards[self.current])

    def ui_to_card(self):
        card = Card(0)
        card.iid = int(self.ui.entry_iid.text)
        card.name = self.ui.entry_name.text
        card.cost = int(self.ui.entry_cost.text)
        card.description = self.ui.entry_description.text
        card.obtainable = True if self.ui.choice_obtainable.choice == "True" else False
        card.base_damage = int(self.ui.entry_damage.text)
        card.base_armor = int(self.ui.entry_armor.text)
        return card

    # Methods: load and save the cards

    def load_cards(self):
        self._all_cards = list()
        with open("resources/cards.toml") as fid:
            for iid, data in toml.load(fid).items():
                card :Card= Card.from_dict(iid, data)
                self._all_cards.append(card)

    def save_cards(self):
        data = {str(card.iid): card for card in self._all_cards}
        with open("tmp-cards-wizard.toml", "w") as fid:
            toml.dump(data, fid)


if __name__ == "__main__":
    app = CardWizard()
    app.run()
