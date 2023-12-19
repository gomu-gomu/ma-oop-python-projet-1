import streamlit as st
from calcul import Calcul



def main():
  
  st.image('./assets/fsr-logo.png')
  st.write('# Bienvenu à notre calculatrice')

  valeur1 = st.number_input('valeur1')
  valeur2 = st.number_input('valeur2')
  
  mon_calc = Calcul(valeur1, valeur2)

  st.divider()
  col1, col2, col3, col4 = st.columns(4)

  if col1.button('somme'):
    col1.write(mon_calc.calcul_somme())

  if col2.button('soustraction'):
    col2.write(mon_calc.calcul_soustraction())

  if col3.button('multiplication'):
    col3.write(mon_calc.calcul_multiplication())

  if col4.button('division'):
    col4.write(mon_calc.calcul_division())

if __name__ == '__main__':
  main()
