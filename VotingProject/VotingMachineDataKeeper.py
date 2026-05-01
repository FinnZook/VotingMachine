import csv
import os

class VotingMachineDataKeeper():
    """Keeps track of voting data."""


    def Check_for_CSVs(self):
        """Creates CSV files if missing."""
        if not os.path.exists("votes.csv"):
            open("votes.csv", "w").close()
        if not os.path.exists("IDs.csv"):
            open("IDs.csv", "w").close()



    def Store_Vote(self, candidate):
        """Stores a candidate vote."""
        with open("votes.csv", "a") as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow([candidate])

    def Store_ID(self, ID):
        """Stores a voter ID."""
        with open("IDs.csv", "a") as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow([ID])

    def Read_Votes(self):
        """Returns total votes for John and Jane."""
        john_votes = 0
        jane_votes = 0
        with open("votes.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) > 0 and row[0] == "John":
                    john_votes += 1
                elif len(row) > 0 and row[0] == "Jane":
                    jane_votes += 1
        return john_votes, jane_votes

    def Check_ID(self, ID):
        """Returns True if ID already exists."""
        with open("IDs.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) > 0 and row[0] == ID:
                    return True
            return False