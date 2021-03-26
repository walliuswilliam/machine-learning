import sys
sys.path.append('kaggle/titanic')
sys.path.append('src')
from parse_line import parse_line
from dataframe import DataFrame
from polynomial_regressor import PolynomialRegressor


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
  if input_string != '' and input_string is not None:
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


# print('testing sub variables...')
# assert df.columns == ["PassengerId", "Survived", "Pclass", "Surname", "Sex", "Age", "SibSp", "Parch", "TicketType", "TicketNumber", "Fare", "CabinType", "CabinNumber", "Embarked"]

# assert df.to_array()[:5] == [
#   [1, 0, 3, "Braund", "male", 22.0, 1, 0, "A/5", 21171, 7.25, None, None, "S"],
#   [2, 1, 1, "Cumings", "female", 38.0, 1, 0, "PC", 17599, 71.2833, "C", 85, "C"],
#   [3, 1, 3, "Heikkinen", "female", 26.0, 0, 0, "STON/O2.", 3101282, 7.925, None, None, "S"],
#   [4, 1, 1, "Futrelle", "female", 35.0, 1, 0, None, 113803, 53.1, "C", 123, "S"],
#   [5, 0, 3, "Allen", "male", 35.0, 0, 0, None, 373450, 8.05, None, None, "S"]]
# print('passed')




# print('\ninitial analysis of data...\n')

# print('Pclass')
# print('mean survival', df.group_by("Pclass").aggregate("Survived", "avg").select(["Pclass", "Survived"]).to_array())
# print('count', df.group_by("Pclass").aggregate("Survived", "count").select(["Pclass", "Survived"]).to_array(), '\n')

# print('Sex')
# print('mean survival', df.group_by("Sex").aggregate("Survived", "avg").select(["Sex", "Survived"]).to_array())
# print('count', df.group_by("Sex").aggregate("Survived", "count").select(["Sex", "Survived"]).to_array(), '\n')

# print('SibSp')
# print('mean survival', df.group_by("SibSp").aggregate("Survived", "avg").select(["SibSp", "Survived"]).to_array())
# print('count', df.group_by("SibSp").aggregate("Survived", "count").select(["SibSp", "Survived"]).to_array(), '\n')

# print('Parch')
# print('mean survival', df.group_by("Parch").aggregate("Survived", "avg").select(["Parch", "Survived"]).to_array())
# print('count', df.group_by("Parch").aggregate("Survived", "count").select(["Parch", "Survived"]).to_array(), '\n')

# print('CabinType')
# print('mean survival', df.group_by("CabinType").aggregate("Survived", "avg").select(["CabinType", "Survived"]).to_array())
# print('count', df.group_by("CabinType").aggregate("Survived", "count").select(["CabinType", "Survived"]).to_array(), '\n')

# print('Embarked')
# print('mean survival', df.group_by("Embarked").aggregate("Survived", "avg").select(["Embarked", "Survived"]).to_array())
# print('count', df.group_by("Embarked").aggregate("Survived", "count").select(["Embarked", "Survived"]).to_array())



# print('\n\nAge')

# age_0_10 = df.where(lambda row: row['Age'] != None).where(lambda row: 0 < row['Age'] <= 10)

# age_10_20 = df.where(lambda row: row['Age'] != None).where(lambda row: 10 < row['Age'] <= 20)

# age_20_30 = df.where(lambda row: row['Age'] != None).where(lambda row: 20 < row['Age'] <= 30)

# age_30_40 = df.where(lambda row: row['Age'] != None).where(lambda row: 30 < row['Age'] <= 40)

# age_40_50 = df.where(lambda row: row['Age'] != None).where(lambda row: 40 < row['Age'] <= 50)

# age_50_60 = df.where(lambda row: row['Age'] != None).where(lambda row: 50 < row['Age'] <= 60)

# age_60_70 = df.where(lambda row: row['Age'] != None).where(lambda row: 60 < row['Age'] <= 70)

# age_70_80 = df.where(lambda row: row['Age'] != None).where(lambda row: 70 < row['Age'] <= 80)


# ages = [age_0_10, age_10_20, age_20_30, age_30_40, age_40_50, age_50_60, age_60_70, age_70_80]

