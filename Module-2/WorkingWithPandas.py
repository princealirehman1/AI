import pandas as pd

class WorkingWithPandas:

    def __init__(self):
        pass

    def setWeeklySchedule(self):
        self.schedule = pd.Series(["Chiken Biryani", "Beef Biryani","Mutton","Nehari","Chinees"],["Menu1","Menu2","Menu3","Menu4","Menu5"])

        print(self.schedule.index)
        print(self.schedule.values)

wwpd = WorkingWithPandas()

wwpd.setWeeklySchedule()