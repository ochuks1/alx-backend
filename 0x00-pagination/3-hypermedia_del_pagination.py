#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

from typing import Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    
    # (Reuse the dataset and get_hyper methods from the previous tasks)

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return pagination details with support for deleted items.
        Args:
            index (int): Start index.
            page_size (int): Size of the page.
        Returns:
            Dict: Pagination metadata and page data.
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.indexed_dataset()
        dataset_size = len(indexed_dataset)

        data = []
        next_index = index
        while len(data) < page_size and next_index < dataset_size:
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
