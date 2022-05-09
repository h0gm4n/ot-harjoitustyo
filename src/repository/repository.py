
import os.path

dirname = os.path.dirname(__file__)


class Repository:

    def __init__(self):
        self.easy_results_repository = (os.path.join(dirname, "..", "data", "easy_results.csv"))
        self.normal_results_repository = (os.path.join(dirname, "..", "data", "normal_results.csv"))
        self.hard_results_repository = (os.path.join(dirname, "..", "data", "hard_results.csv"))
        self.results_list = [self.easy_results_repository, self.normal_results_repository, self.hard_results_repository]

    def write(self, player_name, time, difficulty):
        if difficulty == 0:
            with open(self.easy_results_repository, "a", encoding="utf8") as file:
                file.write(f"{player_name},{time}\n")
        elif difficulty == 1:
            with open(self.normal_results_repository, "a", encoding="utf8") as file:
                file.write(f"{player_name},{time}\n")
        elif difficulty == 2:
            with open(self.hard_results_repository, "a", encoding="utf8") as file:
                file.write(f"{player_name},{time}\n")

    def clear_results(self):
        for i in self.results_list:
            with open(i, "w", encoding="utf8"):
                pass

    def create_or_maintain_result_files(self):
        for i in self.results_list:
            with open(i, "a", encoding="utf8"):
                pass
