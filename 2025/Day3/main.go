package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	input := readInput("input.txt")

	part1(input)
	// part2(input)
}

func part1(input []string) {
	fmt.Println("Part 1")
}

func part2(input []string) {
	fmt.Println("Part 2")
}

func readInput(filename string) []string {
	inputBytes, err := os.ReadFile(filename)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error reading input.txt: %v\n", err)
		os.Exit(1)
	}
	input := strings.Split(string(inputBytes), "\n")
	if len(input) == 0 {
		fmt.Fprintf(os.Stderr, "Input file is empty\n")
		os.Exit(1)
	}
	return input
}
