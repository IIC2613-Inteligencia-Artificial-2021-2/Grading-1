{ pkgs ? import <nixpkgs> {} }:

let
  pyPkgs = pkgs.python38Packages;
in
  pyPkgs.buildPythonApplication {
    pname = "assignment-1";
    version = "0.0.0";

    src = pkgs.lib.cleanSource ./.;

    # Run environment
    propagatedBuildInputs = with pyPkgs; [
      numpy
      pygame_sdl2
      termcolor
    ];
    # Check
    checkInputs = with pyPkgs; [
      autopep8
      mypy
      pylint
      pytest

      # Tools that become available on the shell
      graphviz
      ipython
      importmagic
      epc
      # python-language-server
      black

      # Grading
      PyGithub
      pkgs.parallel
    ];
    checkPhase = ''
      autopep8 --aggressive --exit-code */.py **/.py
      pytest
      mypy ./main.py
    '';

    meta = {
      homepage = "https://github.com/IIC2613-Inteligencia-Artificial-2021-2/";
      license = pkgs.lib.licenses.bsd3;
      description = "A project for grading the 1st assignment.";
    };
  }
