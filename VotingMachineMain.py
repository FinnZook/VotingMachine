from VotingMachineLogic import *





def Voting_Machine_Main():
    """Starts the voting machine program."""

    # - - - - - Setup - - - - -
    REF_application = QApplication([])
    REF_window = Voting_Machine_Logic()
    REF_window.show()
    REF_application.exec()



if __name__ == '__main__':
    Voting_Machine_Main()