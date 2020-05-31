

g++ gen.c -o gen
g++ -fopenmp -o omp qr_omp.cc -lm
g++ ./qr_simple.cc -o simple
## Generating file with size of matrix 20 and save it in file named "input"


for ((j = 2 ; j < 20 ; j++)); do

  rm ./global_test/test_omp_$j
  rm ./global_test/test_simple_$j

done



for ((j = 2 ; j < 20 ; j++)); do

  for ((i = 5 ; i < 1000 ; i+=50)); do
    echo ___________________
    echo size $j $i

    echo generate matrix

    ./gen $i > input
    echo omp
    ./omp -n 7 -file input -silent >> ./global_test/test_omp_$j
    echo simple
    ./simple -file input -silent >> ./global_test/test_simple_$j

  done

done





### Few example how to call program
## Print matrix & solution & time
# ./omp -n 4 -file input

## Print time only - for benchmark purposes
#./omp -n 4 -file input -silent

## Delete files
rm gen input omp simple
