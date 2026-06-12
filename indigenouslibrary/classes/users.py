# Indigenous Mob
class IndigenousMob:
    def __init__(self, mob_id, mob_name):
        self.mob_id = mob_id
        self.mob_name = mob_name
#--#

#---#
# User Classes
#---#
class User:
    def __init__(self, user_id, first_name, last_name, email, password_hash, phone_number, date_joined):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = password_hash
        self.phone_number = phone_number
        self.date_joined = date_joined

    def request_access(self):
        return

    def request_authorisation(self):
        return
#---#
# Extended Users
#---#
class AuthorisedMobMember(User):
    def __init__(self, user_id, first_name, last_name, email, password_hash, phone_number, date_joined, associated_mob):
        User.__init__(self, user_id, first_name, last_name, email, password_hash, phone_number, date_joined)
        self.associated_mob = associated_mob
#--#
class Researcher(User):
    def __init__(self, user_id, first_name, last_name, email, password_hash, phone_number, date_joined, artefacts):
        User.__init__(self, user_id, first_name, last_name, email, password_hash, phone_number, date_joined)
        self.artefacts = artefacts
    def upload_new_artefacts(self):
        return
#---#
# Reviewers
#---#
class Reviewer(User):
    def __init__(self, user_id, first_name, last_name, email, password_hash, phone_number, date_joined, pending_reviews, reviews, active):
        User.__init__(self, user_id, first_name, last_name, email, password_hash, phone_number, date_joined)
        self.pending_reviews = pending_reviews
        self.reviews = reviews
        self.active = active

    def handoff_review(self):
        return
#--#
class AcademicReviewer(Reviewer):
    def __init__(self, user_id, first_name, last_name, email, password_hash, phone_number, date_joined, pending_reviews, reviews, active, field_of_study):
        Reviewer.__init__(self, user_id, first_name, last_name, email, password_hash, phone_number, date_joined, pending_reviews, reviews, active)
        self.field_of_study = field_of_study
#--#
class IndigenousReviewer(Reviewer, AuthorisedMobMember):
    def __init__(self, user_id, first_name, last_name, email, password_hash, phone_number, date_joined, pending_reviews, reviews, active, associated_mob):
        Reviewer.__init__(self, user_id, first_name, last_name, email, password_hash, phone_number, date_joined, pending_reviews, reviews, active)
        AuthorisedMobMember.__init__(self, associated_mob)