# age_names = ['age_0_10', 'age_10_20', 'age_20_30', 'age_30_40', 'age_40_50', 'age_50_60', 'age_60_70', 'age_70_80']

# for age_group in ages:
#   age_selected = age_group.select(["Survived"]).to_array()
#   total = 0
#   for data_point in age_selected:
#     total += data_point[0]

#   avg = total/len(age_selected)
#   print(age_names[ages.index(age_group)] + '\n', 'average:', round(avg, 2), '\n', 'count:', len(age_selected), '\n')



# print('\n\nFare')

# fare_0_5 = df.where(lambda row: row['Fare'] != None).where(lambda row: 0 < row['Fare'] <= 5)

# fare_5_10 = df.where(lambda row: row['Fare'] != None).where(lambda row: 5 < row['Fare'] <= 10)

# fare_10_20 = df.where(lambda row: row['Fare'] != None).where(lambda row: 10 < row['Fare'] <= 20)

# fare_20_50 = df.where(lambda row: row['Fare'] != None).where(lambda row: 20 < row['Fare'] <= 50)

# fare_50_100 = df.where(lambda row: row['Fare'] != None).where(lambda row: 50 < row['Fare'] <= 100)

# fare_100_200 = df.where(lambda row: row['Fare'] != None).where(lambda row: 100 < row['Fare'] <= 200)

# fare_200_ = df.where(lambda row: row['Fare'] != None).where(lambda row: 200 < row['Fare'])



# fares = [fare_0_5, fare_5_10, fare_10_20, fare_20_50, fare_50_100, fare_100_200, fare_200_]

# fare_names = ['fare_0_5', 'fare_5_10', 'fare_10_20', 'fare_20_50', 'fare_50_100', 'fare_100_200', 'fare_200_']

# for fare_group in fares:
#   fare_selected = fare_group.select(["Survived"]).to_array()
#   total = 0
#   for data_point in fare_selected:
#     total += data_point[0]

#   avg = total/len(fare_selected)
#   print(fare_names[fares.index(fare_group)] + '\n', 'average:', round(avg, 2), '\n', 'count:', len(fare_selected), '\n')


# changing male and female to 0 and 1
sexes = df.data_dict['Sex']
for sex_index in range(len(df.data_dict['Sex'])):
  if sexes[sex_index] == 'male':
    df.data_dict['Sex'][sex_index] = 0
  elif sexes[sex_index] == 'female':
    df.data_dict['Sex'][sex_index] = 1

#removing None from age
for age_index in range(len(df.data_dict['Age'])):
  if df.data_dict['Age'][age_index] is None:
    df.data_dict['Age'][age_index] = 29.699

df = DataFrame(df.data_dict, df.columns)

#SibSp
df.data_dict['SibSp=0'] = []
for num_index in range(len(df.data_dict['SibSp'])):
  if df.data_dict['SibSp'][num_index] == 0:
    df.data_dict['SibSp=0'].append(1)
  else:
    df.data_dict['SibSp=0'].append(0)

#Parch
df.data_dict['Parch=0'] = []
for num_index in range(len(df.data_dict['Parch'])):
  if df.data_dict['Parch'][num_index] == 0:
    df.data_dict['Parch=0'].append(1)
  else:
    df.data_dict['Parch=0'].append(0)

#cabin types
for cabin_index in range(len(df.data_dict['CabinType'])):
  df.data_dict['CabinType'][cabin_index] = [df.data_dict['CabinType'][cabin_index]]

df.create_dummy_variables('CabinType')

cabin_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', None]
for cabin in cabin_list:
  df.data_dict['CabinType=' + str(cabin)] = df.data_dict[cabin]
  del df.data_dict[cabin]


# Embarked
for embark_index in range(len(df.data_dict['Embarked'])):
  df.data_dict['Embarked'][embark_index] = [df.data_dict['Embarked'][embark_index]]

df.create_dummy_variables('Embarked')

embark_list = ['C', 'Q', 'S', None]
for embark in embark_list:
  df.data_dict['Embarked=' + str(embark)] = df.data_dict[embark]
  del df.data_dict[embark]

df.columns = []
for key in df.data_dict:
  df.columns.append(key)

