#!/bin/bash
echo -e "Reference benchmark using synchronous PyMongo"
python concurrent_throughput_benchmark/pymongo_throughput.py 1000

echo -e "\nReference benchmark using bit.ly's AsyncMongo"
python concurrent_throughput_benchmark/asyncmongo_throughput.py 1000

echo -e "\nMotor benchmark"
python concurrent_throughput_benchmark/asyncmongo_throughput.py 1000
