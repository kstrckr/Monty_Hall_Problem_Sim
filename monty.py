import random

class door:
    def __init__(self):
        self.isRevealed = False
        self.content = 0

    def __str__(self):
        return self.content

class three_doors:
    def __init__(self):
        self.doors = [door(), door(), door()]
        self.randomize_doors()

    def __str__(self):
        return str([(door.content, door.isRevealed) for door in self.doors])

    def randomize_doors(self):

        indexes_assigned = []

        while len(indexes_assigned) < 2:
            random_index = random.randint(0,2)
            if len(indexes_assigned) == 0:
                self.doors[random_index].content = 1
                indexes_assigned.append(random_index)
            else:
                if indexes_assigned[0] != random_index:
                    self.doors[random_index].content = 1
                    indexes_assigned.append(random_index)

class contestant:
    def __init__(self, doors):
        self.choice = random.randint(0,2)
        doors.doors[self.choice].isRevealed = True
        # self.switch_choice = random.choice([True, False])

    def switch_choice(self, doors):
        for index, door in enumerate(doors):
            if not door.isRevealed:
                doors[self.choice].isRevealed = False
                self.choice = index
                doors[self.choice].isRevealed = True
                break

class host:
    def reveal_one_door(self, doors):
        for door in doors:
            if not door.isRevealed and door.content == 1:
                door.isRevealed = True
                break

class game_instance:
    def __init__(self, switch_choice):
        self.doors = three_doors()
        self.contestant = contestant(self.doors)
        self.host = host()
        self.host.reveal_one_door(self.doors.doors)

        if switch_choice:
            self.contestant.switch_choice(self.doors.doors)

    def check_win(self):
        return self.doors.doors[self.contestant.choice].content == 0


def run_x_games(count, switch_choice):
    wins = 0
    losses = 0


    for i in range(0,count):

        game = game_instance(switch_choice)
        if game.check_win():
            wins += 1
        else:
            losses += 1

        # print(game.doors)
        # print(game.check_win())

    print("Changed Doors {} : Wins {} : Losses {} : Ratio {}".format(switch_choice, wins, losses, wins/count))


if __name__ == "__main__":
    run_x_games(10000, False)
    run_x_games(10000, True)
