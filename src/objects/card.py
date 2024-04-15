import copy


class Card:
    """
    Create a card.

    Args:
        name (str): The name of the card.
    """

    def __init__(self, name:str):
        self.name = name
        self.iid = 0
        self.cost = 0
        self.upgrades = 0
        self.description = ""
        
        self.damage = 0
        self.armor = 0

    def __str__(self) -> str:
        if self.upgrades > 0:
            return f"Card({self.iid:03d}, {self.name}, +{self.upgrades})"
        else:
            return f"Card({self.iid:03d}, {self.name})"

    def __repr__(self) -> str:
        return str(self)

    # Properties

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

    def upgrade(self):
        """Upgrade the card by increasing its stats."""

        self.upgrades += 1
        self.damage += 1

    def upgrade_multiple(self, n:int):
        """
        Upgrade the card several times.

        Args:
            n (int): Number of time the card is upgraded.
        """

        for _ in range(n):
            self.upgrade()
