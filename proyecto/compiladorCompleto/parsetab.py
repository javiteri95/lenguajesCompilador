
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'EQUALS ARREGLO LPAREN RPAREN FUNCION NUMBERS OPERADOR NUMPY POINT ARRAY COMA RCORCHER LCORCHER NP VAR ID IMPORT AS ZEROS FROMstatement  : arreglo\n                  | ID EQUALS arreglo\n                  | VAR EQUALS arreglo\n                  | operacion\n                  | ID EQUALS operacion\n                  | VAR EQUALS operacion\n                  | importacion\n                  importacion : IMPORT NUMPY AS ID\n                   | IMPORT NUMPY\n                   | FROM NUMPY IMPORT ARRAY\n                   | FROM NUMPY IMPORT ARRAY AS ID\n                   | FROM NUMPY IMPORT ID\n                   | FROM NUMPY IMPORT ID AS ID\n                   | IMPORT ID AS ID\n                   | IMPORT ID\n                   | FROM ID IMPORT ID\n                   | FROM ID IMPORT ID AS IDvariosarreglos : ARREGLO RPAREN\n                      | ARREGLO COMA variosarreglos\n                      variosarreglos2 : ARREGLO RCORCHER\n                      | ARREGLO COMA variosarreglos2\n                      arreglo : NP POINT ARRAY LPAREN LPAREN variosarreglos RPAREN\n               | NP POINT ARRAY LPAREN LCORCHER variosarreglos2 RPAREN\n               | NP POINT ARRAY LPAREN LCORCHER RCORCHER RPAREN\n               | NP POINT ARRAY LPAREN LPAREN RPAREN RPAREN\n               | NP POINT ARRAY LPAREN ARREGLO RPAREN\n               | NP POINT FUNCION LPAREN LPAREN variosarreglos RPAREN\n               | NP POINT FUNCION LPAREN LCORCHER variosarreglos2 RPAREN\n               | NP POINT FUNCION LPAREN LCORCHER RCORCHER RPAREN\n               | NP POINT FUNCION LPAREN LPAREN RPAREN RPAREN\n               | NP POINT FUNCION LPAREN ARREGLO RPAREN\n               | NP POINT ZEROS LPAREN NUMBERS COMA NUMBERS RPAREN\n               | NUMPY POINT ARRAY LPAREN LPAREN variosarreglos RPAREN\n               | NUMPY POINT ARRAY LPAREN LCORCHER variosarreglos2 RPAREN\n               | NUMPY POINT ARRAY LPAREN LCORCHER RCORCHER RPAREN\n               | NUMPY POINT ARRAY LPAREN LPAREN RPAREN RPAREN\n               | NUMPY POINT ARRAY LPAREN ARREGLO RPAREN\n               | NUMPY POINT FUNCION LPAREN LPAREN variosarreglos RPAREN\n               | NUMPY POINT FUNCION LPAREN LCORCHER variosarreglos2 RPAREN\n               | NUMPY POINT FUNCION LPAREN LCORCHER RCORCHER RPAREN\n               | NUMPY POINT FUNCION LPAREN LPAREN RPAREN RPAREN\n               | NUMPY POINT FUNCION LPAREN ARREGLO RPAREN\n               | FUNCION LPAREN LPAREN variosarreglos RPAREN\n               | FUNCION LPAREN LCORCHER variosarreglos2 RPAREN\n               | FUNCION LPAREN LCORCHER RCORCHER RPAREN\n               | FUNCION LPAREN LPAREN RPAREN RPAREN\n               | FUNCION LPAREN ARREGLO RPAREN\n               | NUMPY POINT ZEROS LPAREN NUMBERS COMA NUMBERS RPARENoperacion : VAR OPERADOR VAR\n                 '
    
