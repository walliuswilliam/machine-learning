def parse_line(line):
  entries = []
  entry_str = ""
  inside_quotes = False
  quote_symbol = None

  for char in line:
    if char == ',' and inside_quotes is False:
      entries.append(str(entry_str))
      entry_str = ""

    else:
      entry_str += char
      if (char == "'" or char == '"') and (char == quote_symbol or quote_symbol is None):
        inside_quotes = not inside_quotes
        quote_symbol = char
        
  entries.append(entry_str)
  return entries


# print('testing line parser...')
# line_1 = "1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,7.25,,S"
# assert parse_line(line_1) == ['1', '0', '3', "'Braund, Mr. Owen Harris'", 'male', '22', '1', '0', 'A/5 21171', '7.25', '', 'S'], parse_line(line_1)

# line_2 = '102,0,3,"Petroff, Mr. Pastcho (""Pentcho"")",male,,0,0,349215,7.8958,,S'
# assert parse_line(line_2) == ['102', '0', '3', '"Petroff, Mr. Pastcho (""Pentcho"")"', 'male', '', '0', '0', '349215', '7.8958', '', 'S'], parse_line(line_2)

# line_3 = '187,1,3,"O\'Brien, Mrs. Thomas (Johanna ""Hannah"" Godfrey)",female,,1,0,370365,15.5,,Q'
# assert parse_line(line_3) == ['187', '1', '3', '"O\'Brien, Mrs. Thomas (Johanna ""Hannah"" Godfrey)"', 'female', '', '1', '0', '370365', '15.5', '', 'Q']
# print('passed')
