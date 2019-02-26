y_pred = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0]
y_true = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# 0 - cladire
# 1 - om

class Lab1:
    def __init__(self, y_pred, y_true):
        self.y_pred = y_pred
        self.y_true = y_true

    def accuracy_score(self, y_true, y_pred):
        if (len(y_true) != len(y_pred)):
            print("Lists have different lengths")
            return
            
        equals = 0
        for idx in range(len(y_pred)):
            equals += (y_true[idx] == y_pred[idx])
        
        return equals / len(y_true)
    
    def precision_recall_score(self, y_true, y_pred):
        if (len(y_true) != len(y_pred)):
            print("Lists have different lengths")
            return
        
        fp, fn, tp = 0, 0, 0

        for idx in range(len(y_pred)):
            if y_pred[idx] == 1 and y_true[idx] == 1:
                tp += 1
            elif y_pred[idx] == 1 and y_true[idx] == 0:
                fp += 1
            elif y_pred[idx] == 0 and y_true[idx] == 1:
                fn += 1
            
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)

        return precision, recall

l1 = Lab1(y_pred, y_true)
print(l1.accuracy_score(l1.y_true, l1.y_pred))

precision, recall = l1.precision_recall_score(l1.y_true, l1.y_pred)
print("%.2f, %.2f" % (precision, recall))