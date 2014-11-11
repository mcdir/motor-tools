#!/bin/bash
echo -e "Reference benchmark using synchronous PyMongo"
python benchmark/pymongo_benchmark.py

echo -e "\nReference benchmark using bit.ly's AsyncMongo"
python benchmark/asyncmongo_benchmark.py

echo -e "\nMotor benchmark"
python benchmark/motor_benchmark.py

echo -e "\nMotor benchmark using Tornado's generator API"
python benchmark/motor_benchmark_gen.py