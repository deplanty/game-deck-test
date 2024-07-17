# Deck building game

This game is a deck building without a name yet.
The project was to create both a deck building game and an interface (tkinter like) for console.

## TUI (text user interface)

This interface has been mainly inspired by the `tkinter` module from Python.

The elements are called **widgets** and positionned on screen with simple layout modes:
  - `pack`: the widgets are stacked.
  - `place`: the widgets are placed "manually" on screen.
  - `grid`: the widgets are placed in a grid.

The available widgets are:
  - Containers:
    - `Frame`: a container for other widgets. Usefull for complex layouts.
    - `LabelFrame`: a bordered frame with a title to separate sections.
  - Static and data:
    - `Label`: a text.
    - `Progressbar`: a progressbar.
    - `HLine`: a simple horizontal line.
  - User interactions:
    - `Button`: a text that triggers a signal when Return key is pressed.
    - `Entry`: wait for user text key inputs.
    - `Choice`: let the user chose an option from several labels (layout: column).
    - `ChoiceLine`: same as Choice but as a line.
    - `ChoiceWidget`: let the user choose an option from several widgets (layout: grid).

Each widget have its own style: foreground color, background color, bold, ...

## Deckbuilding

This game is based on "Dawncaster" and "Rogue Adventure".

The gameloop is:
  1. Choose a hero to start the journey.
  2. Select which encounter you want to face.
  3. Win the battle against the encounter.
  4. Improve your deck:
    - Upgrade one of our cards.
    - Add a new card.
  5. Repeat from 2.
  6. When all the encounters are defeated, you can upgrade your hero and go to the next stage (WIP).

The hero has several stats:
  - HP: his health points.
  - Energy: the pool of energy to play cards.
  - Hand size: how many cards he can draw at the start of the turn.
  - Augments: some permanent bonuses.

The cards have several effects:
  - Deal damage.
  - Buff:
    - Give armor.
    - Increase his strenght.
    - Increase his resistance.
    - Grant thorn.
  - Debuf:
    - Burn.
    - Poison.
    - Weakness.
  - Heal.
  - Restore some energy.
  - Hurt the user.
  - Draw a or multiple cards.
  - Bash to deal damage equal to the armor.
