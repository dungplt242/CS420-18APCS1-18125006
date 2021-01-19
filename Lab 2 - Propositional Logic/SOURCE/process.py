from string import ascii_uppercase


def string_convert(string):
    clause = new_clause()
    elements = string.split()
    for ele in elements:
        if ele == "OR":
            continue
        elif ele[0] == '-':
            clause[ele[1]] = -1
        else:
            clause[ele[0]] = 1
    return clause


def new_clause():
    return {variable: 0 for variable in ascii_uppercase}


def negate(source_clause):
    clauses = []
    for variable in ascii_uppercase:
        if source_clause[variable] != 0:
            new_split_clause = new_clause()
            new_split_clause[variable] = -source_clause[variable]
            clauses.append(new_split_clause)
    return clauses


def is_empty_clause(clause):
    for variable in ascii_uppercase:
        if clause[variable] != 0:
            return False
    return True


def clause_convert(clause):
    if is_empty_clause(clause):
        return "{}"
    string = ""
    for variable in ascii_uppercase:
        if clause[variable] == 0:
            continue
        elif clause[variable] == -1:
            string += "-"
        string += str(variable) + " OR "
    return string[:-4]


def clause_resolve(c1, c2):
    clause = new_clause()
    for variable in ascii_uppercase:
        if c1[variable] * c2[variable] == 1:
            clause[variable] = c1[variable]
        elif c1[variable] + c2[variable] != 0:
            clause[variable] = c1[variable] + c2[variable]
    return clause


def resolve(c1, c2):
    ready_resolve = False
    for variable in ascii_uppercase:
        if c1[variable]*c2[variable] == -1:
            if ready_resolve:
                return None
            else:
                ready_resolve = True
    if ready_resolve:
        return clause_resolve(c1, c2)
    return None


def write_iteration(clauses, output_stream):
    output_stream.write(str(len(clauses)) + '\n')
    for clause in clauses:
        output_stream.write(clause_convert(clause) + '\n')