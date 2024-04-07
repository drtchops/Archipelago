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
        "randomize_switches": "true",
        "randomize_elevator": "true",
    }


class AllTest(AstalonTestBase):
    options = {
        "difficulty": "hard",
        "randomize_characters": "true",
        "randomize_health_pickups": "true",
        "randomize_attack_pickups": "true",
        "randomize_white_keys": "true",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
        "randomize_shop": "true",
        "randomize_switches": "true",
        "randomize_elevator": "true",
        "start_with_qol": "true",
        "free_apex_elevator": "true",
        "open_early_doors": "true",
    }
