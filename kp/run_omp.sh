##!/usr/bin/env bash

## Compilation
g++ gen.c -o gen
 g++ -fopenmp -o omp qr_omp.cc -lm

## Generating file with size of matrix 20 and save it in file named "input"
./gen 5 > input

### Few example how to call program
## Print matrix & solution & time
./omp -n 4 -file input

## Print time only - for benchmark purposes
#./omp -n 4 -file input -silent

## Delete files
rm gen input omp
