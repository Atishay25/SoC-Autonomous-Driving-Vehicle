#!/bin/bash

if [[ $# -eq 0 ]] ; then
    echo 'Provide the grid file name as arguement'
    echo 'Example : ./run.sh grid20.txt'
    exit 0
fi

maze="data/maze/"$1
mdp_encoded="mdp"${maze: -6}

python3 encoder.py --grid ${maze} > ${mdp_encoded}
python3 planner.py --mdp ${mdp_encoded} --algorithm vi > value_and_policy_file
python3 decoder.py --grid ${maze} --value_policy value_and_policy_file
python3 visualize.py ${maze}