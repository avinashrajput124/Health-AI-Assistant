import rest_framework
from rest_framework.views import exception_handler
from rest_framework.exceptions import (
        AuthenticationFailed,
        NotFound
    )
from rest_framework.views import Response
from rest_framework import status

from tokenize import Token
from utils.exceptions.custom_exception import *


def error_handler(exc, context):
    """Custom API exception handler."""
    response = exception_handler(exc, context)
    payload = {
        'status_code': status.HTTP_200_OK,
        'resultCode': '0',
        'errorMessage': '',
        'actionPerformed': ''
    }
    paginatin_payload = {"count": 0,
                    "next": "null",
                    "previous": "null",
                    "results": []
                    }
    

    if response is not None:

        if isinstance(exc, rest_framework.exceptions.ValidationError):
            error = list(exc.detail.values())
            error = error[0]
            error = str(error[0])
            if 'pk' in error:
                field = str(list(exc.detail.keys())[0])
                payload['errorMessage'] = "Invalid {} id".format(field)
                payload['actionPerformed'] = "Invalid {} id".format(field)
                payload['resultCode'] = '0'
                resp = Response(payload, status=status.HTTP_200_OK)
                return resp
            else:
                payload['errorMessage'] = exc.detail
                payload['actionPerformed'] = exc.detail
                payload['resultCode'] = '0'
                resp = Response(payload, status=status.HTTP_200_OK)
                return resp

        if isinstance(exc, TokenDecodError):
            payload['errorMessage'] = exc.error
            payload['actionPerformed'] = exc.error
            payload['resultCode'] = '0'
            resp = Response(payload, status=status.HTTP_200_OK)
            return resp

        if isinstance(exc, AuthenticationError):
            payload['errorMessage'] = exc.error
            payload['actionPerformed'] = exc.error
            payload['resultCode'] = '3'
            resp = Response(payload, status=status.HTTP_200_OK)
            return resp
        
        if isinstance(exc, rest_framework.exceptions.NotAuthenticated):
            payload['errorMessage'] = 'Missing Authentication Token'
            payload['actionPerformed'] = ''
            payload['resultCode'] = '0'
            resp = Response(payload, status=status.HTTP_200_OK)
            return resp
        
        if isinstance(exc, InvalidTokenError):
            payload['errorMessage'] = exc.error
            payload['actionPerformed'] = exc.error
            payload['resultCode'] = '5'
            resp = Response(payload, status=status.HTTP_200_OK)
            return resp    

        if isinstance(exc, AuthenticationFailed):
            payload['errorMessage'] = 'Token has been expired'
            payload['actionPerformed'] = 'Token has been expired'
            payload['resultCode'] = '4'
            resp = Response(payload, status=status.HTTP_200_OK)
            return resp

        if isinstance(exc, ValidationError):
            payload['errorMessage'] = exc.error
            payload['actionPerformed'] = exc.detail
            resp = Response(payload, status=status.HTTP_200_OK)
            return resp

        if isinstance(exc, NotFound):
            payload['errorMessage'] = exc.error
            payload['actionPerformed'] = exc.detail
            resp = Response(payload, status=status.HTTP_200_OK)
            return resp

        if isinstance(exc, ValueError):
            payload['errorMessage'] = exc.error
            payload['actionPerformed'] = exc.detail
            resp = Response(payload, status=status.HTTP_200_OK)
            return resp
        
        if isinstance(exc, ResponseError):
            payload['errorMessage'] = exc.error
            payload['actionPerformed'] = exc.detail
            resp = Response(payload, status=status.HTTP_200_OK)
            return resp
    
        if isinstance(exc, PageNotFound):
            # paginatin_payload['result'] = exc.msg
            resp = Response(paginatin_payload, status=status.HTTP_200_OK)
            return resp

        if isinstance(exc, AuthorizationError):
            payload['errorMessage'] = exc.error
            payload['actionPerformed'] = exc.error
            resp = Response(payload, status=status.HTTP_200_OK)
            return resp
        
        if isinstance(exc, rest_framework.exceptions.NotFound):
            payload['errorMessage'] = "Invalid page number"
            payload['actionPerformed'] = "Invalid page number"
            resp = Response(payload, status=status.HTTP_200_OK)
            return resp
        
