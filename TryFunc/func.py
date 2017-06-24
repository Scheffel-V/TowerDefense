empty = []

def first(list ):
    return list[0]


def rest(list):
	return list[1:]


def is_empty(list):
	if len(list) == 0:
		return True
	else:
		return False


def cons(element,list):
	if (element != empty):
		return [element]+list
	else:
		return []