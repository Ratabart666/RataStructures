import pytest
import re


def handle_not_implemented(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AttributeError as exp:
            regex_result = re.findall(pattern="'(.*?)'", string=str(exp))
            module = regex_result[0]
            attribute = regex_result[1]
            if "has no attribute " in str(exp):
                pytest.skip(
                    attribute + "() is not implemented yet at module: " + module)
            else:
                raise exp
        except:
            raise
    return wrapper
