class Calcul:
  def __init__(self, a, b) -> None:
    self.a = a
    self.b = b
  
  def __verifier_numerique(self):
    return isinstance(self.a, (float, int)) and isinstance(self.b, (float, int))
  
  def calcul_somme(self):
    if self.__verifier_numerique():
      return self.a + self.b
    else:
      return 'Erreur : Les valeurs doivent être numériques'
  
  def calcul_soustraction(self):
    if self.__verifier_numerique():
      return self.a - self.b
    else:
      return 'Erreur : Les valeurs doivent être numériques'
  
  def calcul_multiplication(self):
    if self.__verifier_numerique():
      return self.a * self.b
    else:
      return 'Erreur : Les valeurs doivent être numériques'
  
  def calcul_division(self):
    if self.__verifier_numerique():
      try:
        return self.a / self.b
      except ZeroDivisionError:
        return 'Erreur : Division par zéro'
    else:
      return 'Erreur : Les valeurs doivent être numériques'
