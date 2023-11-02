

class Constants:

    # Emulator configuration
    SCREEN_WIDTH = 160
    SCREEN_HEIGHT = 144
    TICKS_PER_SECOND = 60

    # Game configuration

    # Path to resources
    ROM_PATH = "resources/"
    ROME_FILE_NAME = "pokemon-red"
    ROM_FILE_PATH = ROM_PATH + ROME_FILE_NAME + ".gb"

    SCREENSHOTS_PATH = "src/resources/screenshots/"
    SCREENSHOTS_FILE_PATH = SCREENSHOTS_PATH + "image_{image_count}.jpg"
    STATES_PATH = "src/resources/states/"
    STATES_FILE_PATH = STATES_PATH + "{state_name}.state"

    # Python configuration
    log_level = "DEBUG"