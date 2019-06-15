Project3
=======
Help Mac Gyver to escape

Design of the mazes
--------------------------
The structure of the maze (structures/Construct.ods) can be edited as a spreassheet :
- 0 for tiles unaccessibles
- for accessible tiles :
    - 1 for classic tiles
    - 2 for departure
    - 3 for arrival

![The structure](/images/maze-spreadsheet.jpg)

The file is to export as a csv (separator ";") in '/structures'. One structure per level (/structures/structurei where i is the level number)
The maze has to be well designed:
- no isolated tile
- it can be traveled without problem (it's possible to finish the game)

Game
--------------------------
Launch game.py to play the game. You have a limited number of lives. First level is level 0. The top level to reach is level 10.
*Go next to the guardian with all the objects collected on your journey.*
*Avoid ennemies.*