df = DataFrame(df.data_dict, df.columns)




print('Sex')
train = DataFrame.from_array(df.to_array()[:500], df.columns)
test = DataFrame.from_array(df.to_array()[500:], df.columns)

selected_train = train.select(['Sex', 'Survived'])

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(selected_train, 'Survived')


#train
dict_list = []
for num in selected_train.data_dict['Sex']:
  dict_list.append({'Sex': num})

predictions = []
for dictionary in dict_list:
  predict = linear_regressor.predict(dictionary)
  if predict >= 0.5:
    predictions.append(1)
  else:
    predictions.append(0)

correct_predictions = 0
for prediction_index in range(len(predictions)):
  if predictions[prediction_index] == selected_train.data_dict['Survived'][prediction_index]:
    correct_predictions += 1

print('train accuracy', correct_predictions/len(predictions))

#test
selected_test = test.select(['Sex', 'Survived'])

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(selected_test, 'Survived')

dict_list = []
for num in selected_test.data_dict['Sex']:
  dict_list.append({'Sex': num})

predictions = []
for dictionary in dict_list:
  predict = linear_regressor.predict(dictionary)
  if predict >= 0.5:
    predictions.append(1)
  else:
    predictions.append(0)

correct_predictions = 0
for prediction_index in range(len(predictions)):
  if predictions[prediction_index] == selected_test.data_dict['Survived'][prediction_index]:
    correct_predictions += 1

print('test accuracy', correct_predictions/len(predictions))
print(linear_regressor.calculate_coefficients(), '\n')


print('Sex, Pclass')
train = DataFrame.from_array(df.to_array()[:500], df.columns)
test = DataFrame.from_array(df.to_array()[500:], df.columns)

selected_train = train.select(['Sex', 'Pclass', 'Survived'])

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(selected_train, 'Survived')


#train
dict_list = []
for column_index in range(len(selected_train.data_dict['Survived'])):
  temp_dict = {}
  for key in selected_train.data_dict:
    if key != 'Survived':
      temp_dict[key] = selected_train.data_dict[key][column_index]
  dict_list.append(temp_dict)

predictions = []
for dictionary in dict_list:
  predict = linear_regressor.predict(dictionary)
  if predict >= 0.5:
    predictions.append(1)
  else:
    predictions.append(0)

correct_predictions = 0
for prediction_index in range(len(predictions)):
  if predictions[prediction_index] == selected_train.data_dict['Survived'][prediction_index]:
    correct_predictions += 1

print('train accuracy', correct_predictions/len(predictions))

#test
selected_test = test.select(['Sex', 'Pclass', 'Survived'])

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(selected_test, 'Survived')

dict_list = []
for column_index in range(len(selected_test.data_dict['Survived'])):
  temp_dict = {}
  for key in selected_test.data_dict:
    if key != 'Survived':
      temp_dict[key] = selected_test.data_dict[key][column_index]
  dict_list.append(temp_dict)

predictions = []
for dictionary in dict_list:
  predict = linear_regressor.predict(dictionary)
  if predict >= 0.5:
    predictions.append(1)
  else:
    predictions.append(0)

correct_predictions = 0
for prediction_index in range(len(predictions)):
  if predictions[prediction_index] == selected_test.data_dict['Survived'][prediction_index]:
    correct_predictions += 1

print('test accuracy', correct_predictions/len(predictions))
print(linear_regressor.calculate_coefficients(), '\n')







print('Sex, Pclass, Fare, Age, SibSp, SibSp=0, Parch=0')
train = DataFrame.from_array(df.to_array()[:500], df.columns)
test = DataFrame.from_array(df.to_array()[500:], df.columns)

selected_train = train.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Survived'])

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(selected_train, 'Survived')


#train
dict_list = []
for column_index in range(len(selected_train.data_dict['Survived'])):
  temp_dict = {}
  for key in selected_train.data_dict:
    if key != 'Survived':
      temp_dict[key] = selected_train.data_dict[key][column_index]
  dict_list.append(temp_dict)

predictions = []
for dictionary in dict_list:
  predict = linear_regressor.predict(dictionary)
  if predict >= 0.5:
    predictions.append(1)
  else:
    predictions.append(0)

