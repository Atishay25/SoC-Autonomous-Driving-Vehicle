#!/bin/bash

python3 encoder.py --grid data/maze/grid10.txt > mdp10.txt
python3 planner.py --mdp mdp10.txt --algorithm vi > value_and_policy_file
#python3 decoder.py --grid data/maze/grid10.txt --value_policy value_and_policy_file