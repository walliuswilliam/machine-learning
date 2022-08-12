class NaiveBayes:
    def __init__(self, data):
        self.data = data
        self.data_len = sum([len(x) for x in data.values()])


    def calc_probability(self, var_idx, var_value, class_type):
        class_list = self.data[class_type]
        if var_idx is None and var_value is None:
            return len(class_list)/self.data_len
        else:
            count = 0
            for observation in class_list:
                if observation[var_idx] == var_value:
                    count += 1
            return count/len(class_list)

    def classify(self, input_list, class_list):
        predictions = []
        for observation in input_list:
            cls_1_val = self.calc_probability(None, None, class_list[0])*self.calc_probability(0, observation[0], class_list[0])*self.calc_probability(1, observation[1], class_list[0])
            cls_2_val = self.calc_probability(None, None, class_list[1])*self.calc_probability(0, observation[0], class_list[1])*self.calc_probability(1, observation[1], class_list[1])
            if cls_1_val > cls_2_val:
                predictions.append(class_list[0])
            else:
                predictions.append(class_list[1])
        return predictions




data = {'scam':[[1,1],[1,1],[1,1],[1,0]], 'no_scam':[[0,0],[0,0],[0,1],[1,0],[0,1],[0,1]]}

nb = NaiveBayes(data)
print(nb.classify([[0,0],[1,1],[1,0],[0,1]], ['scam', 'no_scam']))