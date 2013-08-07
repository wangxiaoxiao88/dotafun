#-*- coding: utf-8 -*-
import logging
import os

logger = logging.getLogger(__name__)
handler = logging.FileHandler(os.path.join(os.getcwd(),'log.txt'))
formatter = logging.Formatter('%(asctime)s\t%(message)s', '%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)