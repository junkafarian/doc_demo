from datetime import datetime
import logging

from flask import Flask, request

logging.basicConfig()

app = Flask(__name__)


class LogHandler(object):
    """ Initialises a logger and provides some utilities for storing pretty
        messages
    """

    my_attribute = 'foo'
    """the reason for being"""

    def log_request(self, debug=False):
        """ Logs details of the current request context provided by Flask.

        **Args**:
            runtime: int
                     timeout for length of run

        **Kwargs**:
            debug: bool
                   debug flag

        **Raises**:
            RuntimeError: if called outside a request context

        **Returns**:
            None
        """
        logger = logging.getLogger(request.url)
        logger.info(
            'Responded to {0} request at {1}'.format(
                request.method,
                datetime.now()
            )
        )


@app.route('/')
def index():
    """ Returns the exceedingly underused adage "Hello World!"
    """
    logger = LogHandler()
    logger.log_request()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
