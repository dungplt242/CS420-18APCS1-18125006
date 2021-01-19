from resolution import pl_resolution
from dp import david_putnam
from process import *


def read_query(input_stream):
    string = input_stream.readline()
    return string_convert(string)


def read_kb(input_stream):
    clauses = []
    n = int(input_stream.readline())
    for _ in range(n):
        string = input_stream.readline()
        clauses.append(string_convert(string))
    return clauses


def read_input():
    input_path = "input.txt"
    input_stream = open(input_path, "r")
    a = read_query(input_stream)
    kb = read_kb(input_stream)
    return a, kb


def output_resolution():
    a, kb = read_input()
    output_path = "outputR.txt"
    output_stream = open(output_path, "w")
    if pl_resolution(a, kb, output_stream):
        output_stream.write("YES")
    else:
        output_stream.write("NO")


def output_davis_putnam():
    a, kb = read_input()
    output_path = "outputDP.txt"
    output_stream = open(output_path, "w")
    if david_putnam(a, kb, output_stream):
        output_stream.write("YES")
    else:
        output_stream.write("NO")


if __name__ == '__main__':
    output_resolution()
    output_davis_putnam()