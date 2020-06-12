from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import Aborter


class NoContentException(HTTPException):
    code = 204
    description = 'No content'


abort = Aborter(extra={204: NoContentException})
