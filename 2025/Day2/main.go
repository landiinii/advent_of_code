package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	input := readInput("input.txt")

	part1(input)
	// part2(input)
}

func part1(input []string) {
	fmt.Println("Part 1")

	running_sum := 0

	for _, id_range := range input {
		start, end := get_id_range(id_range)
		for i := start; i <= end; i++ {
			str_num := fmt.Sprintf("%d", i)
			if len(str_num)%2 != 0 {
				continue
			}
			mid := len(str_num) / 2
			left := str_num[:mid]
			right := str_num[mid:]
			if left == right {
				running_sum += i
			}
		}
	}
	fmt.Println(running_sum)
}

func part2(input []string) {
	fmt.Println("Part 2")
}

func get_id_range(id_range string) (int, int) {
	parts := strings.Split(id_range, "-")
	start, err := strconv.Atoi(parts[0])
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error converting start to int: %v\n", err)
		os.Exit(1)
	}
	end, err := strconv.Atoi(parts[1])
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error converting end to int: %v\n", err)
		os.Exit(1)
	}
	return start, end
}

func readInput(filename string) []string {
	inputBytes, err := os.ReadFile(filename)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error reading input.txt: %v\n", err)
		os.Exit(1)
	}
	input := strings.Split(string(inputBytes), ",")
	if len(input) == 0 {
		fmt.Fprintf(os.Stderr, "Input file is empty\n")
		os.Exit(1)
	}
	return input
}
