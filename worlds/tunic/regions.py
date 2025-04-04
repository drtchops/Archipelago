tunic_regions: dict[str, tuple[str]] = {
    "Menu": ("Overworld",),
    "Overworld": ("Overworld Holy Cross", "East Forest", "Dark Tomb", "Beneath the Well", "West Garden",
                  "Ruined Atoll", "Eastern Vault Fortress", "Beneath the Vault", "Quarry Back", "Quarry", "Swamp",
                  "Spirit Arena"),
    "Overworld Holy Cross": tuple(),
    "East Forest": tuple(),
    "Dark Tomb": ("West Garden",),
    "Beneath the Well": tuple(),
    "West Garden": tuple(),
    "Ruined Atoll": ("Frog's Domain", "Library"),
    "Frog's Domain": tuple(),
    "Library": tuple(),
    "Eastern Vault Fortress": ("Beneath the Vault",),
    "Beneath the Vault": ("Eastern Vault Fortress",),
    "Quarry Back": ("Quarry", "Monastery"),
    "Quarry": ("Monastery", "Lower Quarry"),
    "Monastery": ("Monastery Back",),
    "Monastery Back": tuple(),
    "Lower Quarry": ("Rooted Ziggurat",),
    "Rooted Ziggurat": tuple(),
    "Swamp": ("Cathedral",),
    "Cathedral": tuple(),
    "Spirit Arena": tuple()
}
