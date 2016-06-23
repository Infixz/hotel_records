# coding: utf-8
import csv
def proc(addr, drop_headline=False):
    pointer = csv.reader(open(addr, 'rU'), dialect=csv.excel_tab)
    if drop_headline:
        pointer.next()
    tmp = [i[0] for i in pointer if i]
    tmp2 = [ row.split() for row in tmp]
    return [tmp2[k] for k in (0,3,4,5,6,7,8,11,19,22)]
    
