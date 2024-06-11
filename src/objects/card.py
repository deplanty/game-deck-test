import copy

from src.utils import Signal


class Card:
    """
    Create a card.

    Args:
        name (str): The name of the card.

    Signals:
        upgraded: triggers when the card is upgraded
    """

    upgraded:Signal

    def __init__(self, name:str):
        self.name = name
        self.owner:Player = None

        self.iid = 0
        self.name_full = ""
        self.cost = 0
        self.upgrades = 0
        self.description = ""

        self.base_damage = 0
        self.base_armor = 0
        # Buff
        self.strenght = 0
        self.resistance = 0
        # Debuff
        self.burn = 0
        self.poison = 0
        # Effects
        self.heal = 0
        self.energy = 0
        self.hurt = 0
        self.draw = 0

        # Signals
        self.upgraded = Signal()

    def __str__(self) -> str:
        if self.upgrades > 0:
            return f"Card({self.iid:03d}, {self.name}, +{self.upgrades})"
        else:
            return f"Card({self.iid:03d}, {self.name})"

    def __repr__(self) -> str:
        return str(self)

    # Properties

    @property
    def damage(self) -> int:
        """Return the calculated damage of the card."""

        # A card without base damage can't deal damage. It's to fix a problem where a "magic" card
        # deals direct damage when the strenght is greater than 0.
        if self.base_damage == 0:
            return 0
        else:
            damage = self.base_damage + self.upgrades
            if self.owner: damage += self.owner.strenght
            return damage

    @property
    def armor(self) -> int:
        """Return the calculated armor of the card."""

        # A card without base armor can't give amror. It's to fix a problem where a card whitout
        # amor can give it.
        if self.base_armor == 0:
            return 0
        else:
            armor = self.base_armor + self.upgrades
            if self.owner: armor += self.owner.resistance
            return armor

    @property
    def info(self) -> str:
        """Return the description of the card as text."""

        return self.description.format(card=self)

    @property
    def info_full(self) -> str:
        """Return the full information of the card as text."""

        text = f"{str(self)}\n"
        text += f"Cost = {self.cost}\n"
        text += self.description.format(card=self)
        return text

    # Class methods

    @classmethod
    def from_dict(cls, name:str, data:dict):
        """
        Create a new Card from the data contained in a dict.

        Args:
            name (str): The name of the card.
            data (dict): Data of the card (iid, cost, damage, armor, ...)
        """

        card = cls(name)
        card.__dict__.update(data)
        return card

    # Methods

    def copy(self):
        """Return a copy of this card"""

        return copy.deepcopy(self)

    def _upgrade(self):
        """Upgrade the card once."""

        self.upgrades += 1

    def upgrade(self, n:int=1):
        """
        Upgrade the card a given number of times.

        Args:
            n (int, optional): Number of time the card is upgraded. Defaults to 1.
        """

        for _ in range(n):
            self._upgrade()

        self.upgraded.emit()
