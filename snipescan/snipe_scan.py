"""A simple program to import assets into SnipeIT"""

import sys
import logging
import logging.config

from PySide6.QtWidgets import QApplication

import settings
from snipeapi import SnipeGet
from ui import Window


def main():
    """Main function to load the program and get things started."""

    #let's setup logging
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    logger = logging.getLogger('snipescan')
    logger.info('***************************************')
    logger.info('          Snipe scan starting')
    logger.info('***************************************')
    logger.debug('Snipe URL: %s', settings.SNIPE_URL)

    # Test connectivity to the Snipe server.  For a properly configured
    # Snipe deployment there should be at least one user returned.  If
    # 0 or None is returned, then exit the program with an error.

    if SnipeGet(settings.SNIPE_URL, settings.API_KEY, 'users').count():
        logger.info('Successfully connected to the Snipe Server')
    else:
        logger.critical('No connection to the Snipe Server.')
        logger.critical(settings.SNIPE_URL)
        sys.exit()

    
    # Launch the UI
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
