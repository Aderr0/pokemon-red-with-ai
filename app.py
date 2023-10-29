from src.pyboy import Pyboy

if __name__.__eq__("__main__"):
    try:
        game = Pyboy(sound=True)
        game.run()
    except KeyboardInterrupt:
        game.close()
    except Exception as e:
        print(e)
        game.close()
