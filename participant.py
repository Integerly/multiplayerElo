class Participant:
    def __init__(self, id, current_rating, prev_participations):
        self.id = id
        self.current_rating = current_rating
        self.prev_participations = prev_participations
        self.new_rating = current_rating
