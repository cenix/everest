"""

This file is part of the everest project.
See LICENSE.txt for licensing, CONTRIBUTORS.txt for contributor information.

Created on Oct 1, 2014.
"""
from everest.resources.base import Member


class MyEntityGrandparentMember(Member):
    relation = 'http://test.org/myentity-grandparent'
