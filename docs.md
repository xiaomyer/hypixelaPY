# Documentation
`hypixelaPY.Hypixel(api)`:
- `api: str` - the provided api key
- `player: Player` - wrapper on the player method of the Hypixel API
- `leaderboards: Leaderboards` - wrapper on the leaderboards method of the Hypixel API

## Player
### Overall
`Player`:
- `get(uuid: str=uuid, name: str=name, input_: str=input_) -> HypixelPlayer` - gets a player from the API
    - this prioritizes `uuid`, then `name`, then `input_`
    - only one input is required for a valid result
```python
hypixel = hypixelaPY.Hypixel(API_KEY)
player = await hypixel.player.get(uuid=uuid)  # will use uuid
player = await hypixel.player.get(name=name)  # will use name
player = await hypixel.player.get(uuid=uuid, name=name)  # will use uuid
player = await hypixel.player.get(input_=input_)  # will use input_
player = await hypixel.player.get(uuid=uuid, name=name, input_=input_)  # will use uuid
player = await hypixel.player.get(name=name, input=input_)  # will use name
```
    
`HypixelPlayer`:
- `str(x)` - returns the name of the player
- `name: str` - the name of the player
- `uuid: str` - the UUId of the player
- `karma: int` - the player's karma
- `achievement_points: int` - the player's achievement points
- `rank: Rank` - the rank data of the player
- `level: Level` - the network level data of the player
- `logins: Logins` - the login times of the player
- `social: Social` - the social media links/names of the player
- `bedwars: Bedwars` - the Bedwars stats of the player
- `skywars: Skywars` - the Skywars stats of the player
- `duels: Duels` - the Duels stats of the player

`Rank`:
- `str(x)` - returns the rank name
- `bool(x)` - checks whether a rank exists
- `name: str, None` - the rank name
- `color: int` - the color as a hexadecimal int

`Level`:
- `exact: float` - the exact network level of the player
- `level: int` - the network level of the player
- `next: int` - the next network level of the player
- `percentage: float` - the percentage of the way the player is to `next`

`Logins`:
- `first: datetime.datetime` - the first login of the player
- `last: datetime.datetime` - the most recent login of the player

`Social`:
any attribute in this class could be `None`
- `twitter: str` - the Twitter link of the player
- `youtube: str` - the YouTube link of the player
- `instagram: str` - the Instagram link of the player
- `twitch: str` - the Twitch link of the player
- `discord: str` - the Discord name or link of the player
- `hypixel_forums: str` - the Hypixel Forums link of the player

### Bedwars
These classes all have the following stat attributes (all but `prestige`, `coins`, `solo`, `doubles`, etc):
- `Solo`
- `Doubles`
- `Threes`
- `Fours`
- `FourVFour`
- `Castle`
- the dreams ones

`Bedwars`:
- `prestige: Prestige` - the star level and prestige of the player
- `coins: int` - the Bedwars coins of the player
- `games_played: int` - the amount of Bedwars games the player has played
- `beds: BedsBrokenLost` - the amount of beds the player has broken and lost
- `kills: KillsDeaths` - the amount of kills and deaths the player has
- `finals: FinalKillsDeaths` - the amount of final kills and final deaths the player has
- `wins: WinsLosses` - the amount of games the player has won and lost
- `winstreak: int` - the overall Bedwars winstreak of the player
- `solo: Solo` - the solo Bedwars stats of the player
- `doubles: Doubles` - the doubles Bedwars stats of the player
- `threes: Threes` - the solo Bedwars stats of the player
- `fours: Fours` - the solo Bedwars stats of the player
- `four_v_four: FourVFour` - the 4v4 Bedwars stats of the player
- `dreams: Dreams` - the dreams Bedwars stats of the player

`Dreams`: All of these classes other than castle have attributes of `solo` or `double` depending on what modes exist. These will have the same attributes as the `Solo` and `Doubles` objects listed above
- `armed`
- `castle`
- `lucky`
- `rush`
- `ultimate`
- `voidless`


```python
hypixel = hypixelaPY.Hypixel(API_KEY)
player = await hypixel.player.get(uuid=uuid)  # will use uuid
print(player.bedwars.prestige.star)
print(player.bedwars.games_played)
print(player.bedwars.solo.games_played)
print(player.bedwars.dreams.armed.doubles.games_played)
```

### Skywars