correct_predictions = 0
for prediction_index in range(len(predictions)):
  if predictions[prediction_index] == selected_train.data_dict['Survived'][prediction_index]:
    correct_predictions += 1

print('train accuracy', correct_predictions/len(predictions))

#test
selected_test = test.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Survived'])

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(selected_test, 'Survived')

dict_list = []
for column_index in range(len(selected_test.data_dict['Survived'])):
  temp_dict = {}
  for key in selected_test.data_dict:
    if key != 'Survived':
      temp_dict[key] = selected_test.data_dict[key][column_index]
  dict_list.append(temp_dict)

predictions = []
for dictionary in dict_list:
  predict = linear_regressor.predict(dictionary)
  if predict >= 0.5:
    predictions.append(1)
  else:
    predictions.append(0)

correct_predictions = 0
for prediction_index in range(len(predictions)):
  if predictions[prediction_index] == selected_test.data_dict['Survived'][prediction_index]:
    correct_predictions += 1

print('test accuracy', correct_predictions/len(predictions))
print(linear_regressor.calculate_coefficients(), '\n')



print('Sex, Pclass, Fare, Age, SibSp, SibSp=0, Parch=0, Embarked=C, Embarked=None, Embarked=Q, Embarked=S')
train = DataFrame.from_array(df.to_array()[:500], df.columns)
test = DataFrame.from_array(df.to_array()[500:], df.columns)

selected_train = train.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'Survived'])

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(selected_train, 'Survived')


#train
dict_list = []
for column_index in range(len(selected_train.data_dict['Survived'])):
  temp_dict = {}
  for key in selected_train.data_dict:
    if key != 'Survived':
      temp_dict[key] = selected_train.data_dict[key][column_index]
  dict_list.append(temp_dict)

predictions = []
for dictionary in dict_list:
  predict = linear_regressor.predict(dictionary)
  if predict >= 0.5:
    predictions.append(1)
  else:
    predictions.append(0)

correct_predictions = 0
for prediction_index in range(len(predictions)):
  if predictions[prediction_index] == selected_train.data_dict['Survived'][prediction_index]:
    correct_predictions += 1

print('train accuracy', correct_predictions/len(predictions))

#test
selected_test = test.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'Survived'])

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(selected_test, 'Survived')

dict_list = []
for column_index in range(len(selected_test.data_dict['Survived'])):
  temp_dict = {}
  for key in selected_test.data_dict:
    if key != 'Survived':
      temp_dict[key] = selected_test.data_dict[key][column_index]
  dict_list.append(temp_dict)

predictions = []
for dictionary in dict_list:
  predict = linear_regressor.predict(dictionary)
  if predict >= 0.5:
    predictions.append(1)
  else:
    predictions.append(0)

correct_predictions = 0
for prediction_index in range(len(predictions)):
  if predictions[prediction_index] == selected_test.data_dict['Survived'][prediction_index]:
    correct_predictions += 1

print('test accuracy', correct_predictions/len(predictions))
print(linear_regressor.calculate_coefficients(), '\n')



print('Sex, Pclass, Fare, Age, SibSp, SibSp=0, Parch=0, Embarked=C, Embarked=None, Embarked=Q, Embarked=S, CabinType=A, CabinType=B, CabinType=C, CabinType=D, CabinType=E, CabinType=F, CabinType=G, CabinType=None')
train = DataFrame.from_array(df.to_array()[:500], df.columns)
test = DataFrame.from_array(df.to_array()[500:], df.columns)

selected_train = train.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'CabinType=A', 'CabinType=B', 'CabinType=C', 'CabinType=D', 'CabinType=E', 'CabinType=F', 'CabinType=G', 'CabinType=None', 'Survived'])


linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(selected_train, 'Survived')


#train
dict_list = []
for column_index in range(len(selected_train.data_dict['Survived'])):
  temp_dict = {}
  for key in selected_train.data_dict:
    if key != 'Survived':
      temp_dict[key] = selected_train.data_dict[key][column_index]
  dict_list.append(temp_dict)

predictions = []
for dictionary in dict_list:
  predict = linear_regressor.predict(dictionary)
  if predict >= 0.5:
    predictions.append(1)
  else:
    predictions.append(0)

