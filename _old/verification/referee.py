from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee

from tests import TESTS


def forbidden(code, runner):
    if len(code) >= 140:
        return False, "Hm, I counted {} symbols.".format(len(code))
    return True, "ok"


api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        function_name="flat_list",
        inspector=forbidden
    ).on_ready)
