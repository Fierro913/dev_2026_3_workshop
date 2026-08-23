class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):

        lista_invertida = []

        for i in range(len(lista)-1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        pass
    
    def buscar_elemento(self, lista, elemento):

        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        pass
    
    def eliminar_duplicados(self, lista):
        lista_sin_duplicados = []
        
        for item in lista:
            if not any(x == item and type(x) is type(item) for x in lista_sin_duplicados):
                lista_sin_duplicados.append(item)
                
        return lista_sin_duplicados  
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        pass
    
    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i = 0  # Puntero para lista1
        j = 0  # Puntero para lista2
        
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
                
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        
        return resultado
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        pass
    
    def rotar_lista(self, lista, k):
        if not lista:
            return []
        k = k % len(lista)

        if k == 0:
            return lista[:]

        return lista[-k:] + lista[:-k]
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        pass
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_actual = sum(lista)
        return suma_esperada - suma_actual
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        pass
    
    def implementar_pila(self):
        elementos = []

        def is_empty():
            return len(elementos) == 0

        def push(elemento):
            elementos.append(elemento)

        def pop():
            if is_empty():
                return None
            return elementos.pop()

        def peek():
            if is_empty():
                return None
            return elementos[-1]

        return {"is_empty": is_empty, 
                "push": push, 
                "pop": pop, 
                "peek": peek}
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        elementos = []

        def is_empty():
            return len(elementos) == 0

        def enqueue(elemento):
            elementos.append(elemento)

        def dequeue():
            if is_empty():
                return None
            return elementos.pop(0)

        def peek():
            if is_empty():
                return None
            return elementos[0]

        return {"is_empty": is_empty, 
                "enqueue": enqueue, 
                "dequeue": dequeue, 
                "peek": peek}
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        if not matriz or not matriz[0]:
            return []

        filas = len(matriz)

        columnas = len(matriz[0])

        return [[matriz[j][i] for j in range(filas)] for i in range(columnas)]
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass