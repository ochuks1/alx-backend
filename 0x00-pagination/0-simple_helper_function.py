#!/usr/bin/env python3
"""Simple helper function."""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple containing the start and end index for pagination.
    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.
    Returns:
        tuple: Start and end index for the page.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
