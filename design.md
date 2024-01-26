
# Design

### Libraries

- button
- socket
- pygame
- ping

### Server side

- the server sends the positions every 0.1 seconds to all players to all client connected

### Map

- Map size should change depending of the numbers of people in the lobby, a small map for a 1v1, a medium map for a 2v2 or a 1v1v1 and a large map for a 3v3 match.
- 1v1v1v1v1 sould not be possible

### Character

- the sprite has animations
    - draw several png images
- gravity implementation
    - simple physics

### The Main Menu

- the user inputs the IP of the server and username that should be used
    - IP used to connect to the server using socket librabry
    - username will be the named displayed to other players

### Two hitboxs

- [ ] the actual hitbox (when the player is being hit)
- [ ] the checking hitbox (when the player successfully dodge a bullet)

- real hitbox :
    - the hitbox used to check if the player has been hit

- crouch hitbox:
    - the hitbox used to check if a player has successfully dodged a shot
    - the server checks it

### bullet

- [ ] bullet trajectory
- [ ] fire rate
- [ ] ray casting

### Physics

- [ ] gravity
- [ ] jumps
- [ ] collisions with map

### Match / gameplay

- [ ] timer or not ?
    - at the end of timer, player(s) with less HP loose
    - or fight until a player dies
        - zone created when timer is 0, if player stays in the zone, they die
- [ ] Su-Pa
    - count number of dodges the player did
    - at 5 dodges, can use "mirror shield"