_lr_action_items = {'COMA':([52,54,59,66,],[75,78,84,95,]),'ARREGLO':([19,37,38,42,43,45,46,60,62,63,65,68,69,71,72,75,78,],[36,52,54,61,64,67,70,54,52,54,52,52,54,52,54,52,54,]),'FROM':([0,],[11,]),'POINT':([3,5,],[14,15,]),'OPERADOR':([2,24,],[13,13,]),'LCORCHER':([19,42,43,45,46,],[38,60,63,69,72,]),'RCORCHER':([38,54,60,63,69,72,],[53,79,85,90,99,104,]),'EQUALS':([2,9,],[12,18,]),'RPAREN':([36,37,50,51,52,53,55,61,62,64,65,67,68,70,71,76,79,85,86,88,89,90,91,93,94,97,98,99,100,102,103,104,105,106,107,111,120,],[49,50,73,74,76,77,80,87,88,92,93,96,97,101,102,-18,-20,112,113,114,115,116,117,118,119,121,122,123,124,125,126,127,128,-19,-21,129,130,]),'VAR':([0,12,13,18,],[2,24,25,24,]),'AS':([16,17,56,57,58,],[32,33,81,82,83,]),'ZEROS':([14,15,],[26,29,]),'NUMBERS':([41,44,84,95,],[59,66,111,120,]),'LPAREN':([10,19,26,27,28,29,30,31,42,43,45,46,],[19,37,41,42,43,44,45,46,62,65,68,71,]),'NP':([0,12,18,],[5,5,5,]),'IMPORT':([0,20,21,],[6,39,40,]),'ARRAY':([14,15,39,],[27,30,56,]),'$end':([1,4,7,8,16,17,22,23,25,34,35,47,48,49,56,57,58,73,74,77,80,87,92,96,101,108,109,110,112,113,114,115,116,117,118,119,121,122,123,124,125,126,127,128,129,130,],[-1,0,-7,-4,-9,-15,-6,-3,-49,-5,-2,-8,-14,-47,-10,-12,-16,-46,-43,-45,-44,-37,-42,-26,-31,-11,-13,-17,-35,-34,-36,-33,-40,-39,-41,-38,-25,-22,-24,-23,-30,-27,-29,-28,-48,-32,]),'NUMPY':([0,6,11,12,18,],[3,16,20,3,3,]),'ID':([0,6,11,32,33,39,40,81,82,83,],[9,17,21,47,48,57,58,108,109,110,]),'FUNCION':([0,12,14,15,18,],[10,10,28,31,10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'importacion':([0,],[7,]),'operacion':([0,12,18,],[8,22,34,]),'variosarreglos':([37,62,65,68,71,75,],[51,89,94,98,103,106,]),'arreglo':([0,12,18,],[1,23,35,]),'variosarreglos2':([38,60,63,69,72,78,],[55,86,91,100,105,107,]),'statement':([0,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> arreglo','statement',1,'p_statement','compilador numpy.py',70),
  ('statement -> ID EQUALS arreglo','statement',3,'p_statement','compilador numpy.py',71),
  ('statement -> VAR EQUALS arreglo','statement',3,'p_statement','compilador numpy.py',72),
  ('statement -> operacion','statement',1,'p_statement','compilador numpy.py',73),
  ('statement -> ID EQUALS operacion','statement',3,'p_statement','compilador numpy.py',74),
  ('statement -> VAR EQUALS operacion','statement',3,'p_statement','compilador numpy.py',75),
  ('statement -> importacion','statement',1,'p_statement','compilador numpy.py',76),
  ('importacion -> IMPORT NUMPY AS ID','importacion',4,'p_importacion','compilador numpy.py',87),
  ('importacion -> IMPORT NUMPY','importacion',2,'p_importacion','compilador numpy.py',88),
  ('importacion -> FROM NUMPY IMPORT ARRAY','importacion',4,'p_importacion','compilador numpy.py',89),
  ('importacion -> FROM NUMPY IMPORT ARRAY AS ID','importacion',6,'p_importacion','compilador numpy.py',90),
  ('importacion -> FROM NUMPY IMPORT ID','importacion',4,'p_importacion','compilador numpy.py',91),
  ('importacion -> FROM NUMPY IMPORT ID AS ID','importacion',6,'p_importacion','compilador numpy.py',92),
  ('importacion -> IMPORT ID AS ID','importacion',4,'p_importacion','compilador numpy.py',93),
  ('importacion -> IMPORT ID','importacion',2,'p_importacion','compilador numpy.py',94),
  ('importacion -> FROM ID IMPORT ID','importacion',4,'p_importacion','compilador numpy.py',95),
  ('importacion -> FROM ID IMPORT ID AS ID','importacion',6,'p_importacion','compilador numpy.py',96),
  ('variosarreglos -> ARREGLO RPAREN','variosarreglos',2,'p_variosarreglos','compilador numpy.py',143),
  ('variosarreglos -> ARREGLO COMA variosarreglos','variosarreglos',3,'p_variosarreglos','compilador numpy.py',144),
  ('variosarreglos2 -> ARREGLO RCORCHER','variosarreglos2',2,'p_variosarreglos2','compilador numpy.py',163),
  ('variosarreglos2 -> ARREGLO COMA variosarreglos2','variosarreglos2',3,'p_variosarreglos2','compilador numpy.py',164),
  ('arreglo -> NP POINT ARRAY LPAREN LPAREN variosarreglos RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',182),
  ('arreglo -> NP POINT ARRAY LPAREN LCORCHER variosarreglos2 RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',183),
  ('arreglo -> NP POINT ARRAY LPAREN LCORCHER RCORCHER RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',184),
  ('arreglo -> NP POINT ARRAY LPAREN LPAREN RPAREN RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',185),
  ('arreglo -> NP POINT ARRAY LPAREN ARREGLO RPAREN','arreglo',6,'p_arreglo','compilador numpy.py',186),
  ('arreglo -> NP POINT FUNCION LPAREN LPAREN variosarreglos RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',187),
  ('arreglo -> NP POINT FUNCION LPAREN LCORCHER variosarreglos2 RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',188),
  ('arreglo -> NP POINT FUNCION LPAREN LCORCHER RCORCHER RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',189),
  ('arreglo -> NP POINT FUNCION LPAREN LPAREN RPAREN RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',190),
  ('arreglo -> NP POINT FUNCION LPAREN ARREGLO RPAREN','arreglo',6,'p_arreglo','compilador numpy.py',191),
  ('arreglo -> NP POINT ZEROS LPAREN NUMBERS COMA NUMBERS RPAREN','arreglo',8,'p_arreglo','compilador numpy.py',192),
  ('arreglo -> NUMPY POINT ARRAY LPAREN LPAREN variosarreglos RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',193),
  ('arreglo -> NUMPY POINT ARRAY LPAREN LCORCHER variosarreglos2 RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',194),
  ('arreglo -> NUMPY POINT ARRAY LPAREN LCORCHER RCORCHER RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',195),
  ('arreglo -> NUMPY POINT ARRAY LPAREN LPAREN RPAREN RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',196),
  ('arreglo -> NUMPY POINT ARRAY LPAREN ARREGLO RPAREN','arreglo',6,'p_arreglo','compilador numpy.py',197),
  ('arreglo -> NUMPY POINT FUNCION LPAREN LPAREN variosarreglos RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',198),
  ('arreglo -> NUMPY POINT FUNCION LPAREN LCORCHER variosarreglos2 RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',199),
  ('arreglo -> NUMPY POINT FUNCION LPAREN LCORCHER RCORCHER RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',200),
  ('arreglo -> NUMPY POINT FUNCION LPAREN LPAREN RPAREN RPAREN','arreglo',7,'p_arreglo','compilador numpy.py',201),
  ('arreglo -> NUMPY POINT FUNCION LPAREN ARREGLO RPAREN','arreglo',6,'p_arreglo','compilador numpy.py',202),
  ('arreglo -> FUNCION LPAREN LPAREN variosarreglos RPAREN','arreglo',5,'p_arreglo','compilador numpy.py',203),
  ('arreglo -> FUNCION LPAREN LCORCHER variosarreglos2 RPAREN','arreglo',5,'p_arreglo','compilador numpy.py',204),
  ('arreglo -> FUNCION LPAREN LCORCHER RCORCHER RPAREN','arreglo',5,'p_arreglo','compilador numpy.py',205),
  ('arreglo -> FUNCION LPAREN LPAREN RPAREN RPAREN','arreglo',5,'p_arreglo','compilador numpy.py',206),
  ('arreglo -> FUNCION LPAREN ARREGLO RPAREN','arreglo',4,'p_arreglo','compilador numpy.py',207),
  ('arreglo -> NUMPY POINT ZEROS LPAREN NUMBERS COMA NUMBERS RPAREN','arreglo',8,'p_arreglo','compilador numpy.py',208),
  ('operacion -> VAR OPERADOR VAR','operacion',3,'p_operacion','compilador numpy.py',225),
]
