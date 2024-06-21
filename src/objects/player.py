import copy

from src.components import Gauge, Buff
from src.objects import Card, Deck
import src.singleton as sgt


class Player:
    """
    Create a player.

    Args:
        iid (int): The player's unique id.
        max_health (int): The player's max health.
    """

    def __init__(self, iid:int, max_health:int, max_energy:int):
        self.iid = int(iid)

        self.name = ""
        self.health = Gauge(max_health)
        self.energy = Gauge(max_energy)
        self.deck = Deck()
        self.hand_size = 2
        # Buffs
        self.armor = Buff("Armor")
        self.strenght = Buff("Strenght")
        self.resistance = Buff("Resistance")
        self.thorn = Buff("Thorn")
        self.buffs = [self.armor, self.strenght, self.resistance, self.thorn]
        # Debuff
        self.burn = Buff("Burn")
        self.poison = Buff("Poison")
        self.weakness = Buff("Weakness")
        self.debuffs = [self.burn, self.poison, self.weakness]
        # Augment
        self.augments = list()

    def __str__(self) -> str:
        return f"{self.name}(HP: {self.health}, EP: {self.energy})"

    def __repr__(self) -> str:
        return str(self)

    # Properties

    @property
    def info(self) -> str:
        """Returns the information of the player"""

        text = list()
        text.append(f"Energy = {self.energy}")
        text.append(f"Deck = {self.deck.info}")
        for buff in self.buffs:
            if buff.info: text.append(f"+ {buff.info}")
        for debuff in self.debuffs:
            if debuff.info: text.append(f"- {debuff.info}")
        return "\n".join(text)

        # Class methods

    @classmethod
    def from_dict(cls, iid:int, data:dict):
        """
        Return a player with all its data from a dict.

        Args:
            iid (int): The player's unique id.
            data (dict): All the data needed.

        Returns:
            Player: The build player from dict.
        """

        player = cls(iid, data["hp"], data["energy"])
        player.name = data["name"]
        player.hand_size = data["hand_size"]
        for card_iid in data["deck"]:
            player.add_card_from_id(card_iid)
        return player

    # Method

    def is_alive(self) -> bool:
        """Return True if the player is alive."""

        return self.health > 0

    def start_of_combat(self):
        """
        Prepare the player at the start of combat: reform and shuffle the deck, process augments.
        """

        self.deck.reform_and_shuffle()

        for augment in self.augments:
            if augment.trigger == "start of combat":
                self.strenght += augment.strenght
                self.resistance += augment.resistance

    def start_of_turn(self):
        """
        Make all the start of turn actions: discard hand, draw new hand, reset armor, ...
        """

        self.deck.discard_hand()
        self.deck.draw(self.hand_size)
        self.energy.refill()
        self.armor.value = 0
        # Apply start of turn debuff
        self.health -= self.poison
        self.poison -= 1

    def end_of_turn(self):
        """
        Make all the en of turn actions: apply buffs and debuffs
        """

        self.health -= self.burn
        self.burn -= 1
        self.weakness -= 1

    def play_card(self, index:int) -> Card:
        """
        Play the card given by its index.
        If the player doesn't have enough energy, return None.

        Args:
            index (int): index of the card in the hand.

        Returns:
            Card: The card being played.
        """

        if len(self.deck.hand) <= 0:
            return None

        card = self.deck.hand[index]
        if self.energy < card.cost:
            return None

        self.energy -= card.cost
        return self.deck.play_from_hand(index)

    def get_buff(self, card:Card):
        """
        The player gets the buffs granted by a card.

        Args:
            card (Card): The card applying its effects on the player.
        """

        self.health -= card.hurt
        self.health += card.heal
        self.energy += card.energy

        self.strenght += card.strenght
        self.resistance += card.resistance
        self.armor += card.armor
        self.thorn += card.thorn
        self.deck.draw(card.draw)

    def get_hit(self, card:Card):
        """
        The player gets hit by a card and apply the effect of the card.

        Args:
            card (Card): The card applying its effects on the player.
        """

        # The card deal damage to the armor. If the armor drops to 0, damage the player.
        if card.damage >= self.armor:
            damage = card.damage - self.armor
            self.armor.value = 0
            self.health -= damage
        else:
            self.armor -= card.damage

        self.burn += card.burn
        self.poison += card.poison
        self.weakness += card.weakness

        # The owner of the card take dame for each stack of thorn
        card.owner.health -= self.thorn

    def copy(self):
        """Return a copy of the player."""

        return copy.deepcopy(self)

    def add_card_from_id(self, iid:int):
        card = sgt.card_from_id(iid)
        card.owner = self
        self.deck.add(card)

    def add_augment_from_id(self, iid:int):
        augment = sgt.augment_from_id(iid)
        self.augments.append(augment)

        if augment.trigger == "get":
            self.health.maximum += augment.max_hp
