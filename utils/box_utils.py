import logging
from collections import namedtuple

logger = logging.getLogger()
BBOX = namedtuple(
    "BBOX",
    [
        'xmin',
        'ymin',
        'xmax',
        'ymax'
    ]
)

def print_bbox(box: BBOX):
    """
    Returns a string output of a bounding box which can be printed.
    :param box: (BBOX). A bounding box.
    :return: (str). A string representing the bounding box coordinates.
    """
    string_output = "xmin = {}  ymin = {}  xmax = {}  ymax = {}".format(
        box.xmin,
        box.ymin,
        box.xmax,
        box.ymax
    )
    return string_output

def validate_bounding_box(box: BBOX):
    if box.xmin > box.xmax:
        logger.error(
            "For the bounding box {}, xmin > xmax. This is an error.".format(
                print_bbox(box)
            )
        )

    if box.ymin > box.ymax:
        logger.error(
            "For the bounding box {}, ymin > ymax. This is an error.".format(
                print_bbox(box)
            )
        )

    if box.xmin == box.xmax:
        logger.warning(
            "For the bounding box {}, xmin = xmax. This might not be a "
            "sensible bounding box. It is advised to check.".format(
                print_bbox(box)
            )
        )

    if box.ymin == box.ymax:
        logger.warning(
            "For the bounding box {}, ymin = ymax. This might not be a "
            "sensible bounding box. It is advised to check.".format(
                print_bbox(box)
            )
        )

    if box.xmin == box.xmax and box.ymin == box.ymax:
        logger.warning(
            "For the bounding box {}, xmin = xmax and ymin = ymax. The "
            "bounding box in this case reduces to a point. This is certainly "
            "not a sensible bounding box. It is advised to check.".format(
                print_bbox(box)
            )
        )

    return box

def get_box_area(box:BBOX):
    area = (box.xmax - box.xmin + 1) * (box.ymax - box.ymin + 1)
    return area

def intersection_over_union(box1: BBOX, box2: BBOX):
    box1 = validate_bounding_box(box1)
    box2 = validate_bounding_box(box2)

    # Get coordinates of the intersection rectangle
    x_left = max(
        box1.xmin,
        box2.xmin
    )
    y_top = max(
        box1.ymin,
        box2.ymin
    )
    x_right = min(
        box1.xmax,
        box2.xmax
    )
    y_bottom = min(
        box1.ymax,
        box2.ymax
    )

    if x_right < x_left or y_bottom < y_top:
        # In this case the boxes are completely disjoint and hence IOU = 0.0
        return 0.0

    intersection_box = BBOX(
        xmin=x_left,
        ymin=y_top,
        xmax=x_right,
        ymax=y_bottom
    )
    intersection_area = get_box_area(intersection_box)
    box1_area = get_box_area(box1)
    box2_area = get_box_area(box2)
    iou = intersection_area / (box1_area + box2_area - intersection_area)
    return iou