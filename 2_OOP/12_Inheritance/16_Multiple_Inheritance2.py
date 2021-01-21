class Team():
    def setTeam(self, team):
        self.team = team
    
    def showTeam(self):
        print (self.team)


class tipeHero():
    def setTipe (self, tipe):
        self.tipe = tipe
    
    def showTipe (self):
        print (self.tipe)



class Hero(Team, tipeHero):
    def __init__(self, name):
        self.name = name


ucup = Hero ('ucup')


ucup.setTeam('nirwana')
ucup.setTipe('MM')
ucup.showTeam()
ucup.showTipe()