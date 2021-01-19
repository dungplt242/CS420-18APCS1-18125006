from process import *


def test_output(clause):
    string = ""
    for variable in ascii_uppercase:
        if clause[variable] == 1:
            string += str(variable) + " "
        elif clause[variable] == -1:
            string += "-"+str(variable)+" "
    print(string)


def remove_old_clause(kb, variable):
    new = []
    for clause in kb:
        if clause[variable] == 0:
            new.append(clause)
    return new


def find_vocabulary(kb):
    vocab = []
    for variable in ascii_uppercase:
        for clause in kb:
            if clause[variable] != 0:
                vocab.append(variable)
                break
    return vocab


def david_putnam(a, kb, output_stream):
    kb.extend(negate(a))
    vocabulary = find_vocabulary(kb)
    found_empty_clause = False
    for variable in vocabulary:
        new = []
        for c1 in kb:
            for c2 in kb:
                if c1[variable]*c2[variable] == -1:
                    resolvent = resolve(c1, c2)
                    if resolvent != None and resolvent not in new and resolvent not in kb:
                        new.append(resolvent)
                        if is_empty_clause(resolvent):
                            found_empty_clause = True
        if len(new) > 0:
            kb = remove_old_clause(kb, variable)
            kb.extend(new)
        write_iteration(kb, output_stream)
        if found_empty_clause:
            return True
    return False


