
# Breaking down problems

### Server side

- what needs to be sent to the server
- 1 server can host one match ?
    - don't have any solutions for now

### Map

- static side-on view
- tile map

- large
    - 3v3
- medium
    - 2v2
- small
    - 1v1

### Character

- animations / stickman


### The Main Menu

- play button 
    - enter the IP
        - the server determines the mode depending of the number of players connected into the lobby

### Two hitboxs

- the actual hitbox (when the player is being hit)
- the checking hitbox (when the player successfully dodge a bullet)

### bullet

- bullet trajectory
- fire rate

### Physics

- gravity
- jumps
- collisions with map

### Match / gameplay

- timer or not ?
    - at the end of timer, player(s) with less HP loose
    - or fight until a player dies
        - zone created when timer is 0, if player stays in the zone, they die
- Su-Pa
    - count number of dodges the player did
    - at 5 dodges, can use "mirror shield"
