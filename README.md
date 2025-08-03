## gamedev workshop @ arts @ large
### AI Free!

#### Setup ~10m
* cheat sheet printouts
* accessing piskel
* using vscode
```
source <(curl -s shinysocks.net/s/aal)
```

#### Show Growing Cat!
* Our deliverable is to make something silly!
* Animation + simple movement!

#### Teaching Python Basics ~15m
* Walk throught the Mosh's cheatsheet with code examples

#### Explaining Game Concepts ~5m
* Game Loop
* Positions / Size
    * Screen-space coordinates
    * Collisions
 * Show RGB with color picker

#### Teaching the Library ~15m
* Walk through my cheatsheet with code examples

Animation:
* load an animation from a spritesheet

Position:
* an (x, y) coordinate representing a location within the game window

Sprite:
* an in-game object with an animation, position, and size
* Sprites are drawn every frame

Text:
* a special sprite with text instead of animation

#### Using Piskel to create and export a spritesheet ~15m
* [piskel](https://www.piskelapp.com/p/create/sprite/)
* Create your animation
    * setup preview to full size!
    * ensure that there is no border around the edges of each frame

* Exporting your completed animation:
    * Consider a good FPS value (experimentation is also great)
    * Make sure you remember how many rows and columns you have
    * Move your png spritesheet into the `src/spritesheets_here/` folder

