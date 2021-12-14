# System Architecture: User -> Auth Server -> ctx -> service.method(ctx, params…)
# Design contents are immutable after created
# DesignService.methods(ctx,.......)

# service = DesignService()
# foo_id = service.create_design(ctx, 'foo')
# service.get_design(ctx, foo_id) -> 'foo'


import unittest
from typing import List, Iterable
from collections import defaultdict


# Identifies the caller of a service method.


class AuthContext:
    def __init__(self, user_id: str):
        self.user_id = user_id  # E.g. ‘userAbc’

# Any calls made to this service are authenticated.


class DesignServiceInterface:
    def __init__(self,
                 id_to_design: dict = {},
                 user_id_to_design_id: dict = defaultdict(set),
                 ):
        self.id_to_design = id_to_design
        self.user_id_to_design_id = user_id_to_design_id

    def create_design(self, ctx: AuthContext, design_content: str) -> str:
        """Creates a design and returns the design id"""
        if not ctx:
            raise Exception('AuthContext not provided')

        next_design_id = len(self.id_to_design)
        self.id_to_design[next_design_id] = design_content
        self.user_id_to_design_id[ctx.user_id].add(next_design_id)

        return next_design_id

    def get_design(self, ctx: AuthContext, design_id: str) -> str:
        """Returns the design content, if the user has access to the design."""
        if not ctx:
            raise Exception('AuthContext not provided')

        if design_id not in self.user_id_to_design_id[ctx.user_id]:
            raise Exception('404 Not Found')

        return self.id_to_design.get(design_id)

    def find_designs(self, ctx: AuthContext) -> Iterable[str]:
        """Returns a list of design ids that the given context has access to."""
        if not ctx:
            raise Exception('AuthContext not provided')

        return self.user_id_to_design_id.get(ctx.user_id)

    def share_design(self,
                     ctx: AuthContext,
                     design_id: str,
                     user_to_share_with_id: str,
                     ) -> None:
        """Gives a specific user access to the design. Assume user ids are valid"""
        if not ctx:
            raise Exception('AuthContext not provided')

        if design_id not in self.user_id_to_design_id[ctx.user_id]:
            raise Exception('404 Not Found')

        self.user_id_to_design_id[user_to_share_with_id].add(design_id)
        return


class DesignServiceTest(unittest.TestCase):

    user1 = "USER_1"
    user2 = "USER_2"

    def setUp(self):
        self.design_service = DesignServiceInterface()

    def test_sharing(self):
        user_one = AuthContext("USER_1")
        user_two = AuthContext("USER_2")
        design_id = self.design_service.create_design(user_one, "foobar")
        self.design_service.share_design(user_one, design_id, user_two.user_id)
        self.assertEqual(self.design_service.find_designs(user_one),
                         self.design_service.find_designs(user_two),
                         )


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(DesignServiceTest)
    unittest.TextTestRunner().run(suite)
