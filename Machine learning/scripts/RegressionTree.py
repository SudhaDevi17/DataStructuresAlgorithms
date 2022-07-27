class TreeNode:
    def __init__(self, examples):
        self.examples = examples
        self.left = None
        self.right = None
        self.split_point = None

        def split(self):

            if len(self.examples)==1:
                return

            best_split = {
            "feature" : None,
            "value" : None,
            "mse" : float("inf"),
            "split_index": None,
            }

            for feature, _ in enumerate(self.examples[0]):

                if feature =="bpd":
                    continue
                self.examples.sort( key = lambda example : self.examples[feature])

                for i in range(len(self.examples[:-1])):
                    split_value =( self.examples[feature][i] + self.examples[feature][i+1])/2
                    mse , split_index = self.get_best_split_mse(self.examples, split_value)
                    if mse< best_split['mse']:
                        best_split = {
                            "feature" : feature,
                            "value" : split_value,
                            "mse" : mse,
                            "split_index": split_index,
                        }
            self.split_point = best_split
            # Recursion with sample subsets below and above the split values

            self.examples.sort(key = lambda example : example[self.split_point["feature"]])
            self.left = TreeNode(self.examples[:self.split_point["split_index"]])
            self.left.split()
            self.right = TreeNode(self.examples[self.examples[self.split_point["split_index"]:]])
            self.right.split()

        def get_best_split_mse(self, feature, split_value ):
            """
            :param self:
            :param feature: feature name
            :param split_value: the given split value
            :return: weighted average of left split lables and right split labels s
            """
            left_split_labels = [example for example in self.examples[feature]<split_value]
            right_split_labels = [example for example in self.examples[feature]> split_value]
            len_samples = len(left_split_labels) + len(right_split_labels)

            if not len(left_split_labels) or not len(right_split_labels):
                return None , None

            left_mse = self.get_mse(left_split_labels)
            right_mse = self.get_mse(right_split_labels)

            mse = (len(left_split_labels)*left_mse + len(right_split_labels)*right_mse)/len_samples
            split_index = len(left_split_labels)

            return mse , split_index


        def get_mse(self, values ):

            avg = self.average(values )
            mse = [(value - avg)**2 for value in values]
            return mse

        def get_average(self, values ):
            nums = len(values)
            return sum([value for value in values])/nums

class RegressionTree:

    def __init__(self, examples):
        self.root = TreeNode(examples)
        self.train()

    def train(self):
        self.root.split()

    def predict(self, example):

        node= self.root

        while node.left and node.right :
            # get the labels leaf from best splits
            if example[self.node.split_point["feature"] < self.node.split_point["value"]]:
                node = node.left
            else:
                node = node.right
            leaf_labels = [leaf_examples["bpd"] for leaf_examples in node.examples]
        return sum(leaf_labels)/len(leaf_labels)

