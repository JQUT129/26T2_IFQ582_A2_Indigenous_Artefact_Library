from enum import Enum


class Visibility(Enum):
    PRIVATE = 1
    UNLISTED = 2
    RESTRICTED = 3
    PUBLIC = 4

class ReviewDecision(Enum):
    ACCEPTED = 1
    REJECTED = 2
    CHANGES_REQUESTED = 3

class ReviewStatus(Enum):
    SUBMITTED = 1
    IN_REVIEW = 2
    COMPLETED = 3