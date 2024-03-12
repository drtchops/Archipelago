# Astalon: Tears of the Earth for Archipelago Setup Guide

## Required Software

- [Astalon: Tears of the Earth](https://store.steampowered.com/app/1046400/Astalon_Tears_of_the_Earth/)
- [BepInEx IL2CPP v6 x86](https://builds.bepinex.dev/projects/bepinex_be)
  - Currently you must use the bleeding edge release of v6 since the stable version does not support IL2CPP. A direct download for the version tested against can be found [here](https://builds.bepinex.dev/projects/bepinex_be/688/BepInEx-Unity.IL2CPP-win-x86-6.0.0-be.688%2B4901521.zip).
- [Archipelago Mod for Astalon](https://github.com/drtchops/Archipelago-Astalon/releases)

## Installation

1. Download and extract BepInEx into your Astalon install folder.
2. Download and extract the Archipelago Mod into your Astalon install folder.

## Connecting

1. Launch the game. It will take longer to open the first time after installing BepInEx as it needs to generate some files.
2. There will be a place to input your connection details in the bottom right corner of the screen. Enter the archipelago server address and port, your player name, and a password if required, and press connect.
3. Once connected, the bottom corner will switch to showing your connection status. A console that shows you any messages from AP will appear at the top of the screen. You can click the show button to expand it and send messages.
4. Start a new save file in any slot. You can also do so before connecting to AP.
5. Items should send out and display an item box in-game when you check locations. Received items should automatically be added to your inventory and an item box will be displayed.

## Resuming

You can load an existing save and conenct to the AP server in any order. Once you've loaded in and connected you will receive any items that were sent since you last played.

## In-Game Controls

Once you've connected to AP you can press F1 to open a set of debug options at the bottom of the screen. If you're softlocked you can use this menu to die and respawn.

## Known Issues

- Received items may need to be turned off and on again in the inventory to start working.
- If the game loses its AP connection, items will not be sent upon reconnecting. You'll have to quit and recollect the items.
- Orbs and keys received as filler items will get collected again every time you reconnect.
- There's currently no softlock prevention.
