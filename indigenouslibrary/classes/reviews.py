#---#
# Review Base Class
#---#
class ReviewCaseBase:
    def __init__(self, review_case_id, review_status, artefact_to_review, contributing_reviews):
        self.review_case_id = review_case_id
        self.review_status = review_status
        self.artefact_to_review = artefact_to_review
        self.contributing_reviews = contributing_reviews

    def finalise_review(self):
        return
    def assign_reviewers(self):
        return
#---#
# Access Review Class
#---#
class AccessReviewCase:
    def __init__(self, review_case_id, review_status, artefact_to_review, contributing_reviews, reason, requesting_user):
        ReviewCaseBase.__init__(self, review_case_id, review_status, artefact_to_review, contributing_reviews)
        self.reason = reason
        self.requesting_user = requesting_user

    def grant_access(self):
        return


# ---#
# Revision Review Case Class
# ---#
class RevisionRequestCase:
    def __init__(self, review_case_id, review_status, artefact_to_review, contributing_reviews, requesting_user, complaint,
                 hide_during_review):
        ReviewCaseBase.__init__(self, review_case_id, review_status, artefact_to_review, contributing_reviews)
        self.requesting_user = requesting_user
        self.complaint = complaint
        self.hide_during_review = hide_during_review

    def update_review_status(self):
        return
    def assign_new_reviewers(self):
        return
#---#
# Live View Case Class
#---#
class LiveViewCase:
    def __init__(self, review_case_id, review_status, artefact_to_review, contributing_reviews, reason, requesting_user, requested_date):
        ReviewCaseBase.__init__(self, review_case_id, review_status, artefact_to_review, contributing_reviews)
        self.reason = reason
        self.requesting_user = requesting_user
        self.requested_date = requested_date

    def approve_request(self):
        return
#---#
# Review Class
#---#
class Review:
    def __init__(self, review_id, review_date, review_author, review_comments, review_decision, review_pending):
        self.review_id = review_id
        self.review_date = review_date
        self.review_author = review_author
        self.review_comments = review_comments
        self.review_decision = review_decision
        self.review_pending = review_pending
    def submit_review(self):
        return

