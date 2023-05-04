#!/bin/bash

if [ -z "$1" ]
then
    echo "Error: Argument not provided"
    exit 1
fi


N=$1
if [ $N -lt 10 ]
then
    OUT=$((N*N))

# Original Statement: elif [ $N -lt 20 ]
elif [ $N -le 20 ]
then
    OUT=1
    LIM=$((N - 10))

# Original Statement: for (( i=1; i<$LIM; i++ ))
    for (( i=1; i<=$LIM; i++ ))
    do
            OUT=$((OUT * i))
    done
else
    LIM=$((N - 20))

# Original Statements: 
    # OUT=$((LIM * LIM))
    # OUT=$((OUT - LIM))
    # OUT=$((OUT / 2))
    OUT=0
    for (( i=1; i<=LIM; i++ ))
    do
            OUT=$((OUT + i))
    done
fi
echo $OUT