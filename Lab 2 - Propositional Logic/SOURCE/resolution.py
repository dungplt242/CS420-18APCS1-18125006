from process import *


def pl_resolution(a, kb, output_stream):
    kb.extend(negate(a))
    found_empty_clause = False
    while True:
        new = []
        for ci in kb:
            for cj in kb:
                resolvent = resolve(ci, cj)
                if resolvent == None:
                    continue
                if resolvent not in new and resolvent not in kb:
                    new.append(resolvent)
                if is_empty_clause(resolvent):
                    found_empty_clause = True
        write_iteration(new, output_stream)
        if len(new) == 0:
            return False
        if found_empty_clause:
            return True
        kb.extend(new)
