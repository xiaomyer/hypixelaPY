# hypixelaPY - Hypixel API wrapper written in Python
[![widget](https://inv.wtf/widget/myerfire)](https://myer.wtf/discord)

Maintained by [Myer (also known as myerfire, MyerFire)](https://github.com/myerfire)
- [YouTube](https://myer.wtf/youtube)
- [Twitter](https://myer.wtf/twitter)
- myer#0001 on Discord

This library is an async wrapper for the [Hypixel API](https://github.com/HypixelDev/PublicAPI).
It also contains some features and wrappers on relevant features of the [Mojang API and session server](https://wiki.vg/Mojang_API).

## Features
- Getting a player from Hypixel from UUID, name, or an unknown source (will try to interpret as UUID first, then name)
    - Names will always be converted to a UUID using the Mojang API
- Getting a player's name history from Mojang from UUID
- Getting the official Hypixel leaderboards
    
## Installation
hypixelaPY is available from the official pYpI package index.

`python -m pip install -U hypixelaPY`

## Quick Start
```python
from hypixelaPY import Hypixel
import asyncio

API_KEY = "hahagetbaited"
# if it isn't obvious enough, replace this string 
# with your API key obtained by running /api new on Hypixel

async def main():
    hypixel = Hypixel(API_KEY)
    player = await hypixel.get(name="Technoblade")
    print(f"[{player.rank.name}] {player.name}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
```
