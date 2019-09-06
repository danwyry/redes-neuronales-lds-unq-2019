class EightSquare:
    def __init__(self, strategy):
        self._graph = dict()
        self._strategy = strategy

    def __getitem__(self, item):
        key = str(item)
        if key not in self._graph.keys():
            self._graph[key] = self._strategy.neighbours(item)
        return self._graph[key]

    def sum_manhattan_distances(self):
        return self._strategy.sum_manhattan_distances

    def num_wrong_numbers(self):
        return self._strategy.num_wrong_numbers

class ESStrategy:
    @staticmethod
    def sum_manhattan_distances(node):
        raise Exception("not implemented")

    @staticmethod
    def num_wrong_numbers(node):
        raise Exception("not implemented")

    @staticmethod
    def neighbours(node):
        raise Exception("not implemented")

class LinearESStrategy(ESStrategy):
    MOVES = {
        #              move, is_valid_move
        'UP':    (lambda u: u-3, lambda pos: pos-3 >= 0),                               # UP
        'RIGHT': (lambda r: r+1, lambda pos: pos+1 != 3 and pos+1 != 6 and pos+1 != 9), # RIGHT
        'DOWN':  (lambda d: d+3, lambda pos: pos+3 <= 8),                               # DOWN
        'LEFT':  (lambda l: l-1, lambda pos: pos-1 != 2 and pos-1 != 5 and pos-1 != -1) # LEFT
    }

    @classmethod
    def sum_manhattan_distances(cls,node):
        s = 0
        for i in range(9):
            s += cls._manhattan_distance(node,i)
        return s

class ArrayStrategy(LinearESStrategy):
    @staticmethod
    def neighbours(node):
        pos = node.index(0)
        moves = dict()
        for label in ArrayStrategy.MOVES:
            move,is_valid_move = ArrayStrategy.MOVES[label]
            if is_valid_move(pos):
                new_pos = move(pos)
                a = node[new_pos]
                new_node = node[:]
                new_node[new_pos] = 0
                new_node[pos] = a
                moves[label] = new_node
        return moves

    @staticmethod
    def num_wrong_numbers(node):
        i = 0
        s = 0
        while i < 9:
            c = node[i]
            s += 1 \
                if c== 0 and c != 8 or c > 0 and c != i + 1 \
                else 0
            i += 1
        return s

    @staticmethod
    def _manhattan_distance(node, i):
        p = node.index(i)
        p = p+1 if p < 8 else 0
        i = int(i)
        return abs(StringStrategy._col(i) - StringStrategy._col(p)) + abs(StringStrategy._row(i) - StringStrategy._row(p))

class StringStrategy(LinearESStrategy):
    @staticmethod
    def neighbours(node):
        moves = dict()
        pos = int(node[9])
        for label in StringStrategy.MOVES:
            move,is_valid_move = StringStrategy.MOVES[label]
            if is_valid_move(pos):
                new_pos = move(pos)
                a=node[new_pos]
                pos1 = new_pos if new_pos < pos else pos
                pos2 = new_pos if new_pos > pos else pos
                e1 = '0' if new_pos < pos else a
                e2 = '0' if new_pos > pos else a
                new_node = node[0:pos1] + e1 + \
                           node[pos1+1:pos2] + e2  + \
                           node[pos2+1:9] +\
                           str(new_pos)
                moves[label] = new_node
        return moves

    @staticmethod
    def is_goal(node):
        return node == "1234567808"

    @staticmethod
    def num_wrong_numbers(node):
        i = 0
        s = 0 if node[9]=='8' else 1
        while i < 9:
            c = int(node[i])
            s += 1 \
                if c > 0 and c != i + 1 \
                else 0
            i += 1
        return s

    @staticmethod
    def _manhattan_distance(node, i):
        p = node.index(str(i))
        p = p+1 if p < 8 else 0
        i = int(i)
        return abs(StringStrategy._col(i) - StringStrategy._col(p)) + abs(StringStrategy._row(i) - StringStrategy._row(p))

    @staticmethod
    def _col(x):
        return 2 if x == 0 else (x - 1) % 3

    @staticmethod
    def _row(x):
        return 0 if x > 0 and x <= 3 else 1 if x > 3 and x <= 6 else 2

    @staticmethod
    def print_node(node):
        for j in range(3):
            line = ""
            for i in range(3 * j, 3 * j + 3):
                line = line + str(node[i]) + ","
            print("  " + line)
