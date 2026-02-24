from settings import FilePath, Group


class AstalonSettings(Group):
    class GamePath(FilePath):
        description = "Astalon game executable"
        is_exe = True

    game_path: GamePath = GamePath("Astalon.exe")
