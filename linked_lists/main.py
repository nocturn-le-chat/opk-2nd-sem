class linked_list:
    pass

    try:
        # Конструктор
        def from_list(list):
            if type(list) != list: raise TypeError
            link = None
            for k in list[::-1]:
                node = linked_list()
                node.value, node.next = k, link
                link = node
            return node

        # Деконструкторы
        def to_list(l_list):
            if type(l_list) != linked_list: raise TypeError
            result = []
            while l_list != None:
                result.append(l_list.value)
                l_list = l_list.next
            return result
        
        def to_str(l_list):
            if type(l_list) != linked_list: raise TypeError
            result = ""
            while l_list.next != None:
                result += f"{l_list.value} -> "
                l_list = l_list.next
            result += f"{l_list.value}"
            return result
        
        # Параметры списка
        def length(l_list):
            if type(l_list) != linked_list: raise TypeError
            counter = 0
            while l_list.next != None:
                counter += 1
                l_list = l_list.next
            return counter
        
        # Операции над звеньями списка
        def prepend(data, l_list):
            if type(l_list) != linked_list or data == None: raise TypeError
            node = linked_list()
            node.value, node.next = data, l_list
            return node
        
        def append(data, l_list):
            if type(l_list) != linked_list or data == None: raise TypeError
            first_node = l_list
            while l_list.next != None:
                l_list = l_list.next
            node = linked_list()
            node.value, node.next = data, None
            l_list.next = node
            return first_node
        
        def copy(l_list):
            if type(l_list) != linked_list: raise TypeError
            return linked_list.from_list(linked_list.to_list(l_list))
        
        def concat (l_list1, l_list2):
            if type(l_list1) != linked_list or type(l_list2) != linked_list: raise TypeError
            first_node = l_list1
            while l_list1.next != None:
                l_list1 = l_list1.next
            l_list1.next = l_list2
            return first_node
        
        def remove(l_list, index):
            if [type(k) for k in [l_list, index]] == [linked_list, int]: raise TypeError
            first_node = l_list
            counter = 0
            while counter+1 != index:
                l_list = l_list.next
            val = l_list.next.value
            l_list.next = l_list.next.next if l_list.next.next != None else None
            return (val, first_node)
        
        def remove_all(data, l_list):
            if type(l_list) != linked_list or data == None: raise TypeError
            first_node = l_list
            while l_list.next != None:
                if l_list.next.value == data:
                    l_list.next = l_list.next.next if l_list.next.next != None else None
            return first_node
        
        # Операции над элементами
        def get(l_list, index):
            if [type(k) for k in [l_list, index]] == [linked_list, int]: raise TypeError
            counter = 0
            while counter != index:
                l_list = l_list.next
            return l_list.value
        
        def get_last(l_list):
            if type(l_list) != linked_list: raise TypeError
            while l_list.next != None:
                l_list = l_list.next
            return l_list.value
        
        def find(data, l_list):
            if type(l_list) != linked_list: raise TypeError
            if type(l_list) != linked_list or data == None: raise TypeError
            counter = 0
            while l_list.next != None:
                if l_list.value == data:
                    return counter
                else:
                    l_list = l_list.next
                    counter += 1
            return -1
        
        def find_custom(l_list, predicate):
            if [type(k) for k in [l_list, predicate]] == [linked_list, function]: raise TypeError
            counter = 0
            while l_list.next != None:
                if predicate(l_list.value):
                    return (l_list.value, counter)
                else:
                    l_list = l_list.next
                    counter += 1
            return (None, -1)
        
        def foreach(l_list, func):
            if [type(k) for k in [l_list, func]] == [linked_list, function]: raise TypeError
            maplist = []
            while l_list.next != None:
                maplist.append(func(l_list.value))
                l_list = l_list.next
            return linked_list.from_list(maplist)
    except TypeError: print("ERROR: unsupported input type")