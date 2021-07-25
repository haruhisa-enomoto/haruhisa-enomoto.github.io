"""
This program enables us to import the lattice of torsion classes in SageMath from
Jan Geuenich's String Applet:
https://www.math.uni-bielefeld.de/~jgeuenich/string-applet/
"""
# GitHub Repository:
# https://github.com/haruhisa-enomoto/StringApplet-to-SageMath-converter

import re

def SAtoSage(tex_path):
    r"""
    Return the data which can be used to construct the poset of torsion classes
    in SageMath from the tex file exported by StringApplet.

    INPUT:

      - ``tex_path`` -- a path of the exported tex file (str)

    OUTPUT:

      a tuple of the form (``tors``, ``rels``), where

      - ``tors`` -- a list of torsion classes, which are represented by
        integers 0,1,2, (a list of integers)

      - ``rels`` -- a list of covering relations, which are tuples
        of the form (U,T)

    """

    with open(tex_path, "r") as f:
        lines_lst = f.readlines()

    # Cut out the needed part
    begin_str = [line for line in lines_lst if "Tilting Quiver" in line][0]
    begin_idx = lines_lst.index(begin_str)
    end_str = [line for line in lines_lst if "Tilting Modules" in line][0]
    end_idx = lines_lst.index(end_str)
    needed_part = lines_lst[begin_idx:end_idx]

    # There are two `scope` environments in the needed part
    # inside the tikzpicture environment.
    # The first one is the set of vertices,
    # and the second one is the set of arrows.
    # scope_count = 1: the first one
    # scope_count = 2: the second one
    scope_count = 0
    tors = []
    rels = []
    for line in needed_part:
        if "begin{scope}" in line:
            scope_count = scope_count + 1
        if scope_count == 0:
            continue
        elif scope_count == 1:
            match = re.search(r'node \((.*)\) at', line)
            if match:
                vtx_name = match.group(1)
                tors.append(int(vtx_name))
        elif scope_count == 2:
            match = re.findall(r'\((.+?)\)', line)
            if match:
                small, large = int(match[1]), int(match[0])
                rels.append((small,large))

    return (tors,rels)

def export(tex_path, output_path):
    r"""
    Write data to a new file.

    The content of the created file is ``data = ...``,
    where ``...`` is a data from which we can construct a poset.

    INPUT:

      - tex_path -- a path of the exported tex file (str)

      - output_path -- a path of the output file
        (error will be raised if the file already exists)

    """

    data = SAtoSage(tex_path)
    with open(output_path, "x") as f:
        f.write('data = ' + str(data))
