#!/usr/bin/env fish

function setup
  echo "  * Setting up tests"
  if test -f $argv/.envrc
    echo "    - Moving .envrc"
    mv $argv/.envrc{,.bak}
  end
  # echo "    - Overwriting shell.nix"
  cp -f shell.nix $argv/shell.nix

  # echo "    - Removing existing secret tests"
  if test (count $argv/secret_*_test.py) != 0
    rm -f $argv/secret_*_test.py &> /dev/null
  end
  # echo "    - Copying fresh secret tests"
  for t in tests/secret_*_test.py
    cp -f $t $argv/(basename $t)
  end
  rm -rf $argv'/test_results/'

  git rev-parse > info_commit.txt
end

function grade_test
  set -l test_file $argv[1]

  set -l hard_deadline '25'
  if set -q argv[2]
    set hard_deadline $argv[2]
  end

  set -l soft_deadline '20'
  if set -q argv[3]
      set soft_deadline $argv[3]
  end

  echo -n "      - Running $test_file ..."
  if timeout \
       --kill-after $hard_deadline \
       $soft_deadline \
       pytest \
         --verbose \
         "$test_file" &> "test_results/logs/$test_file.log"
    set_color green
    echo "  Passed :)"
    set_color normal
    touch "test_results/passed/$test_file"
    cp "test_results/logs/$test_file.log" "test_results/passed/"
    return 0
  else
    set_color red
    echo "  Failed :("
    set_color normal
    touch "test_results/failed/$test_file"
    cp "test_results/logs/$test_file.log" "test_results/failed/"
    return 1
  end
end

function grade
  echo "  * Grading"

  if test -d test_results
    echo "    - Test result directory exists, not touching it..."
    return
  else
    mkdir test_results
    mkdir test_results/passed
    mkdir test_results/failed
    mkdir test_results/logs
  end

  echo "    - Running tests"
  for t in secret_*_test.py
    if grade_test $t
      echo "passed"
    else
      echo "failed"
    end
  end

  echo "    - Writing fake grade"
  touch grade.json
end


for assignment_directory in $argv
  echo "Grading $assignment_directory"
  setup $assignment_directory

  pushd $assignment_directory
  grade
  popd
  echo ""
end
