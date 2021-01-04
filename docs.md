# Documentation
`hypixelaPY.Hypixel(api_key)`:
- `api: str` - the provided api key
- `player: Player` - wrapper on the player method of the Hypixel API
- `leaderboards: Leaderboards` - wrapper on the leaderboards method of the Hypixel API

## Player
`Player`:
- `get(uuid: str=uuid, name: str=name, input_: str=input_) -> HypixelPlayer` - gets a player from the API
    - this prioritizes `uuid`, then `name`, then `input_`
    - only one input is required for a valid result
    
`HypixelPlayer`:
- `str(x)` - returns the name of the player
- `name: str` - the name of the player
- `uuid: str` - the UUId of the player
- `karma: int` - the player's karma
- `achievement_points: int` - the player's achievement points
- `rank: Rank` - the rank data of the player
- `level: Level` - the network level data of the player
- `logins: LoginTimes` - the login times of the player
- `social: Social` - the social media links/names of the player
- `bedwars: Bedwars` - the Bedwars stats of the player
- `skywars: Skywars` - the Skywars stats of the player
- `duels: Duels` - the Duels stats of the player

`Rank`:
- `str(x)` - returns the rank name
- `bool(x)` - checks whether a rank exists
- `name: str` - the rank name
- `color: int` - the color as a hexadecimal int

`Level`:
- `exact: float` - the exact network level of the player
- `level: int` - the network level of the player
- `next: int` - the next network level of the player
- `percentage: float` - the percentage of the way the player is to `next`

`LoginTimes`:
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