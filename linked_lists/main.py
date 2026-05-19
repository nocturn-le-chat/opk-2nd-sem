class Linked_list:
    pass

    try:
        # Конструктор
        def from_list(List):
            if type(List) != list: raise TypeError
            link = None
            for k in list[::-1]:
                node = Linked_list()
                node.value, node.next = k, link
                link = node
            return node

        # Деконструкторы
        def to_list(linked_list):
            if type(linked_list) != Linked_list: raise TypeError
            result = []
            while linked_list != None:
                result.append(linked_list.value)
                linked_list = linked_list.next
            return result
        
        def to_str(linked_list):
            if type(linked_list) != Linked_list: raise TypeError
            result = ""
            while linked_list.next != None:
                result += f"{linked_list.value} -> "
                linked_list = linked_list.next
            result += f"{linked_list.value}"
            return result
        
        # Параметры списка
        def length(linked_list):
            if type(linked_list) != Linked_list: raise TypeError
            counter = 0
            while linked_list.next != None:
                counter += 1
                linked_list = linked_list.next
            return counter
        
        # Операции над звеньями списка
        def prepend(data, linked_list):
            if type(linked_list) != Linked_list or data == None: raise TypeError
            node = Linked_list()
            node.value, node.next = data, linked_list
            return node
        
        def append(data, linked_list):
            if type(linked_list) != Linked_list or data == None: raise TypeError
            first_node = linked_list
            while linked_list.next != None:
                linked_list = linked_list.next
            node = Linked_list()
            node.value, node.next = data, None
            linked_list.next = node
            return first_node
        
        def copy(linked_list):
            if type(linked_list) != Linked_list: raise TypeError
            return Linked_list.from_list(Linked_list.to_list(linked_list))
        
        def concat (l_list1, l_list2):
            if type(l_list1) != Linked_list or type(l_list2) != Linked_list: raise TypeError
            first_node = l_list1
            while l_list1.next != None:
                l_list1 = l_list1.next
            l_list1.next = l_list2
            return first_node
        
        def remove(linked_list, index):
            if [type(k) for k in [linked_list, index]] == [Linked_list, int]: raise TypeError
            first_node = linked_list
            counter = 0
            while counter+1 != index:
                linked_list = linked_list.next
            val = linked_list.next.value
            linked_list.next = linked_list.next.next if linked_list.next.next != None else None
            return (val, first_node)
        
        def remove_all(data, linked_list):
            if type(linked_list) != Linked_list or data == None: raise TypeError
            first_node = linked_list
            while linked_list.next != None:
                if linked_list.next.value == data:
                    linked_list.next = linked_list.next.next if linked_list.next.next != None else None
            return first_node
        
        # Операции над элементами
        def get(linked_list, index):
            if [type(k) for k in [linked_list, index]] == [Linked_list, int]: raise TypeError
            counter = 0
            while counter != index:
                linked_list = linked_list.next
            return linked_list.value
        
        def get_last(linked_list):
            if type(linked_list) != Linked_list: raise TypeError
            while linked_list.next != None:
                linked_list = linked_list.next
            return linked_list.value
        
        def find(data, linked_list):
            if type(linked_list) != Linked_list: raise TypeError
            if type(linked_list) != Linked_list or data == None: raise TypeError
            counter = 0
            while linked_list.next != None:
                if linked_list.value == data:
                    return counter
                else:
                    linked_list = linked_list.next
                    counter += 1
            return -1
        
        def find_custom(linked_list, predicate):
            if [type(k) for k in [linked_list, predicate]] == [Linked_list, function]: raise TypeError
            counter = 0
            while linked_list.next != None:
                if predicate(linked_list.value):
                    return (linked_list.value, counter)
                else:
                    linked_list = linked_list.next
                    counter += 1
            return (None, -1)
        
        def foreach(linked_list, func):
            if [type(k) for k in [linked_list, func]] == [Linked_list, function]: raise TypeError
            maplist = []
            while linked_list.next != None:
                maplist.append(func(linked_list.value))
                linked_list = linked_list.next
            return Linked_list.from_list(maplist)
    except TypeError: print("ERROR: unsupported input type")