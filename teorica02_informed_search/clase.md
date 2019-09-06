# Clase 3
## Búsqueda Informada
### State explosion problem
#### From Arad to Bucharest

Estimación de la mejor solución


#### Greedy search

#### Algoritmo A*
Considera el costo acumulado hasta el nodo n desde el estado inicial (g(n)) más lo que estima la heurística (h(n)).

    f(n) = g(n) + h(n)
 
**ADmisibilidad**: una función heurística es admisible cuando nunca sobre-estima la distancia al objetivo
*Corolario*: si h(n) = INFINITO, entonces el objetivo  es inalcanzable

**Dominancia**:  una funcion heurística h2 domina a h1 si :
    
    h2(n) >= h1(n) ... para todo n

#### Cómo medimos la calidad de una heurística?

**Effective Branching Factor** (EBF)


Ejercicio: 
+ 8-Square Problem
+implementar dos funciones heurísticas
    + number of wrong numbers 
    + sum of manhattan distances (norma 1)
