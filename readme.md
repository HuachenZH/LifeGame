# LifeGame
## ~~blabla~~ intro
I met some difficulties in my life so i decide to code something.  
Life does not go well, and i'm going to code a life game, how ironic.  
The core code comes from [this post](https://beltoforion.de/en/recreational_mathematics/game_of_life.php)

## Requirements
You might see `from PIL import Image`. You need to install `Pillow` instead of PIL, PIL is no longer maintained.



## functional needs
I developped an ascii style lifegame earlier... however running python in a terminal is not performant. The program is not as smooth as the famous C donut.  
So i decided to use the python game library.
- the canva size is not fixed
- user can draw the initial state in paint, then save in jpg/png, then the program read it.
- feature to be developped: user can add blocks in real time, after the game launched


## task list
- ~~define py version~~
- ~~create virtual env~~
- ~~install libs~~
- learn lifegame.py
- ~~clean up code~~
  - remove argument cellsize in main (or maybe not, need to understand what it s doing)  
    --> No it's better to keep it, a cell IS NOT a pixel.
  - ~~mission upgrade: add docstring and explain cellsize~~
  - ~~change variable name, col means color but not column~~
  - ~~change dim: equal to input image size~~
- add feature
  - ~~read a canva (jpg, png)~~
  - ~~make it an argument~~
  - ~~set a default value for input path~~
  - ~~transform to vector~~
  - interactive with mouse. Mouse can draw new live cells.
    - i asked chatgpt to give some ideas, seems working with mouse event. I need to
    - mouse evnet test passed
    - get cursor postion
    - reflect position into canva
    - change the original update() function or write a new function