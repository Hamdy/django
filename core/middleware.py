from typing import Any


class Mymiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
    
    def __call__(self, req) -> Any:
        return self.get_response(req)

    def process_request(self, req):
        ...


    def process_response(self, req, res):
        return res
