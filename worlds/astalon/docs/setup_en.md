# Astalon: Tears of the Earth for Archipelago Setup Guide

## Required Software

- [Astalon: Tears of the Earth](https://store.steampowered.com/app/1046400/Astalon_Tears_of_the_Earth/)
- [BepInEx IL2CPP v6 x86](https://builds.bepinex.dev/projects/bepinex_be)
  - Currently you must use the bleeding edge release of v6 since the stable version does not support IL2CPP. A direct download for the version tested against can be found [here](https://builds.bepinex.dev/projects/bepinex_be/688/BepInEx-Unity.IL2CPP-win-x86-6.0.0-be.688%2B4901521.zip).
- [Archipelago Mod for Astalon](https://github.com/drtchops/Archipelago-Astalon/releases)

## Installation Procedure

1. Download and extract BepInEx into your Astalon install folder.
2. Download and extract the Archipelago Mod into your Astalon install folder.

## Connecting

1. Open `Astalon Tears of the Earth/BepInEx/config/Archipelago.cfg` in a text editor and change the `address`, `port`, `slotName`, and `password` fields as needed.
2. Launch the game. It will take longer to open the first time after installing BepInEx as it needs to generate some files.
3. Start a new save file in any slot.
4. The game should connect to AP automatically when you gain control. You can look at the BepInEx console to verify.

## Resuming

The game will connect to AP upon loading a save game. Any items you received while the game was closed will be added to your inventory.

## Archipelago Text Client

We recommend having Archipelago's Text Client open on the side to keep track of what items you receive and send.
Astalon has in-game messages, but they disappear quickly and there's no reasonable way to check your message history in-game.

## Known Issues

- Received items may need to be turned off and on again in the inventory to start working.
- If the game loses its AP connection, items will not be sent upon reconnecting. You'll have to quit and recollect the items.
- Orbs received as filler items will get collected again every time you reconnect.
- There's currently no softlock prevention, but you can press Left Ctrl + Left Shift + K to die and respawn.
