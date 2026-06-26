"""
Batcher

Responsibility:
- Split tasks into manual batches.
- No external batching libraries.
"""


class Batcher:

    def __init__(self, batch_size=2):

        self.batch_size = batch_size

    def create_batches(self, tasks):

        batches = []

        current_batch = []

        for task in tasks:

            current_batch.append(task)

            if len(current_batch) == self.batch_size:

                batches.append(current_batch)

                current_batch = []

        if len(current_batch) > 0:

            batches.append(current_batch)

        return batches