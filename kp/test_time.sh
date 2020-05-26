

g++ gen.c -o gen
g++ -fopenmp -o omp qr_omp.cc -lm
g++ ./qr_simple.cc -o simple
## Generating file with size of matrix 20 and save it in file named "input"

rm test_omp
rm test_simple

for ((i = 5 ; i < 1000 ; i+=50)); do
  echo size $i
  echo generate matrix
  ./gen $i > input
  echo omp
  ./omp -n 4 -file input -silent >> test_omp
  echo simple
  ./simple -file input -silent >> test_simple

done


### Few example how to call program
## Print matrix & solution & time
# ./omp -n 4 -file input

## Print time only - for benchmark purposes
#./omp -n 4 -file input -silent

## Delete files
rm gen input omp simple
