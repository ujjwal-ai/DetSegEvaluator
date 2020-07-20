import os
import logging
from protos import categories_pb2
from google.protobuf import text_format

def read_categories(category_file):
    if not os.path.isfile(category_file):
        raise OSError('The category file {} was not found.'.format(category_file))

    pb_txt = open(category_file, 'r').read()
    msg = categories_pb2.Categories()
    text_format.Merge(pb_txt, msg)
    names = [
        x.name for x in msg.category
    ]
    labels = [
        x.label for x in msg.category
    ]
    display_names = [
        x.display_name for x in msg.category
    ]
    logger = logging.getLogger()
    if len(names) != len(set(names)):
        logger.error(
            "In the category file duplicates were found for the attribute"
            "name."
        )

    if len(labels) != len(set(labels)):
        logger.error(
            "In the category file duplicates were found for the attribute "
            "label."
        )

    if len(display_names) != len(set(display_names)):
        if len(set(display_names)) != 1:
            logger.error(
                "The attribute display_name must be uniquely specified for "
                "all categories, or should not be specified at all."
            )

    return dict(
        names=names,
        labels=labels,
        display_names=display_names
    )






