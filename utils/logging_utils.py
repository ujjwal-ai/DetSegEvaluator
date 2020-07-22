import logging

class ParentLogger(object):
    LOGLEVEL = dict(
        info=logging.INFO,
        debug=logging.DEBUG,
        warning=logging.WARNING,
        fatal=logging.FATAL
    )
    def __init__(self,
                 loglevel,
                 logfilename=None,
                 log_to_stderr=None
                 ):
        if loglevel not in list(
            self.LOGLEVEL.keys()
        ):
            raise ValueError('Invalid loglevel.')

        self._logger = logging.getLogger('Evaluation.')

        if logfilename is not None:
            try:
                filehandler = logging.FileHandler(
                    filename=logfilename,
                    mode='w'
                )
            except OSError:
                raise OSError('The specified logfile {} cannot be '
                              'created.'.format(logfilename))
            self.logger.addHandler(filehandler)

        if log_to_stderr:
            streamhandler = logging.StreamHandler()
            self.logger.addHandler(streamhandler)

    @property
    def logger(self):
        return self._logger