# CPP_05 Project – Measurement Data Analyzer

During the second 45-minute block, you will keep developing one program:

`P05_measurement_data.cpp`

The starter program contains six measurement values:

```text
18, 24, 11, 29, 21, 17
```

The goal is not to let `main()` perform every calculation. We will split the program into
smaller, named functions. Before each new section, Inno shows a short analogous sample
using different variable names, then you apply the same idea to the project.

## P1 – Print the data

Create a `void` function that receives the address of the first element of the measurement
array and the number of elements, then uses a loop to print all measurements.

Within the project, use the prototype → call → definition structure.

## P2 – Sum

Create a function that traverses the array and returns the sum of the measurement values.
`main()` should only call the function and print the returned result.

## P3 – Average

Create a function returning `double` that calculates the average. Do not copy the summing
loop again: the average function should use the sum function that you created in P2.
Make sure division does not lose the fractional part.

## P4 – Maximum

Create a function that returns the largest measurement value. You may assume the array is
not empty.

## P5 – Count values above a threshold

Create a function with three parameters: measurement data, number of elements, and a
threshold. The function should return how many measurements are **strictly greater** than
the threshold.

First use the initial value `20` stored in `alertThreshold`.

## P6 – Reuse your earlier pointer knowledge

Create a `void` function that receives the address of an integer variable and increases the
stored value by 1. Call it with the address of `alertThreshold`. Then call your P5 function
again with the new threshold value.

## P7 – `<cmath>` in the project

Create a `distance` function with two `double` parameters. It should calculate the Euclidean
distance from the origin:

```text
sqrt(x*x + y*y)
```

Use the `sqrt` function from the `<cmath>` library. The starting coordinates are `3.0` and
`4.0`.

## Expected check values

When every section is complete, you can check your program with these results:

- sum: `120`
- average: `20`
- maximum: `29`
- number of measurements greater than 20: `3`
- threshold after increment: `21`
- number of measurements greater than 21: `2`
- distance of the measurement station from the origin: `5`

Your exact output formatting may differ; the calculated values must match.
