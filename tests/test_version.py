# SPDX-FileCopyrightText: © 2024 Jesse P. Johnson <jpj6652@gmail.com>
# SPDX-License-Identifier: Unlicensed
"""Provide versioning sanity check."""

from example_pipeline import __version__


def test_version():
    assert __version__ == '0.1.0.post3'
