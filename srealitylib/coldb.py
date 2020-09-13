"""
v 0.1 sreality package

Hynek Los
"""

import requests
import json
import logging
from logging import StreamHandler

logger = logging.getLogger()
# logger.addHandler(StreamHandler())
# logger.setLevel(logging.ERROR)



def querySreality(sfilter):
    """query sreality for data"""
    sfilter['page'] = 1
    sfilter['per_page'] = 50
    resjlFinal = []
    for paging in range(1, 10000):
        logger.debug(f"fetching data from page{sfilter['page']}")
        res = requests.get("https://www.sreality.cz/api/cs/v2/estates", params=sfilter)

        resj = json.loads(res.text)
        try:
            resjl = resj['_embedded']['estates']
        except Exception as ex:
            resjl = []
        if len(resjl) == 0:
            break
        resjlFinal.extend(resjl)
        sfilter['page'] = sfilter['page'] + 1
    return resjlFinal


def ishashidUnique():
    """
    querySreality vraci hashid . kontrola, zda jde o unikatni pro vypis:
    :return:
    """
    filter = {
            "category_main_cb": 1,
            #"category_sub_cb":"11|12",
            "category_type_cb": 1,
            #"locality_region_id": 10,
    }
    res = querySreality(sfilter=filter)
    hashIdDb=[]

    for item in res:
        if 'hash_id' not in item.keys():
            print(f" hash_id klic neni v {item} ... neco je spatne")
            break
        if item['hash_id'] in hashIdDb:
            print(f" hash_id neni unikatni - nasel jsem {item['hash_id']}")
            break
        hashIdDb.append(item['hash_id'])
    print(f"ok prosel jsem {len(hashIdDb)} zaznamu a zadne has_id se neopakovalo.")

def srealityStableParams():
    """overovaci funkce. jake je % vyskytu jednotlivych parametru ve vysledku hledani.

    """
    filter = {
            "category_main_cb": 1,
            "category_sub_cb":"11|12",
            "category_type_cb": 1,
            #"locality_region_id": 10,
    }
    res = querySreality(sfilter=filter)
    occurenceRate = {}

    for item in res:
        for ik in item.keys():
            if ik in occurenceRate:
                occurenceRate[ik] = occurenceRate[ik] + 1
            else:
                occurenceRate[ik] = 1
    ocl = len(res)
    for io in occurenceRate.keys():
        print("{0:20s} {1}%".format(io, int((occurenceRate[io] * 100) / ocl)))
    print(f"pocet zaznamu {ocl}")


if __name__ == '__main__':
    pass
    # querySreality(sfilter={
    #     "category_main_cb": 1,
    #     "category_sub_cb":"11|12",
    #     "category_type_cb": 1,
    #     "locality_region_id": 10,
    #     "tms": 1599903723673
    # })

    #srealityStableParams()

    # ishashidUnique()