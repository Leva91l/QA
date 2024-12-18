from faker import Faker

fake = Faker()


class Ticket:
    def __init__(self, question):
        self.question = question


class TicketGenerator:
    def __init__(self, group):
        self.group = group

    def generate_tickets(self):
        for i in range(len(self.group)):
            yield Ticket(fake.text(max_nb_chars=20))
