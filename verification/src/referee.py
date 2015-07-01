from checkio_referee import RefereeBase, ENV_NAME


import settings_env
from tests import TESTS


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "flat_list"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "flatList"
    }
