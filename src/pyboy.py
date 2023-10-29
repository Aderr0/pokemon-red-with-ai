
from pyboy import PyBoy

from src.constants import Constants
from src.enum import GameMode
from src.log import get_logger

class Pyboy:
    """
    Pyboy is a wrapper class for the Open Source project pyboy : https://github.com/Baekalfen/PyBoy
    This class makes it easy to load a ROM file, run the game, manipulate the screen, and send inputs
    """
    
    def __init__(self, sound=False):
        self.logger = get_logger(__class__.__name__)

        self.sound = sound
        self.tick_count = 0

        self.game = self.load_rom()

    def load_rom(self) -> PyBoy:
        """Loads the ROM file.

        The ROM file location is set in the Constants class in `src/constants.py`.
        It instances a PyBoy object, thanks to the Open Source project pyboy : https://github.com/Baekalfen/PyBoy.


        Returns
        -------
        PyBoy
            The PyBoy instance with the loaded ROM
        """
        rom_path = Constants.ROM_PATH
        try:
            game = PyBoy(rom_path, sound=self.sound)
            self.logger.debug(f"Loaded ROM: {rom_path}")
            return game
        except FileNotFoundError:
            print(f"Error: ROM '{rom_path}' not found.")

    def run(self, mode=GameMode.NORMAL) -> None:
        """Run the game in the specified mode.

        This method runs the game in the specified mode where the mode can be NORMAL or AI_TRAINING.
        NORMAL mode is the default mode and runs the game in real-time.
        AI_TRAINING mode is used to train the AI.

        Parameters
        ----------
        mode : _type_, optional
            _description_, by default GameMode.NORMAL
        """

        if mode == GameMode.AI_TRAINING:
            pass
        elif mode == GameMode.NORMAL:
            self.logger.debug("Starting game in real-time...")
            self.show_commands()
            while not self.game.tick():
                pass

                # Each second, take a screenshot
                if self.tick_count % Constants.TICKS_PER_SECOND == 0:
                    self.screen_image(image_count = self.tick_count//Constants.TICKS_PER_SECOND)

    def screen_image(self, image_count: int|str) -> None:
        image = self.game.screen_image()
        image.save(Constants.SCREENSHOT_PATH.format(image_count=image_count))

    def tick(self) -> bool:
        self.tick_count += 1
        return self.game.tick()
    
    def close(self, save = False) -> None:
        self.game.stop(save)

    def show_commands(self) -> None:
        self.logger.info("Commands:")
        self.logger.info("Arrow keys: Move up / down / left / right")
        self.logger.info("A: Button A on GBA")
        self.logger.info("B: Button B on GBA")
        self.logger.info("Enter: Pause on GBA")
        self.logger.info("Space: Accelerate the game")
        self.logger.info("Escape: Turn off the game")