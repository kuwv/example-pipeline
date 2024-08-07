# SPDX-FileCopyrightText: © 2024 Jesse P. Johnson <jpj6652@gmail.com>
# SPDX-License-Identifier: Unlicensed

"""Provide example pipelines to prototype github actions."""

import logging
from typing import List

__author__ = 'Jesse P. Johnson'
__title__ = 'example_pipeline'
__version__ = '0.1.0.post1'
__all__: List[str] = []

logging.getLogger(__name__).addHandler(logging.NullHandler())
