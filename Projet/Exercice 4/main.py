from .robot_mobile import RobotCMobile
from .robot import RobotC, Direction


#specialized robot classes:
class RobotSurveillance(RobotCMobile):
    def sendOrientation(self, other_robot: RobotCMobile) -> None:
        """Share orientation with another robot"""
        other_robot.setOrientation(self.orientation)

class RobotAccueil(RobotCMobile):
    def accueillir(self, visiteur: str) -> str:
        return f"Bienvenue {visiteur}!"
    
    def indiqueChemin(self, destination: str) -> str:
        return f"Pour aller à {destination}, suivez-moi."
    
    def prendreRendezVous(self, details: str) -> str:
        return f"Rendez-vous enregistré: {details}"

class RobotChirurgical(RobotC):
    def __init__(self, id: int):
        super().__init__(id, "Chirurgical")
        
    def preparerInstrument(self, instrument: str) -> None:
        print(f"Préparation de {instrument}")
    
    def suivreOperation(self) -> None:
        print("Suivi de l'opération en cours")
    
    def assisterChirurgien(self) -> None:
        print("Assistance au chirurgien")

class RobotNettoyage(RobotCMobile):
    def nettoyerZone(self, zone: str) -> None:
        print(f"Nettoyage de la zone {zone}")
    
    def decontaminer(self) -> None:
        print("Décontamination en cours")

def main():
    # Create array of 4 different robots
    robots = [
        RobotSurveillance(id=1),
        RobotAccueil(id=2),
        RobotChirurgical(id=3),
        RobotNettoyage(id=4)
    ]
    
    # 1. Surveillance Robot Demo
    surveillance_robot = robots[0]
    print("\n=== Démonstration Robot de Surveillance ===")
    # Change orientation and share with reception robot
    surveillance_robot.setOrientation(Direction.EST)
    surveillance_robot.sendOrientation(robots[1])
    print(f"Robot de surveillance orienté vers: {surveillance_robot.orientation.name}")
    print(f"Robot d'accueil orienté vers: {robots[1].orientation.name}")
    
    # 2. Reception Robot Demo
    reception_robot = robots[1]
    print("\n=== Démonstration Robot d'Accueil ===")
    print(reception_robot.accueillir("Dr. Martin"))
    print(reception_robot.indiqueChemin("Bloc Opératoire"))
    print(reception_robot.prendreRendezVous("Consultation Cardiologie - 14h"))
    
    # 3. Surgical Robot Demo
    surgical_robot = robots[2]
    print("\n=== Démonstration Robot Chirurgical ===")
    surgical_robot.preparerInstrument("Scalpel")
    surgical_robot.suivreOperation()
    surgical_robot.assisterChirurgien()
    
    # 4. Cleaning Robot Demo
    cleaning_robot = robots[3]
    print("\n=== Démonstration Robot de Nettoyage ===")
    # Move to different locations and clean
    cleaning_robot.setOrientation(Direction.NORD)
    cleaning_robot.avancer(2.0)
    cleaning_robot.nettoyerZone("Couloir")
    
    cleaning_robot.setOrientation(Direction.EST)
    cleaning_robot.avancer(1.0)
    cleaning_robot.nettoyerZone("Salle d'opération")
    cleaning_robot.decontaminer()
    
    # Display final positions
    print("\n=== Positions Finales des Robots ===")
    for robot in robots:
        print(f"Robot {robot.id} ({robot.category}) - Position: "
              f"x={robot.position.x:.1f}, y={robot.position.y:.1f}, z={robot.position.z:.1f}")

if __name__ == "__main__":
    main()