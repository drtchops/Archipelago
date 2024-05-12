from . import AstalonTestBase


class DefaultTest(AstalonTestBase):
    pass


class KeysTest(AstalonTestBase):
    options = {
        "randomize_white_keys": "true",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
    }


class SwitchesTest(AstalonTestBase):
    options = {
        "randomize_elevator": "true",
        "randomize_switches": "true",
    }


class SwitchesOnlyTest(AstalonTestBase):
    options = {
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
    }


class AllEasyTest(AstalonTestBase):
    options = {
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
        "start_with_qol": "true",
        "apex_elevator": "vanilla",
        "open_early_doors": "true",
    }


class AllHardTest(AstalonTestBase):
    options = {
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
        "start_with_qol": "true",
        "apex_elevator": "vanilla",
        "open_early_doors": "true",
    }


class VanillaTest(AstalonTestBase):
    options = {
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
        "start_with_qol": "false",
        "open_early_doors": "false",
    }


class EyeHuntTest(AstalonTestBase):
    options = {
        "goal": "eye_hunt",
        "additional_eyes_required": "6",
        "extra_eyes": "33",
    }
