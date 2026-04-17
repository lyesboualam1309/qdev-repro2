class ErreurTropCourt(ValueError):
    def __init__(self, n=None):
        if n is not None:
            self.message = f"{n} caractères tandis que le minimum est 5"
            super().__init__(self.message)
        else:
            super().__init__()

class ErreurTropLong(ValueError):
    def __init__(self, n=None):
        if n is not None:
            self.message = f"{n} caractères tandis que le maximum est 10"
            super().__init__(self.message)
        else:
            super().__init__()

def codeCommandeConforme(code: str) -> bool:
    numero = ['0','1','2','3','4','5','6','7','8','9']
    if len(code) < 5:
        raise ErreurTropCourt(len(code))
    if len(code) > 10:
        raise ErreurTropLong(len(code))
    if code[0] != "#":
        return False
    if code[1] not in numero or code[2] not in numero:
        return False
    for c in code[3:]:
        if not c.isalnum():
            return False
    return True
