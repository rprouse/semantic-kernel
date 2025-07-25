# Copyright (c) Microsoft. All rights reserved.

from collections.abc import Sequence
from typing import TypeVar, Union

from semantic_kernel.services.ai_service_client_base import AIServiceClientBase

AI_SERVICE_CLIENT_TYPE = TypeVar("AI_SERVICE_CLIENT_TYPE", bound=AIServiceClientBase)

T = TypeVar("T")

OneOrMany = Union[T, Sequence[T]]
OneOrList = Union[T, list[T]]
OptionalOneOrMany = Union[T, Sequence[T], None]
OptionalOneOrList = Union[T, list[T], None]

__all__ = ["AI_SERVICE_CLIENT_TYPE", "OneOrList", "OneOrMany", "OptionalOneOrList", "OptionalOneOrMany"]
