#---#
# Artefact Base Class
#---#
class ArtefactBase:
    def __init__(self, artefact_id, author, last_updated, visibility, sensitive, collection,
                 authorised_users, reviews, description, mob,
                 location, date_created, date_discovered, cultural_context,
                 culturally_sensitive, cultural_sensitivity_reason, restriction_reason):
        self.artefact_id = artefact_id
        self.author = author
        self.last_updated = last_updated
        self.visibility = visibility
        self.sensitive = sensitive
        self.collection = collection
        self.authorised_users = authorised_users
        self.reviews = reviews
        self.description = description
        self.mob = mob
        self.location = location
        self.date_created = date_created
        self.date_discovered = date_discovered
        self.cultural_context = cultural_context
        self.culturally_sensitive = culturally_sensitive
        self.cultural_sensitivity_reason = cultural_sensitivity_reason
        self.restriction_reason = restriction_reason

#---#
# Audio Artefact
#---#
class AudioArtefact(ArtefactBase):
    def __init__(self, artefact_id, author, last_updated, visibility, sensitive, collection,
                 authorised_users, reviews, description, mob,
                 location, date_created, date_discovered, cultural_context,
                 culturally_sensitive, cultural_sensitivity_reason, restriction_reason, audio_file):
        ArtefactBase.__init__(self, artefact_id, author, last_updated, visibility, sensitive,
                              collection, authorised_users, reviews, description, mob, location,
                              date_created, date_discovered, cultural_context, culturally_sensitive,
                              cultural_sensitivity_reason, restriction_reason)
        self.audio_file = audio_file