correct_predictions = 0
for prediction_index in range(len(predictions)):
  if predictions[prediction_index] == selected_train.data_dict['Survived'][prediction_index]:
    correct_predictions += 1

print('train accuracy', correct_predictions/len(predictions))

#test
# selected_test = test.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'CabinType=A', 'CabinType=B', 'CabinType=C', 'CabinType=D', 'CabinType=E', 'CabinType=F', 'CabinType=G', 'CabinType=None', 'Survived'])

# linear_regressor = PolynomialRegressor(degree=1)
# linear_regressor.fit(selected_test, 'Survived')

# dict_list = []
# for column_index in range(len(selected_test.data_dict['Survived'])):
#   temp_dict = {}
#   for key in selected_test.data_dict:
#     if key != 'Survived':
#       temp_dict[key] = selected_test.data_dict[key][column_index]
#   dict_list.append(temp_dict)

# predictions = []
# for dictionary in dict_list:
#   predict = linear_regressor.predict(dictionary)
#   if predict >= 0.5:
#     predictions.append(1)
#   else:
#     predictions.append(0)

# correct_predictions = 0
# for prediction_index in range(len(predictions)):
#   if predictions[prediction_index] == selected_test.data_dict['Survived'][prediction_index]:
#     correct_predictions += 1

# print('test accuracy', correct_predictions/len(predictions))
print(linear_regressor.calculate_coefficients(), '\n')




print('Sex, Pclass, Fare, Age, SibSp, SibSp=0, Parch=0, Embarked=C, Embarked=None, Embarked=Q, Embarked=S, CabinType=A, CabinType=B, CabinType=C, CabinType=D, CabinType=E, CabinType=F, CabinType=G, CabinType=None, CabinType=T')
train = DataFrame.from_array(df.to_array()[:500], df.columns)
test = DataFrame.from_array(df.to_array()[500:], df.columns)

selected_train = train.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'CabinType=A', 'CabinType=B', 'CabinType=C', 'CabinType=D', 'CabinType=E', 'CabinType=F', 'CabinType=G', 'CabinType=None', 'CabinType=T', 'Survived'])


linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(selected_train, 'Survived')


#train
dict_list = []
for column_index in range(len(selected_train.data_dict['Survived'])):
  temp_dict = {}
  for key in selected_train.data_dict:
    if key != 'Survived':
      temp_dict[key] = selected_train.data_dict[key][column_index]
  dict_list.append(temp_dict)

predictions = []
for dictionary in dict_list:
  predict = linear_regressor.predict(dictionary)
  if predict >= 0.5:
    predictions.append(1)
  else:
    predictions.append(0)

correct_predictions = 0
for prediction_index in range(len(predictions)):
  if predictions[prediction_index] == selected_train.data_dict['Survived'][prediction_index]:
    correct_predictions += 1

print('train accuracy', correct_predictions/len(predictions))

#test
# selected_test = test.select(['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp=0', 'Parch=0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'CabinType=A', 'CabinType=B', 'CabinType=C', 'CabinType=D', 'CabinType=E', 'CabinType=F', 'CabinType=G', 'CabinType=None', 'CabinType=T', 'Survived'])

# linear_regressor = PolynomialRegressor(degree=1)
# linear_regressor.fit(selected_test, 'Survived')

# dict_list = []
# for column_index in range(len(selected_test.data_dict['Survived'])):
#   temp_dict = {}
#   for key in selected_test.data_dict:
#     if key != 'Survived':
#       temp_dict[key] = selected_test.data_dict[key][column_index]
#   dict_list.append(temp_dict)

# predictions = []
# for dictionary in dict_list:
#   predict = linear_regressor.predict(dictionary)
#   if predict >= 0.5:
#     predictions.append(1)
#   else:
#     predictions.append(0)

# correct_predictions = 0
# for prediction_index in range(len(predictions)):
#   if predictions[prediction_index] == selected_test.data_dict['Survived'][prediction_index]:
#     correct_predictions += 1

# print('test accuracy', correct_predictions/len(predictions))
print(linear_regressor.calculate_coefficients(), '\n')