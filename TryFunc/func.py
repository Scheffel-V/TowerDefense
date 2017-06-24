empty = []

def first(list ):
    return list[0]


def rest(list):
	rest_of_list = []
	for x in range(1,len(list)):
		rest_of_list.append(list[x])
	return rest_of_list

def is_empty(list):
	if len(list) == 0:
		return True
	else:
		return False
def cons(element,list):
	if(element != empty):
		aux_list = [element]
		return aux_list+list
	else:
		return []	