import logging
logging.basicConfig(level=logging.DEBUG)

def buggy_func(a,b):
    result=a*b
    logging.debug(f"a: {a} b: {b} result: {result}")
    return result
print(buggy_func(3,3))