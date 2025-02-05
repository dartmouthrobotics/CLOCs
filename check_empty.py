# AQL
# e.g.
# python check_empty.py data/kitti/ImageSets/train.txt d2_detection_data/

import os
import sys

txt_file_path = sys.argv[1]
detection_path = sys.argv[2]

EXTENSION = ".txt"

with open(txt_file_path, "r") as f:
    for l in f:
        file_size = os.path.getsize(os.path.join(detection_path,
            l.strip() + EXTENSION))
        if file_size < 10:
            print("{}".format((l.strip(), file_size)))

