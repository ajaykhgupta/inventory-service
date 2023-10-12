from fastapi import HTTPException


class NotFoundException(HTTPException):

    def __init__(self, status_code=404, detail="Not Found!") -> None:
        super().__init__(status_code=status_code, detail=detail)


class BadRequestException(HTTPException):

    def __init__(self, status_code=400, detail="Bad Request!") -> None:
        super().__init__(status_code=status_code, detail=detail)
