from eight_square import EightSquare, StringStrategy, ArrayStrategy
from search_algorithms import gs
# Un nodo es un string de 10 caracteres donde el último caracter representa el índice de la posición donde se encuentra
# el 0, para ahorrar la búsqueda del 0 en todo el string en cada iteración.

print ("STRINGS --------")
initial = "8253104675"
StringStrategy.print_node(initial)
game = EightSquare(StringStrategy)
gs1 = gs(game, initial, game.num_wrong_numbers())
print(gs1)
gs2 = gs(game, initial, game.sum_manhattan_distances())
print(gs2)

# print ("ARRAYS --------")
# initial = [8,2,5,3,1,0,4,6,7]
# StringStrategy.print_node(initial)
# game = EightSquare(ArrayStrategy)
# print(gs(game,str(initial), game.num_wrong_numbers()))
# print(gs(game,str(initial), game.sum_manhattan_distances()))
