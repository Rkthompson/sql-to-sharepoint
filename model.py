from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set

def add_to_batch(line: ListItem, batches: List[Batch]) -> str:
    batch = next(b for b in sorted(batches))
    batch.add_to_batch(line)
    return batch.reference

# ListItem class represents a value object that will 
# transition from SQL record to SharePoint List Item.

@dataclass(unsafe_hash=True)
class ListItem:
    id_number: int
    client_name: str
    job_number: int
    job_year: int
    job_description: str
    date_requested_by: date
    artwork_needed_by: date
    final_due_date: date
    assign_to: str
    requested_by: str
    request_status: str
    date_completed: date

# Batch class represents a collection of job requests
# as one or more ListItems

class Batch:
    def __init__(self):
        self._database_lines = set()  # type: Set[ListItem]

    def __repr__(self):
        return f"<Batch {self.reference}>"
        
    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

    def add_to_batch(self, database_line: ListItem):
        self._database_lines.add(database_line)

    