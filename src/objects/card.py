import copy

from src.utils import Signal


class Card:
    """
    Create a card.

    Args:
        iid (int): The uniq id if the card.
    """

    def __init__(self, iid:int):
        self.iid = int(iid)

        self.owner:Player = None

        # The name of the card
        self.name:str = ""
        # Its energy cost
        self.cost:int = 0
        # The number of upgrades that the card benefits
        self.upgrades:int = 0
        # Its description (used with .format())
        self.description:str = ""

        # If the hero can obtain this card
        self.obtainable:bool = True

        # The base damage, used to calculate the real damage it deals
        self.base_damage:int = 0
        # The base armor, used to calculate the real armor it grants
        self.base_armor:int = 0

        # Buff: increase buff of a player
        self.strenght:int = 0
        self.resistance:int = 0
        self.thorn:int = 0
        # Debuff: increase debuf of a player
        self.burn:int = 0
        self.poison:int = 0
        self.weakness:int = 0
        # Effects
        # Heals the player
        self.heal:int = 0
        # Grants energy to the player
        self.energy:int = 0
        # Deals damage to the player that play the card
        self.hurt:int = 0
        # Allows the player to draw more cards
        self.draw:int = 0
        # Deals damage equal to the armor of the player
        self.bash:bool = False

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
        if self.bash and self.owner:
            damage = self.owner.armor
        elif self.base_damage == 0:
            damage = 0
        else:
            damage = self.base_damage + self.upgrades
            if self.owner: damage += self.owner.strenght
            if self.owner and self.owner.weakness > 0: damage //= 2
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
        text += f"Obtainable = {self.obtainable}\n"
        text += self.description.format(card=self)
        return text

    # Class methods

    @classmethod
    def from_dict(cls, iid:int, data:dict):
        """
        Create a new Card from the data contained in a dict.

        Args:
            iid (int): The uniq id of the card.
            data (dict): Data of the card (iid, cost, damage, armor, ...)
        """

        card = cls(iid)
        card.__dict__.update(data)
        return card

    def to_dict(self) -> dict:
        """
        Return the data from this card as a dict.
        Only export parameters where the value is different than the default.
        """

        default = Card(-1)

        data = dict()
        for key, value in self.__dict__.items():
            if value != getattr(default, key):
                data[key] = value
        return data

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
