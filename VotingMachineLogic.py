from PyQt6.QtWidgets import *
from VotingMachineRawGuiV0_1 import *
from VotingMachineDataKeeper import *

class Voting_Machine_Logic(QMainWindow, Ui_MainWindow):
    """Controls the voting machine window."""

    def __init__(self):
        """Sets up the window and connects buttons."""
        super().__init__()
        self.setupUi(self)

        self.REF_data_keeper = VotingMachineDataKeeper() # a ref to data keeper
        self.REF_data_keeper.Check_for_CSVs() # make blank CSVs if they don't exist

        # - - - - - Connect the buttons to Methods - - - - -
        # - - Main Menu - -
        self.VoteButton.clicked.connect(lambda: self.Go_To_Voting_Page())
        self.ViewButton.clicked.connect(lambda: self.Go_To_Viewing_Page())
        # - - Voting Page - -
        self.ConfirmVoteButton.clicked.connect(lambda: self.Try_to_Vote())
        self.BackFromVotingButton.clicked.connect(lambda: self.Go_To_Main_Menu())
        # - - Viewing Page - -
        self.BackFromViewerButton.clicked.connect(lambda: self.Go_To_Main_Menu())



    # - - - - - Page Navigation Methods - - - - -
    # page indexes:
    # 0 = main menu
    # 1 = voting page
    # 2 = viewing page

    def Go_To_Voting_Page(self):
        """Goes to the voting page."""
        self.stackedWidget.setCurrentIndex(1) # this is how we can switch pages
        self.ErrorLabel.hide()

    def Go_To_Viewing_Page(self):
        """Goes to the viewing page."""
        self.stackedWidget.setCurrentIndex(2)
        self.Update_Vote_Viewer()

    def Go_To_Main_Menu(self):
        """Goes to the main menu."""
        self.stackedWidget.setCurrentIndex(0)



    # - - - - - Action Methods - - - - -
    def Try_to_Vote(self):
        """Checks and saves a vote."""
        ID = self.IDTextBox.text()
        if (self.Is_this_a_valid_ID(ID)):
            pass # keep this pass
        else:
            self.Invalid_ID_Error()
            return
        if self.JohnButton.isChecked():
            self.Save_Vote("John")
            self.Save_ID(ID)
            self.Reset_Vote()
        elif self.JaneButton.isChecked():
            self.Save_Vote("Jane")
            self.Save_ID(ID)
            self.Reset_Vote()

        else:
            self.No_Vote_Error()
    def Reset_Vote(self):
        """Resets the vote form."""
        self.IDTextBox.setText("")
        self.JohnButton.setAutoExclusive(False)
        self.JaneButton.setAutoExclusive(False)

        self.JohnButton.setChecked(False)
        self.JaneButton.setChecked(False)

        self.JohnButton.setAutoExclusive(True)
        self.JaneButton.setAutoExclusive(True)
        self.ErrorLabel.hide()




    # - - - - - Misc Methods - - - - -
    def Update_Vote_Viewer(self):
        """Updates the vote totals."""

        john_votes, jane_votes = self.REF_data_keeper.Read_Votes()
        self.JohnVotesLabel.setText("Votes for John: " + str(john_votes))
        self.JaneVotesLabel.setText("Votes for Jane: " + str(jane_votes))

    def Save_Vote(self, candidate):
        """Stores a vote."""
        self.REF_data_keeper.Store_Vote(candidate)

    def Save_ID(self, ID):
        """Stores an ID."""
        self.REF_data_keeper.Store_ID(ID)


    def No_Vote_Error(self):
        """Shows no vote error."""
        self.ErrorLabel.setText("Choose candidate")
        self.ErrorLabel.show()


    def Invalid_ID_Error(self):
        """Shows invalid ID error."""
        self.ErrorLabel.setText("Enter Valid ID")
        self.ErrorLabel.show()

    def Is_this_a_valid_ID(self, ID):
        """Returns True if the ID is valid."""
        if ID == "":
            return False
        if (self.REF_data_keeper.Check_ID(ID)):
            return False
        return True