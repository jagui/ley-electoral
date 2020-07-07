from operator import itemgetter


class DHont:
    def __init__(self, votes, num_seats):
        self.votes = sorted(votes, key=itemgetter(1), reverse=True)
        self.num_seats = num_seats

    def calculate_seats(self):
        seats = [0] * self.num_seats
        iterations = [
            [None for i in range(len(self.votes))] for j in range(self.num_seats)
        ]
        for i in range(0, self.num_seats):
            iteration = iterations[i]
            for j in range(0, len(self.votes)):
                iteration[j] = {
                    "party": self.votes[j][0],
                    "quotient": round(self.votes[j][1] / (seats[j] + 1)),
                    "seats": seats[j],
                }
            max_value = max(iteration, key=itemgetter("quotient"))
            max_index = iteration.index(max_value)
            seats[max_index] += 1
            iteration[max_index]["seats"] += 1
        return [{"party": d["party"], "seats": d["seats"]} for d in iterations[-1]]


if __name__ == "__main__":
    dHont = DHont(
        votes=[("A", 340000), ("B", 280000), ("C", 160000), ("D", 60000), ("E", 15000)],
        num_seats=7,
    )

    seats = dHont.calculate_seats()
    print(*seats, sep="\n")
