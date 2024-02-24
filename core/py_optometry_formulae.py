# -*- coding: utf-8 -*-
"""py optometry formulae.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R3ZeaW1IlYAot-t1hryaxuCz5L-lMthu
"""


import numpy as np
import pandas as pd
import math

class OptometryFormulas:
    @staticmethod
    # prentice rule
    def prentice(distance, power):
      return distance * power

    @staticmethod
    # Back Vertex Distance Compensator
    def vertex_distance(distance, power):
      return power/(1-(distance*power))

    @staticmethod
    # Back Vertex Distance Compensator
    def back_vertex_power(prescription, old_distance, new_distance):
      pass

    @staticmethod
    # Equivalent power
    def equivalent_power(Fp, Bp, Distance, Index):
      return Fp + Bp - (Bp*Fp*(Distance/Index))

    @staticmethod
    # side vertex power
    def side_vertex_power(Fp, Bp, Distance, Index, front=True):
      if front:
        return Fp + (Bp / ( 1 - ((Bp * Distance)/Index)))
      else:
        return Bp + (Fp / ( 1 - ((Fp * Distance)/Index)))

    @staticmethod
    def CVF(nc, nm):
      '''
      CURVE VARIATION FACTOR
      nc = refractive index of base material, usually crown glass
      nm = refractive index of lens material
      '''
      return (nc -1)/(nm -1)

    @staticmethod
    def abbe_number(nd, nF, nC):
      '''
      ABBE NUMBER
      nd = refractive index for 587.56 nm
      nF = refractive index for 486.31 nm
      nC = refractive index for 656.28 nm
      '''
      return (nd-1)/(nF-nC)

    @staticmethod
    def trans_chromatic_abberation(c, F, v):
      '''v = Abbe number
      P = prismatic effect
      c = distance from the optical centre of the lens (in cm)
      F = lens power
      '''
      return  (c*F)/v

    @staticmethod
    def fresnel_refrectance(ns, nf):
      '''
      ns = refractive index of the second medium (medium into which the light is travelling)
      nf = refractive index of the first medium
      '''
      return ((ns- nf)/ (ns+ nf))**2


    @staticmethod
    def MARTINS_FORMULA_FOR_TILT(S, a):
      '''
      S = sphere power
      a = tilt
      '''
      return S*(1 + ((np.sin(np.deg2rad(a))**2)/3))

    @staticmethod
    def new_inset(P,L,F,S):
      '''
      P = monocular distance PD
      L = working distance in dioptres
      F = distance lens power
      S = eye (centre of rotation) to specs in dioptres
      '''
      return (P*L)/(L+F-S)

    @staticmethod
    def simple_transpostion(px):
      '''
      px(precription) = '+1.75/−0.75×90'
      '''
      px = px.replace(' ', '')
      sphere_split = px.split('/')
      cyl_split = sphere_split[1].split('x')

      if sphere_split[0] in ['plano', 'Plano', 'PLANO']:
        sphere = '0.00'
      else:
        sphere = sphere_split[0]

      axis = cyl_split[1]
      cyl = cyl_split[0]
      new_sphere = round(float(sphere) + float(cyl), 2)

      if int(axis) > 90:
        new_axis = int(axis) - 90
      elif int(axis) == 90:
        new_axis = 180
      else:
        new_axis = int(axis) + 90

      if cyl[0] == '-':
        if new_sphere > 0:
          return f'''{new_sphere:+.2f}/+{float(cyl[1:]):.2f}x{new_axis}'''
        elif new_sphere < 0:
          return f'''{new_sphere:+.2f}/+{float(cyl[1:]):.2f}x{new_axis}'''
        else:
          return f'''{new_sphere:+.2f}/+{float(cyl[1:]):.2f}x{new_axis}'''
      elif cyl[0] == '+':
        if new_sphere > 0:
          return f'''{new_sphere:+.2f}/-{float(cyl[1:]):.2f}x{new_axis}'''
        elif new_sphere < 0:
          return  f'''{new_sphere:+.2f}/-{float(cyl[1:]):.2f}x{new_axis}'''
        else:
          return f'''{new_sphere:+.2f}/-{float(cyl[1:]):.2f}x{new_axis}'''



    @staticmethod
    def base_toric_transpostion(px, bc):
      '''
      px(precription) = '+1.75/−0.75×90'
      bc = base curve
      '''
      bc = float(bc)
      px = px.replace(' ', '')
      sphere_split = px.split('/')
      cyl_split = sphere_split[1].split('x')

      if sphere_split[0] in ['plano', 'Plano', 'PLANO']:
        sphere = '0.00'
      else:
        sphere = sphere_split[0]

      axis = cyl_split[1]
      cyl = cyl_split[0]

      if (float(cyl) > 0) and (float(bc) > 0) or (float(cyl) < 0) and (float(bc) < 0):

        sphere_curve = float(sphere)-(float(bc))

        if int(axis) > 90:
          bc_axis = int(axis) - 90
        elif int(axis) == 90:
          bc_axis = 180
        else:
          bc_axis = int(axis) + 90

        new_cyl = float(bc)+float(cyl)

        if float(bc) < 0:
          print(f'      {sphere_curve:+.2f}')
          print('------'*4)
          bc_string = f'''{bc:+.2f}x{bc_axis}'''
          cyl_string = f'''{new_cyl:+.2f}x{axis}'''
          denominator = f'  {bc_string}/{cyl_string}'
          print(denominator)
          return f'''{sphere_curve:+.2f}/({denominator.replace(' ', '')})'''
        else:
          bc_string = f'''{bc:+.2f}x{bc_axis}'''
          cyl_string = f'''{new_cyl:+.2f}x{axis}'''
          denominator = f'  {bc_string}/{cyl_string}'
          print(denominator)
          print('------'*4)
          print(f'      {sphere_curve:+.2f}')
          return f'''({denominator.replace(' ', '')})/{sphere_curve:+.2f}'''

      else:
        px = simple_transpostion(px)
        px = px.replace(' ', '')
        sphere_split = px.split('/')
        cyl_split = sphere_split[1].split('x')

        if sphere_split[0] in ['plano', 'Plano', 'PLANO']:
          sphere = '0.00'
        else:
          sphere = sphere_split[0]

        axis = cyl_split[1]
        cyl = cyl_split[0]
        sphere_curve = float(sphere)-(float(bc))

        if int(axis) > 90:
          bc_axis = int(axis) - 90
        elif int(axis) == 90:
          bc_axis = 180
        else:
          bc_axis = int(axis) + 90

        new_cyl = float(bc)+float(cyl)

        if float(bc) < 0:
          print(f'      {sphere_curve:+.2f}')
          print('------'*4)
          bc_string = f'''{bc:+.2f}x{bc_axis}'''
          cyl_string = f'''{new_cyl:+.2f}x{axis}'''
          denominator = f'  {bc_string}/{cyl_string}'
          print(denominator)
          return f'''{sphere_curve:+.2f}/({denominator.replace(' ', '')})'''
        else:
          bc_string = f'''{bc:+.2f}x{bc_axis}'''
          cyl_string = f'''{new_cyl:+.2f}x{axis}'''
          denominator = f'  {bc_string}/{cyl_string}'
          print(denominator)
          print('------'*4)
          print(f'       {sphere_curve:+.2f}')
          return f'''({denominator.replace(' ', '')})/{sphere_curve:+.2f}'''

    @staticmethod
    def sphere_transpostion(px, sc):
      '''
      px(precription) = '+1.75/−0.75×90'
      sc = sphere curve
      '''
      sc = float(sc)
      px = px.replace(' ', '')
      sphere_split = px.split('/')
      cyl_split = sphere_split[1].split('x')

      if sphere_split[0] in ['plano', 'Plano', 'PLANO']:
        sphere = '0.00'
      else:
        sphere = sphere_split[0]

      axis = cyl_split[1]
      cyl = cyl_split[0]

      if ((float(cyl) > 0) and (float(sc) < 0)) or ((float(cyl) < 0) and (float(sc) > 0)):

        base_curve = float(sphere)-(float(sc))

        if int(axis) > 90:
          bc_axis = int(axis) - 90
        elif int(axis) == 90:
          bc_axis = 180
        else:
          bc_axis = int(axis) + 90

        new_cyl = float(base_curve)+float(cyl)

        if float(sc) > 0:
          print(f'      {sc:+.2f}')
          print('------'*4)
          bc_string = f'''{base_curve:+.2f}x{bc_axis}'''
          cyl_string = f'''{new_cyl:+.2f}x{axis}'''
          denominator = f'  {bc_string}/{cyl_string}'
          print(denominator)
          return f'''{sc:+.2f}/({denominator.replace(' ', '')})'''
        else:
          bc_string = f'''{base_curve:+.2f}x{bc_axis}'''
          cyl_string = f'''{new_cyl:+.2f}x{axis}'''
          denominator = f'  {bc_string}/{cyl_string}'
          print(denominator)
          print('------'*4)
          print(f'      {sc:+.2f}')
          return f'''({denominator.replace(' ', '')})/{sc:+.2f}'''

      else:
        px = simple_transpostion(px)
        px = px.replace(' ', '')
        sphere_split = px.split('/')
        cyl_split = sphere_split[1].split('x')

        if sphere_split[0] in ['plano', 'Plano', 'PLANO']:
          sphere = '0.00'
        else:
          sphere = sphere_split[0]

        axis = cyl_split[1]
        cyl = cyl_split[0]
        base_curve = float(sphere)-(float(sc))

        if int(axis) > 90:
          bc_axis = int(axis) - 90
        elif int(axis) == 90:
          bc_axis = 180
        else:
          bc_axis = int(axis) + 90

        new_cyl = float(base_curve)+float(cyl)

        if float(sc) > 0:
          print(f'      {sc:+.2f}')
          print('------'*4)
          bc_string = f'''{base_curve:+.2f}x{bc_axis}'''
          cyl_string = f'''{new_cyl:+.2f}x{axis}'''
          denominator = f'  {bc_string}/{cyl_string}'
          print(denominator)
          return f'''{sc:+.2f}/({denominator.replace(' ', '')})'''
        else:
          bc_string = f'''{base_curve:+.2f}x{bc_axis}'''
          cyl_string = f'''{new_cyl:+.2f}x{axis}'''
          denominator = f'  {bc_string}/{cyl_string}'
          print(denominator)
          print('------'*4)
          print(f'      {sc:+.2f}')
          return f'''({denominator.replace(' ', '')})/{sc:+.2f}'''

    @staticmethod
    def acurate_transpostion(px, t, n, bc=None, sc=None):
      '''
      px = '+1.75/-0.75x90'
      sc = sphere curve
      bc = base curve
      F2 = base curve/cross curve
      F = sphere power
      F1 = sphere curve
      t = thickness of the lens
      n = refractive index

    -------- formula ---------
      F2 = F − F1/[1 − (t/n) F1]
      '''
      if bc != None:
        bc = float(bc)
        px = px.replace(' ', '')
        sphere_split = px.split('/')
        cyl_split = sphere_split[1].split('x')

        if sphere_split[0] in ['plano', 'Plano', 'PLANO']:
          f = '0.00'
        else:
          f = sphere_split[0]

        axis = cyl_split[1]
        cyl = cyl_split[0]

        if (float(cyl) > 0) and (float(bc) > 0) or (float(cyl) < 0) and (float(bc) < 0):

          front_curve = float(f)-(float(bc))

          cci = float(f) - (front_curve/(1 - ((t/n)*front_curve)))
          ccii = (float(f) + float(cyl))- (front_curve/(1 - ((t/n)*front_curve)))

          if int(axis) > 90:
            bc_axis = int(axis) - 90
          elif int(axis) == 90:
            bc_axis = 180
          else:
            bc_axis = int(axis) + 90

          print(f'{front_curve:+.2f}')
          print('------'*4)
          print(f'{cci:+.2f}x{bc_axis}/{ccii:+.2f}x{axis}')

        else:
          px = simple_transpostion(px)
          px = px.replace(' ', '')
          acurate_transpostion(px, t, n, bc)


      elif sc != None:
        sc = float(sc)
        px = px.replace(' ', '')
        sphere_split = px.split('/')
        cyl_split = sphere_split[1].split('x')

        if sphere_split[0] in ['plano', 'Plano', 'PLANO']:
          f = '0.00'
        else:
          f = sphere_split[0]

        axis = cyl_split[1]
        cyl = cyl_split[0]

        if (float(cyl) > 0) and (float(sc) < 0) or (float(cyl) < 0) and (float(sc) > 0):

          front_curve = sc

          cci = float(f) - (front_curve/(1 - ((t/n)*front_curve)))
          ccii = (float(f) + float(cyl))- (front_curve/(1 - ((t/n)*front_curve)))

          if int(axis) > 90:
            bc_axis = int(axis) - 90
          elif int(axis) == 90:
            bc_axis = 180
          else:
            bc_axis = int(axis) + 90

          print(f'{front_curve:+.2f}')
          print('------'*4)
          print(f'{cci:+.2f}x{bc_axis}/{ccii:+.2f}x{axis}')

        else:
          px = simple_transpostion(px)
          px = px.replace(' ', '')
          acurate_transpostion(px, t, n, sc)

    @staticmethod
    def pxrx(pwr1, pwr2, axis_at_pwr1=None, axis_at_pwr2=None):
      if axis_at_pwr2 != None:
        if pwr1 > pwr2:
          sph = pwr1
          cyl= pwr2-pwr1
          axis = f'{int(axis_at_pwr2)}'
        else:
          sph = pwr2
          cyl= pwr1-pwr2
          axis = f'{int(axis_at_pwr2 - 90)}' if axis_at_pwr1 > 90 else f'{int(axis_at_pwr2 + 90)}'

      elif axis_at_pwr1 != None:
        if pwr1 > pwr2:
          sph = pwr1
          cyl= pwr2-pwr1
          axis = f'{int(axis_at_pwr1 - 90)}' if axis_at_pwr1 > 90 else f'{int(axis_at_pwr1 + 90)}'
        else:
          sph = pwr2
          cyl= pwr1-pwr2
          axis = f'{int(axis_at_pwr1)}'

      sph = f'{sph:+.2f}'
      cyl = f'{cyl:+.2f}'
      rx = f'{sph}DS/{cyl}DCx{axis}'
      return rx




