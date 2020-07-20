import os
import logging


def read_detection_file_list(detection_list_file : str):
    """
    Reads the list of files, each containing detections for one image.
    The full path to the files should be stored in "detection_list_file",
    one each line.
    :param detection_list_file: A text file storing full paths to detection
    files. Each detection file should contain detections for one specific
    image.
    :return: A list of full paths to the detection files.
    """

    if not os.path.isfile(detection_list_file):
        raise OSError('The file {} does not exist.'.format(detection_list_file))

    detection_file_list = open(detection_list_file, 'r').readlines()
    detection_file_list = list(
        map(
            lambda x : x.strip(),
            detection_file_list
        )
    )
    logger = logging.getLogger()
    logger.info('Number of detection files : {}.'.format(len(detection_file_list)))
    return detection_file_list