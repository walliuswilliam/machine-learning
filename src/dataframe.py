import sys
sys.path.append('src')
from matrix import Matrix

class DataFrame:
  def __init__(self, data_dict, column_order):
    self.data_dict = data_dict
    self.columns = column_order
  
  def to_array(self): 
    arr_transpose = []

    for variable_name in self.columns:
      arr_transpose.append(self.data_dict[variable_name])
      
    arr_matrix = Matrix(arr_transpose)
    arr_mat_transpose = arr_matrix.transpose()
    return arr_mat_transpose.elements

  def select(self, columns):
    dictionary = self.data_dict
    temp_dict = {key:dictionary[key] for key in columns}
    return DataFrame(temp_dict, columns)

  def select_rows(self, rows):
    final_dict = self.data_dict
    for key in final_dict:
      final_dict[key] = [self.data_dict[key][num] for num in rows]
    return DataFrame(final_dict, self.columns)

  def apply(self, key, funct):
    final_dict = self.data_dict
    prev_list = self.data_dict[key]
    final_dict[key] = [funct(num) for num in prev_list]
    return DataFrame(final_dict, self.columns)

  def create_interaction_terms(self, col_1, col_2):
    df_array = self.to_array()
    selected_columns = self.select_columns([col_1, col_2])
    column_array = selected_columns.to_array()

    for row in range(len(column_array)):
      product = column_array[row][0]*column_array[row][1]
      df_array[row].append(product)

    column_list = self.columns+[str(col_1+' * '+col_2)]
    return DataFrame.from_array(df_array, column_list)

  def create_dummy_variables(self, variable):
    dummy_variables = []
    for variable_list in self.data_dict[variable]:
      for var in variable_list:
        if var not in dummy_variables:
          dummy_variables.append(var)

    for dummy_variable in dummy_variables:
      dummy_values = [(1 if dummy_variable in dummy_list else 0) for dummy_list in self.data_dict[variable]]
      self.data_dict[dummy_variable] = dummy_values

    variable_index = self.columns.index(variable)
    for dum_variable in reversed(dummy_variables):
      self.columns.insert(variable_index, dum_variable)
    self.columns.remove(variable)
    
    del self.data_dict[variable]
    return DataFrame(self.data_dict, self.columns)
 
  def copy(self):
    return DataFrame(self.data_dict.copy(), self.columns.copy())

  @classmethod
  def from_array(cls, arr, columns):
    data_dict = {columns[key]:[arr[i][key] for i in range(len(arr))] for key in range(len(columns))}
    return cls(data_dict, columns)

  def convert_row_from_array_to_dict(self, row):
    row_to_dict = {self.columns[index]:row[index] for index in range(len(row))}
    return row_to_dict
  
  def where(self, funct):
    dict_rows = {self.columns[i]:[] for i in range(len(self.columns))}
    rows = [self.convert_row_from_array_to_dict(row_index) for row_index in self.to_array()]
    
    for row in rows:
      if funct(row):
        for key, value in row.items():
          dict_rows[key].append(value)
    return DataFrame(dict_rows, self.columns)

  def order_by(self, column, ascending=True):
    df_array = self.to_array()
    column_index = self.columns.index(column)
    df_array.sort(key = lambda x: x[column_index], reverse= not ascending)
    return DataFrame.from_array(df_array, self.columns)

  def group_by(self, column):
    unique_elements = []
    final_list = []
    df_array = self.to_array()
    column_index = self.columns.index(column)

    for row in df_array:
      if row[column_index] not in unique_elements:
        unique_elements.append(row[column_index])

    for element in unique_elements:
      instances = []
      grouped_list = [[] for column in self.columns]
      for row in df_array:
        if row[column_index] == element:
          instances.append(df_array.index(row))
      for instance in instances:
        row = df_array[instance]
        count = 0
        for entry in row:
          grouped_list[count].append(entry)
          count += 1
      grouped_list[column_index] = element
      final_list.append(grouped_list)
      
    return DataFrame.from_array(final_list, self.columns)
      

  def aggregate(self, col_name, how):
    arr = self.to_array()
    col_index = self.columns.index(col_name)

    if how == 'count':
      for row in arr:
        for entry_index in range(len(row)):
          if entry_index == col_index:
            row[col_index] = len(row[col_index])
      return DataFrame.from_array(arr, self.columns)

    elif how == 'max':
      for row in arr:
        for entry_index in range(len(row)):
          if entry_index == col_index:
            row[col_index] = max(row[col_index])
      return DataFrame.from_array(arr, self.columns)

    elif how == 'min':
      for row in arr:
        for entry_index in range(len(row)):
          if entry_index == col_index:
            row[col_index] = min(row[col_index])
      return DataFrame.from_array(arr, self.columns)

    elif how == 'sum':
      for row in arr:
        for entry_index in range(len(row)):
          if entry_index == col_index:
            row[col_index] = sum(row[col_index])
      return DataFrame.from_array(arr, self.columns)

    elif how == 'avg':
      for row in arr:
        for entry_index in range(len(row)):
          if entry_index == col_index:
            row[col_index] = sum(row[col_index])/len(row[col_index])
      return DataFrame.from_array(arr, self.columns)
    
  def query(self, string):
    string = string.replace('ORDER BY', 'ORDER_BY')
    string = string.replace('GROUP BY', 'GROUP_BY')
    string = string.split()

    operations = ['SELECT', 'WHERE', 'ORDER_BY', 'GROUP_BY']
    operation_queries = []

    temp_string = ''
    count = 0
    for word in string:
      if ((count == 0) or (word not in operations)):
        temp_string += word + ' '
        count += 1

      else:
        temp_string = temp_string[:-1]
        operation_queries.append(temp_string)
        temp_string = str(word) + ' '
        count = 0

    temp_string = temp_string[:-1]
    operation_queries.append(temp_string)

    keyword_to_function = {'SELECT': self.select, 'WHERE': self.where, 'ORDER_BY': self.order_by, 'GROUP_BY': self.group_by}


    final_df = None
    columns = None
    print(operation_queries)

    for query in operation_queries:
      query = query.split()
      
      stripped_list = []
      for input_query in query[1:]:
        stripped_list.append(input_query.strip(','))
      
      function_dict = {'operation': query[0], 'inputs': stripped_list}
      
      if function_dict['operation'] == 'ORDER_BY':
        temp_list = []
        for input_string in function_dict['inputs']:
          input_index = function_dict['inputs'].index(input_string)
          if input_index % 2 == 1:
            temp_list.append((function_dict['inputs'][input_index-1], input_string))
        
        function_dict['inputs'] = temp_list

        for argument in function_dict['inputs']:
          print(argument, argument[1])
          if argument[1] == 'DESC':
            final_df = keyword_to_function[function_dict['operation']](argument[0], ascending=False)
            print('desc')
          else:
            final_df = keyword_to_function[function_dict['operation']](argument[0])
            print('asc')
      elif function_dict['operation'] == 'SELECT':
        columns = function_dict['inputs']

        final_df = keyword_to_function[function_dict['operation']](function_dict['inputs'])

    return DataFrame(final_df.data_dict, columns)


  @classmethod
  def from_csv(cls, path_to_csv, data_types, parser=None, columns=None):
    with open(path_to_csv, "r") as file:
      lines = file.read().split('\n')
      if columns == None:
        columns = lines[0].split(',')
        lines = lines[1:]
      arr = []
      for line in lines:
        if len(line) > 0:
          str_entries = parser(line)
          entries = []
          for i, str_entry in enumerate(str_entries):
            col_name = columns[i]
            data_type = data_types[col_name]
            if str_entry != '':
              entry = data_type(str_entry)
            else:
              entry = None
            entries.append(entry)
          arr.append(entries)
    return cls.from_array(arr, columns)
  
