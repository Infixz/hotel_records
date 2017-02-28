# coding: utf-8
import os

def namelist():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    tmp_dir = os.walk(BASE_DIR)
    return [os.path.join(BASE_DIR,i) for i in tmp_dir.next()[2] if i.endswith('.csv')]
