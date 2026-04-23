#!/usr/bin/env python3
"""
Module containing index_range helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start and end indexes for a given page and page size.

    Args:
        page: The page number (1-indexed).
        page_size: The number of items per page.

    Returns:
        A tuple (start_index, end_index) for the requested page.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
