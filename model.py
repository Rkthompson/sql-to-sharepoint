from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set

# ListItem class represents a value object that will 
# transition from SQL record to SharePoint List Item.

@dataclass(frozen=True)
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
        self._to_batch = set()  # type: ListItem
        
    def add_to_batch(self, request: ListItem):
        self._to_batch.add(request)