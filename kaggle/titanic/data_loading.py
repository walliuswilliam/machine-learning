import sys
sys.path.append('kaggle/titanic')
sys.path.append('src')
from parse_line import parse_line
from dataframe import DataFrame


data_types = {
    "PassengerId": int,
    "Survived": int,
    "Pclass": int,
    "Name": str,
    "Sex": str,
    "Age": float,
    "SibSp": int,
    "Parch": int,
    "Ticket": str,
    "Fare": float,
    "Cabin": str,
    "Embarked": str
}

df = DataFrame.from_csv("datasets/dataset_of_knowns.csv", data_types=data_types, parser=parse_line)
assert df.columns == ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]

assert df.to_array()[:5] == [
  [1, 0, 3, '"Braund, Mr. Owen Harris"', "male", 22, 1, 0, "A/5 21171", 7.25, None, "S"],
  [2, 1, 1, '"Cumings, Mrs. John Bradley (Florence Briggs Thayer)"', "female", 38, 1, 0, "PC 17599", 71.2833, "C85", "C"],
  [3, 1, 3, '"Heikkinen, Miss. Laina"', "female", 26, 0, 0, "STON/O2. 3101282", 7.925, None, "S"],
  [4, 1, 1, '"Futrelle, Mrs. Jacques Heath (Lily May Peel)"', "female", 35, 1, 0, "113803", 53.1, "C123", "S"],
  [5, 0, 3, '"Allen, Mr. William Henry"', "male", 35, 0, 0, "373450", 8.05, None, "S"]
  ]


new_columns = ["PassengerId", "Survived", "Pclass", "Surname", "Sex", "Age", "SibSp", "Parch", "TicketType", "TicketNumber", "Fare", "CabinType", "CabinNumber", "Embarked"]

cols = ["PassengerId", "Survived", "Pclass", "Surname", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]

def name_splitter(input_string):
  return input_string.split(',')[0][1:]

df.apply('Name', name_splitter)
df = DataFrame.from_array(df.to_array(), cols)

def cabin_splitter(input_string):
  if input_string is not '' and input_string is not None:
    if ' ' in input_string:
      input_string = input_string.split(' ')[0]
    if len(input_string[1:]) > 0:
      return (input_string[0], int(input_string[1:]))
    else:
      return (input_string[0], None)
  else:
    return (None, None)


cabin_types = []
cabin_numbers = []
for cabin_number in df.data_dict['Cabin']:
  split_cabin = cabin_splitter(cabin_number)
  cabin_types.append(split_cabin[0])
  cabin_numbers.append(split_cabin[1])

df.data_dict['CabinType'] = cabin_types
df.data_dict['CabinNumber'] = cabin_numbers

del df.data_dict['Cabin']
df.columns.remove('Cabin')


def ticket_splitter(input_string):
  if input_string is not None:
    if ' ' in input_string:
      input_string = input_string[::-1]
      input_string = input_string.split(' ', 1)
      input_string = input_string[::-1]
      return (input_string[0][::-1], int(input_string[1][::-1]))
    else:
      if input_string.isdigit():
        return (None, int(input_string))
      else:
        return (input_string, None)
  else:
    return (None, None)


ticket_types = []
ticket_numbers = []
for ticket_number in df.data_dict['Ticket']:
  split_ticket = ticket_splitter(ticket_number)
  ticket_types.append(split_ticket[0])
  ticket_numbers.append(split_ticket[1])

df.data_dict['TicketType'] = ticket_types
df.data_dict['TicketNumber'] = ticket_numbers

del df.data_dict['Ticket']
df.columns.remove('Ticket')

df = DataFrame(df.data_dict, new_columns)


print('testing sub variables...')
assert df.columns == ["PassengerId", "Survived", "Pclass", "Surname", "Sex", "Age", "SibSp", "Parch", "TicketType", "TicketNumber", "Fare", "CabinType", "CabinNumber", "Embarked"]

assert df.to_array()[:5] == [
  [1, 0, 3, "Braund", "male", 22.0, 1, 0, "A/5", 21171, 7.25, None, None, "S"],
  [2, 1, 1, "Cumings", "female", 38.0, 1, 0, "PC", 17599, 71.2833, "C", 85, "C"],
  [3, 1, 3, "Heikkinen", "female", 26.0, 0, 0, "STON/O2.", 3101282, 7.925, None, None, "S"],
  [4, 1, 1, "Futrelle", "female", 35.0, 1, 0, None, 113803, 53.1, "C", 123, "S"],
  [5, 0, 3, "Allen", "male", 35.0, 0, 0, None, 373450, 8.05, None, None, "S"]]
print('passed')






print('initial analysis of data...')
print(df.group_by('Sex').to_array())