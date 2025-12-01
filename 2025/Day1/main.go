package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	input := readInput("input.txt")

	part1(input)
	part2(input)
}

func part1(input []string) {
	fmt.Println("Part 1")
	start := 50
	zeros := 0

	for _, line := range input {
		if start == 0 {
			zeros += 1
		}

		step := get_step(line) % 100

		new_position := start + step
		if new_position < 0 {
			new_position = 100 + new_position
		} else if new_position > 99 {
			new_position = new_position - 100
		}

		start = new_position
	}
	fmt.Println(zeros)
}

func part2(input []string) {
	fmt.Println("Part 2")
	start := 50
	zeros := 0

	for _, line := range input {

		step := get_step(line)

		zeros += int(math.Floor(math.Abs(float64(step) / 100)))

		new_position := start + (step % 100)
		if new_position < 0 {
			new_position = 100 + new_position
			if start != 0 {
				zeros += 1
			}
		} else if new_position > 99 {
			new_position = new_position - 100
			zeros += 1
		} else if new_position == 0 {
			zeros += 1
		}

		start = new_position
	}
	fmt.Println(zeros)
}

func get_step(line string) int {
	direction := line[0]
	distance, err := strconv.Atoi(line[1:])
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error converting distance to int: %v\n", err)
		os.Exit(1)
	}
	if direction == 'L' {
		return -distance
	} else {
		return distance
	}
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
