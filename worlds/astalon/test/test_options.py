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


class AllEasyTest(AstalonTestBase):
    options = {
        "difficulty": "easy",
        "randomize_characters": "solo",
        "randomize_health_pickups": "true",
        "randomize_attack_pickups": "true",
        "randomize_white_keys": "true",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
        "randomize_shop": "true",
        "randomize_elevator": "true",
        "randomize_switches": "true",
        "start_with_qol": "true",
        "free_apex_elevator": "true",
        "open_early_doors": "true",
    }


class AllHardTest(AstalonTestBase):
    options = {
        "difficulty": "hard",
        "randomize_characters": "solo",
        "randomize_health_pickups": "true",
        "randomize_attack_pickups": "true",
        "randomize_white_keys": "true",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
        "randomize_shop": "true",
        "randomize_elevator": "true",
        "randomize_switches": "true",
        "start_with_qol": "true",
        "free_apex_elevator": "true",
        "open_early_doors": "true",
    }
