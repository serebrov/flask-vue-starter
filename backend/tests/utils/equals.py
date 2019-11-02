from datetime import datetime
import re
from uuid import UUID


class EqualsInteger:
    """Helper to check that the value we compare to is integer.

    For example,

    def test_compare_dicts():
        assert {
            'userName':'bob',
            'id': 2004
        } == {
            'userName': 'bob',
            'lastModified': EqualsInteger()
        }
    """

    def __eq__(self, other):
        return type(other) == int


class EqualsString:
    """Helper to check that the value we compare to is string."""

    def __eq__(self, other):
        return type(other) == str


class EqualsUUIDString:
    """Helper to check that the value we compare to is string with UUID."""

    def __eq__(self, other):
        if type(other) != str:
            return False
        try:
            UUID(other)
        except ValueError:
            return False
        return True


class EqualsRegexp:
    """Helper to check that the value we compare to matches the regexp."""

    def __init__(self, regexp):
        self._regexp = regexp

    def __eq__(self, other):
        result = re.search(self._regexp, str(other))
        if not result:
            print("Regexp comparison failed: {} #= {}".format(self._regexp, other))
        return result


class EqualsDatetimeString:
    """Helper to check that the value we compare to is datetime string."""

    def __init__(self, date_format):
        self._date_format = date_format

    def __eq__(self, other):
        dt = datetime.strptime(other, self._date_format)
        return type(dt) == datetime


class EqualsAnything:
    """Helper to ignore some of the values when comparing dicts.

    For example,

    def test_compare_dicts():
        assert {
            'userName':'bob',
            'lastModified':'2012-01-01'
        } == {
            'userName': 'bob',
            'lastModified': EqualsAnything()
        }
    """

    def __eq__(self, other):
        return True


class EqualsPartialDict:
    """Helper to assert some keys/values in a dict.

    For example,

    def test_compare_dicts():
        assert {
            'userName':'bob',
            'id': 2004
        } == EqualsPartialDict({
            'userName': 'bob',
        })
    """

    def __init__(self, expected_dict, chain="root"):
        assert type(expected_dict) == dict
        self.expected_dict = expected_dict
        self.chain = chain

    def __eq__(self, other):
        assert type(other) == dict
        for key in self.expected_dict:
            expected_value = self.expected_dict[key]
            other_value = other[key]

            if type(expected_value) == dict:
                assert type(other_value) == dict
                chain = self.chain + " -> " + key
                expected = EqualsPartialDict(expected_value, chain)
                assert expected == other_value

            result = other_value == expected_value
            if not result:
                print(
                    "Partial comparison failed in {}: {} #= {}\n".format(
                        self.chain + " -> " + key, expected_value, other_value
                    )
                )
                return False
        return True
