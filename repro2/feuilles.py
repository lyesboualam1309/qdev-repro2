from enum import Enum

class Reponse(Enum):
  ACCEPTER_SANS_ALERTE = 0,
  ACCEPTER_ALERTE_ORANGE = 1,
  ACCEPTER_ALERTE_ROUGE = 2,
  REFUSER = 3

def verifierCommandeImpression(nbFeuillesNecessaires : int, nbFeuillesEnStock : int) -> Reponse:
  pass
