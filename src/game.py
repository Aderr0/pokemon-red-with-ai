
from src.pyboy import Pyboy
from src.enums import GameMode
from src.log import get_logger

class Game:

    def __init__(self, emulator: Pyboy, mode: GameMode = GameMode.NORMAL):
        self.logger = get_logger(__class__.__name__)

        self.emulator = emulator
        self.mode = mode


    def run(self) -> None:
        """Run the game in the specified mode.

        This method runs the game in the specified mode where the mode can be NORMAL or AI_TRAINING.
        NORMAL mode is the default mode and runs the game in real-time.
        AI_TRAINING mode is used to train the AI.

        Parameters
        ----------
        mode : GameMode, optional
            The mode to run the game in, by default GameMode.NORMAL
        """

        if self.mode == GameMode.AI_TRAINING:
            pass
        elif self.mode == GameMode.NORMAL:
            self.start_game_in_real_time()

    def start_game_in_real_time(self) -> None:
            self.logger.debug("Starting game in real-time...")
            self.emulator.load_state()
            self.emulator.show_commands()

            try:
                while self.emulator.tick():
                    pass
            except KeyboardInterrupt:
                self.close(save=True)

    def close(self, save=False) -> None:
        """Close the game.

        Parameters
        ----------
        save : bool, optional
            Whether to save the game, by default False
        """
        self.logger.debug("Closing game...")
        self.emulator.stop(save=save)
