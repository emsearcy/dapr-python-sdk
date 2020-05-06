# -*- coding: utf-8 -*-

"""
Copyright (c) Microsoft Corporation.
Licensed under the MIT License.
"""

from .calltype import ActorCallType


class ActorMethodContext:
    """A Actor method context that contains method information invoked
    by :class:`ActorRuntime`.
    """
    def __init__(self, method_name: str, call_type: ActorCallType):
        self._method_name = method_name
        self._call_type = call_type

    @property
    def method_name(self) -> str:
        """Return method name"""
        return self._method_name

    @property
    def call_type(self) -> ActorCallType:
        """Return :class:`ActorCallType` for this method"""
        return self._call_type

    @classmethod
    def create_for_actor(cls, method_name: str):
        """Helper to create :class:`ActorMethodContext` object
        for actor_interface_method type
        """
        return ActorMethodContext(method_name, ActorCallType.actor_interface_method)
