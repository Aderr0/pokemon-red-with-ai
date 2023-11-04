
from src.pyboy import Pyboy
from src.game import Game
from src.enums import GameMode
from src.log import get_logger

logger = get_logger(__name__)

if __name__.__eq__("__main__"):
    try:
        emulator = Pyboy(sound=True)
        game = Game(emulator, GameMode.NORMAL)

        game.run()
    except KeyboardInterrupt:
        game.close(save=True)
    except Exception as e:
        logger.exception(e)