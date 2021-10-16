#!/usr/bin/env python

import contextlib
import copy
import json
import os
import re
from collections import ChainMap
from decimal import Decimal
from pathlib import Path
from pprint import pprint


@contextlib.contextmanager
def pushd(new_dir):
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(previous_dir)


def file_to_string(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            return f.read()


SCORES = {
    # NM-Puzzle
    #   - [0.2] Implemente la heurística mencionada en clases de la suma de las
    #     distancias de Manhattan entre las losetas (/tiles/) y su posición final.
    "secret_nm_puzzle_h_public_test.py": Decimal("0.02"),
    "secret_nm_puzzle_h_h2_w3_reversed_test.py": Decimal("0.03"),
    "secret_nm_puzzle_h_h2_w3_static_test.py": Decimal("0.03"),
    "secret_nm_puzzle_h_h3_w4_start_test.py": Decimal("0.01"),
    "secret_nm_puzzle_h_random_3_3_test.py": Decimal("0.05"),
    "secret_nm_puzzle_h_random_3_4_test.py": Decimal("0.06"),
    # Sokoban
    #   - [0.2] Implemente esta heurística.
    "secret_sokoban_public_test.py": Decimal("0.05"),
    "secret_sokoban_h_manhattan_test.py": Decimal("0.15"),
    #   - [0.3] Notando que el agente tiene que acercarse a las cajas es fácil notar
    #     que falta contar acciones. Implemente esta versión mejorada de la
    #     heurística.
    "secret_sokoban_h_manhattan_walk_easy_test.py": Decimal("0.1"),
    "secret_sokoban_h_manhattan_walk_med_test.py": Decimal("0.2"),
    #   - [0.7] Implemente una heurística estrictamente mejor que las anteriores.
    "secret_sokoban_h_better_test.py": Decimal("0.7"),
    # ID-DFS
    #   - [0.3] Implemente ID-DFS y logre pasar los tests de optimalidad.
    "secret_iddfs_public_nosol_test.py": Decimal("0.1"),
    "secret_iddfs_public_test.py": Decimal("0.2"),
    # Alt
    "secret_iddfs_public_alt_nosol_test.py": Decimal("0.1"),
    "secret_iddfs_public_alt_test.py": Decimal("0.2"),
    # A*
    #   - [0.8] Implemente A*
    "secret_astar_public_test.py": Decimal("0.1"),
    "secret_astar_best_f_test.py": Decimal("0.5"),
    "secret_astar_search_test.py": Decimal("0.2"),
    #   - [0.2] Implemente desempates optimistas usando mayor $g$ o menor $h$.
    "secret_astar_tie_breaking_test.py": Decimal("0.1"),
    "secret_astar_search_tie_breaking_test.py": Decimal("0.1"),
}


def grade(github_user):
    passed_tests = sorted([p.name for p in Path("test_results/passed").rglob("*.py")])
    failed_tests = sorted([p.name for p in Path("test_results/failed").rglob("*.py")])

    # Python3.8 does not support Union (operator |)
    scores = {t: str(Decimal(0.0)) for t in failed_tests}
    for passed_test in passed_tests:
        scores[passed_test] = str(SCORES[passed_test])

    return {
        "github_user": github_user,
        "commit": file_to_string("info_commit.txt").strip(),
        "passed_tests": passed_tests,
        "failed_tests": failed_tests,
        "total_score": str(
            sum([SCORES[t] for t in passed_tests])
        ),  # `json` can't serialize Decimals...
        "scores": scores,
    }


REPO_PREFIX = "tarea-1-2021-2-"


def main(argv):
    # program_name = argv[0]
    args = argv[1:]

    full_report = {}
    for assignment_path in args:
        assignment_dir = os.path.basename(assignment_path)
        if not assignment_dir.startswith(REPO_PREFIX):
            print("Skipping ", assignment_path)
            continue

        github_user = assignment_dir[len(REPO_PREFIX) :]
        with pushd(assignment_path):
            report = grade(github_user)
            full_report[github_user] = report
            pprint(report)
            with open("report.json", "w") as json_file:
                json.dump(report, json_file)
                print("Wrote `report.json`")

    with open("full_report.json", "w") as json_file:
        json.dump(full_report, json_file)
        print("Wrote `full_report.json`")


if __name__ == "__main__":
    import sys

    main(sys.argv)
