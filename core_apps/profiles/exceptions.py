from rest_framework import APIException

class CantFollowYourself(APIException):
    status_code = 403
    default_detail = "You cant follow your self"
    default_code = "forbidden"