class ErreurTropCourt(ValueError):
  def __init__(self, n = None):
    if n is not None:
      self.message = f"{n} caractères tandis que le minimum est 5"
      super().__init__(self.message)
    else:
      super().__init__()

class ErreurTropLong(ValueError):
  def __init__(self, n = None):
    if n is not None:
      self.message = f"{n} caractères tandis que le maximum est 10"
      super().__init__(self.message)
    else:
      super().__init__()
