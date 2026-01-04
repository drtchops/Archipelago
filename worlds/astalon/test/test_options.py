from .bases import AstalonTestBase


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
        "difficulty": "easy",
        "randomize_characters": "solo",
        "randomize_key_items": "true",
        "randomize_health_pickups": "true",
        "randomize_attack_pickups": "true",
        "randomize_white_keys": "true",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
        "randomize_shop": "true",
        "randomize_elevator": "true",
        "randomize_switches": "true",
        "randomize_candles": "true",
        "randomize_orb_multipliers": "true",
        "start_with_qol": "true",
        "apex_elevator": "vanilla",
        "open_early_doors": "true",
    }


class AllHardTest(AstalonTestBase):
    options = {  # noqa: RUF012
        "difficulty": "hard",
        "randomize_characters": "solo",
        "randomize_key_items": "true",
        "randomize_health_pickups": "true",
        "randomize_attack_pickups": "true",
        "randomize_white_keys": "true",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
        "randomize_shop": "true",
        "randomize_elevator": "true",
        "randomize_switches": "true",
        "randomize_candles": "true",
        "randomize_orb_multipliers": "true",
        "start_with_qol": "true",
        "apex_elevator": "vanilla",
        "open_early_doors": "true",
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
