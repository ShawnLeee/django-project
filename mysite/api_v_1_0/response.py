import json
class LSResponse():
    def __init__(self, status=1 , err_msg='',data = None):
        self.status = status
        self.err_msg = err_msg
        self.data = data

    def to_json(self):
        json_res = {
            'status' : self.status,
            'err_msg' : self.err_msg,
            'data' : self.data,
        }
        return json_res

