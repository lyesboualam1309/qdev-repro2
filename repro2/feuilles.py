from enum import Enum

class Reponse(Enum):
    ACCEPTER_SANS_ALERTE = 0
    ACCEPTER_ALERTE_ORANGE = 1
    ACCEPTER_ALERTE_ROUGE = 2
    REFUSER = 3

def verifierCommandeImpression(nbFeuillesNecessaires: int, nbFeuillesEnStock: int) -> Reponse:
    if nbFeuillesNecessaires <= 0:
        raise ValueError("Erreur")
    if nbFeuillesNecessaires > 2000:
        return Reponse.REFUSER
    difference = nbFeuillesEnStock - nbFeuillesNecessaires
    if difference > 50:
        return Reponse.ACCEPTER_SANS_ALERTE
    if 1 <= difference <= 50:
        return Reponse.ACCEPTER_ALERTE_ORANGE
    if difference == 0:
        return Reponse.ACCEPTER_ALERTE_ROUGE
    if difference < 0:
        return Reponse.REFUSER
