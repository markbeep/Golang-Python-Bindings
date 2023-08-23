package main

import "C"
import (
	"fmt"
	"math/rand"
)

//export collatz
func collatz(n int) int {
	if n%2 == 0 {
		return n / 2
	}
	return 3*n + 1
}

//export loopCollatz
func loopCollatz(n, k int) int {
	for i := 0; i < k; i++ {
		n = collatz(n)
	}
	return n
}

func main() {
	k := int(rand.Uint32()) + 1 // Random positive int
	for i := 0; i < 1_000_000_000; i++ {
		k = collatz(k)
	}
	fmt.Println(k)
}
