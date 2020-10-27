import os
def BASE_DIR(ji):
    return print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



BASE_DIR('asgi.py')
# s = os.path.join(BASE_DIR,'static')
# print(s)
