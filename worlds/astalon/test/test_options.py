from .bases import AstalonTestBase

FULL_RANDOM = {
    "randomize_characters": "solo",
    "randomize_key_items": "true",
    "randomize_health_pickups": "true",
    "randomize_attack_pickups": "true",
    "randomize_white_keys": "true",
    "randomize_blue_keys": "true",
    "randomize_red_keys": "true",
    "randomize_shop": "true",
    "randomize_switches": "true",
    "randomize_elevator": "true",
    "randomize_candles": "true",
    "randomize_orb_multipliers": "true",
    "shuffle_void_portals": "decoupled",
    "apex_elevator": "included",
}


class DefaultTest(AstalonTestBase):
    pass


class KeysTest(AstalonTestBase):
    options = {  # noqa: RUF012
        "randomize_white_keys": "true",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
    }


class SwitchesTest(AstalonTestBase):
    options = {  # noqa: RUF012
        "randomize_elevator": "true",
        "randomize_switches": "true",
    }


class SwitchesOnlyTest(AstalonTestBase):
    options = {  # noqa: RUF012
        "difficulty": "hard",
        "randomize_characters": "vanilla",
        "randomize_key_items": "false",
        "randomize_health_pickups": "false",
        "randomize_attack_pickups": "false",
        "randomize_white_keys": "false",
        "randomize_blue_keys": "false",
        "randomize_red_keys": "false",
        "randomize_shop": "false",
        "randomize_elevator": "false",
        "randomize_switches": "true",
        "randomize_candles": "false",
        "randomize_orb_multipliers": "false",
    }


class AllEasyTest(AstalonTestBase):
    options = {  # noqa: RUF012
        **FULL_RANDOM,
        "difficulty": "easy",
        "shuffle_void_portals": "coupled",
    }


class AllHardTest(AstalonTestBase):
    options = {  # noqa: RUF012
        **FULL_RANDOM,
        "difficulty": "hard",
    }


class VanillaTest(AstalonTestBase):
    options = {  # noqa: RUF012
        "randomize_characters": "vanilla",
        "randomize_key_items": "false",
        "randomize_health_pickups": "false",
        "randomize_attack_pickups": "false",
        "randomize_white_keys": "false",
        "randomize_blue_keys": "false",
        "randomize_red_keys": "false",
        "randomize_shop": "false",
        "randomize_elevator": "false",
        "randomize_switches": "false",
        "randomize_candles": "false",
        "randomize_orb_multipliers": "false",
        "start_with_qol": "false",
        "open_early_doors": "false",
    }


class EyeHuntTest(AstalonTestBase):
    options = {  # noqa: RUF012
        "goal": "eye_hunt",
        "additional_eyes_required": "6",
        "extra_eyes": "33",
    }


class StartingLocationMechTest(AstalonTestBase):
    options = {  # noqa: RUF012
        **FULL_RANDOM,
        "starting_location": "mechanism",
    }


class StartingLocationHopTest(AstalonTestBase):
    options = {  # noqa: RUF012
        **FULL_RANDOM,
        "starting_location": "hall_of_phantoms",
    }


class StartingLocationRoaTest(AstalonTestBase):
    options = {  # noqa: RUF012
        **FULL_RANDOM,
        "starting_location": "ruins_of_ash",
    }


class StartingLocationApexTest(AstalonTestBase):
    options = {  # noqa: RUF012
        **FULL_RANDOM,
        "starting_location": "apex",
    }


class StartingLocationCataTest(AstalonTestBase):
    options = {  # noqa: RUF012
        **FULL_RANDOM,
        "starting_location": "catacombs",
    }


class StartingLocationTrTest(AstalonTestBase):
    options = {  # noqa: RUF012
        **FULL_RANDOM,
        "starting_location": "tower_roots",
    }


class StartingLocationCdTest(AstalonTestBase):
    options = {  # noqa: RUF012
        **FULL_RANDOM,
        "starting_location": "cyclops_den",
    }


class StartingLocationCathTest(AstalonTestBase):
    options = {  # noqa: RUF012
        **FULL_RANDOM,
        "starting_location": "cathedral",
    }


class StartingLocationSpTest(AstalonTestBase):
    options = {  # noqa: RUF012
        **FULL_RANDOM,
        "starting_location": "serpent_path",
    }
