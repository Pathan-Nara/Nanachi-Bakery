from buildings.Casino import Casino
from buildings.JorysHouse import JorysHouse
from buildings.Mine import Mine
from buildings.RastaStreet import RastaStreet
from buildings.PoissonAJorys import PoissonAJorys
from buildings.ChienAgrejon import ChienAgrejon


class BuildingList:
    def __init__(self):
        self.buildings = [
            Casino(),
            JorysHouse(),
            Mine(),
            RastaStreet(),
            PoissonAJorys(),
            ChienAgrejon()
        ]

    def get_buildings(self):
        return self.buildings