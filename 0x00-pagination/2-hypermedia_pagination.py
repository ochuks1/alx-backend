#!/usr/bin/env python3
"""Hypermedia pagination with additional metadata."""

import math
from typing import Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    
    # (Reuse the dataset and get_page methods from Task 1)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return pagination details with metadata.
        Args:
            page (int): Page number.
            page_size (int): Size of the page.
        Returns:
            Dict: Pagination metadata and page data.
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
