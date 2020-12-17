
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN COMMENT C_BRACE C_PAREN DIV ELSE EQUALS G_THAN ID IF L_THAN MINUS MULT NUMBER O_BRACE O_PAREN PLUS PRINT PRINTLN SEMICOLON STRING VARIABLE_NAME WHILEstart : start variable_assignment\n\t\t| variable_assignmentoperator : PLUS\n\t\t\t| MINUS\n\t\t\t| MULT\n\t\t\t| DIVexpr : O_PAREN VARIABLE_NAME operator VARIABLE_NAME C_PARENexpr : O_PAREN VARIABLE_NAME operator NUMBER C_PAREN\n\t\t\t| O_PAREN VARIABLE_NAME operator expr C_PARENexpr : O_PAREN NUMBER operator VARIABLE_NAME C_PAREN\n\t\t\t| O_PAREN expr operator VARIABLE_NAME C_PARENexpr : O_PAREN expr operator expr C_PAREN\n\t\t\t| O_PAREN NUMBER operator expr C_PAREN\n\t\t\t| O_PAREN expr operator NUMBER C_PAREN\n\t\t\t| O_PAREN NUMBER operator NUMBER C_PARENvariable_assignment : VARIABLE_NAME ASSIGN NUMBER SEMICOLON\n\t\t\t\t\t\t| VARIABLE_NAME ASSIGN expr SEMICOLONvariable_assignment : VARIABLE_NAME ASSIGN STRING SEMICOLONvariable_assignment : VARIABLE_NAME ASSIGN VARIABLE_NAME SEMICOLON'
    
_lr_action_items = {'VARIABLE_NAME':([0,1,2,4,5,10,11,12,13,14,18,19,20,21,22,23,24,],[3,3,-2,-1,6,15,-19,-16,-17,-18,25,-3,-4,-5,-6,29,32,]),'$end':([1,2,4,11,12,13,14,],[0,-2,-1,-19,-16,-17,-18,]),'ASSIGN':([3,],[5,]),'NUMBER':([5,10,18,19,20,21,22,23,24,],[7,16,26,-3,-4,-5,-6,28,33,]),'STRING':([5,],[9,]),'O_PAREN':([5,10,18,19,20,21,22,23,24,],[10,10,10,-3,-4,-5,-6,10,10,]),'SEMICOLON':([6,7,8,9,34,35,36,37,38,39,40,41,42,],[11,12,13,14,-7,-8,-9,-15,-10,-13,-12,-11,-14,]),'PLUS':([15,16,17,34,35,36,37,38,39,40,41,42,],[19,19,19,-7,-8,-9,-15,-10,-13,-12,-11,-14,]),'MINUS':([15,16,17,34,35,36,37,38,39,40,41,42,],[20,20,20,-7,-8,-9,-15,-10,-13,-12,-11,-14,]),'MULT':([15,16,17,34,35,36,37,38,39,40,41,42,],[21,21,21,-7,-8,-9,-15,-10,-13,-12,-11,-14,]),'DIV':([15,16,17,34,35,36,37,38,39,40,41,42,],[22,22,22,-7,-8,-9,-15,-10,-13,-12,-11,-14,]),'C_PAREN':([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[34,35,36,37,38,39,40,41,42,-7,-8,-9,-15,-10,-13,-12,-11,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'variable_assignment':([0,1,],[2,4,]),'expr':([5,10,18,23,24,],[8,17,27,30,31,]),'operator':([15,16,17,],[18,23,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> start variable_assignment','start',2,'p_start','main.py',94),
  ('start -> variable_assignment','start',1,'p_start','main.py',95),
  ('operator -> PLUS','operator',1,'p_operator','main.py',99),
  ('operator -> MINUS','operator',1,'p_operator','main.py',100),
  ('operator -> MULT','operator',1,'p_operator','main.py',101),
  ('operator -> DIV','operator',1,'p_operator','main.py',102),
  ('expr -> O_PAREN VARIABLE_NAME operator VARIABLE_NAME C_PAREN','expr',5,'p_expr_variable','main.py',106),
  ('expr -> O_PAREN VARIABLE_NAME operator NUMBER C_PAREN','expr',5,'p_expr_variable_a','main.py',120),
  ('expr -> O_PAREN VARIABLE_NAME operator expr C_PAREN','expr',5,'p_expr_variable_a','main.py',121),
  ('expr -> O_PAREN NUMBER operator VARIABLE_NAME C_PAREN','expr',5,'p_expr_variable_b','main.py',134),
  ('expr -> O_PAREN expr operator VARIABLE_NAME C_PAREN','expr',5,'p_expr_variable_b','main.py',135),
  ('expr -> O_PAREN expr operator expr C_PAREN','expr',5,'p_expr','main.py',148),
  ('expr -> O_PAREN NUMBER operator expr C_PAREN','expr',5,'p_expr','main.py',149),
  ('expr -> O_PAREN expr operator NUMBER C_PAREN','expr',5,'p_expr','main.py',150),
  ('expr -> O_PAREN NUMBER operator NUMBER C_PAREN','expr',5,'p_expr','main.py',151),
  ('variable_assignment -> VARIABLE_NAME ASSIGN NUMBER SEMICOLON','variable_assignment',4,'p_variable_assignment_number','main.py',163),
  ('variable_assignment -> VARIABLE_NAME ASSIGN expr SEMICOLON','variable_assignment',4,'p_variable_assignment_number','main.py',164),
  ('variable_assignment -> VARIABLE_NAME ASSIGN STRING SEMICOLON','variable_assignment',4,'p_variable_assignment_string','main.py',174),
  ('variable_assignment -> VARIABLE_NAME ASSIGN VARIABLE_NAME SEMICOLON','variable_assignment',4,'p_variable_assignment_var','main.py',184),
]