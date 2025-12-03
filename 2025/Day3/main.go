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
	for _, line := range input {
		slots := parse_bank(line)
		first_slot := slots[0]
		second_slot := slots[1]
		for i := 1; i < len(slots)-1; i++ {
			if slots[i] > first_slot {
				first_slot = slots[i]
				second_slot = slots[i+1]
			} else if slots[i] > second_slot {
				second_slot = slots[i]
			}
		}
		if slots[len(slots)-1] > second_slot {
			second_slot = slots[len(slots)-1]
		}
		running_sum += first_slot*10 + second_slot
	}
	fmt.Println(running_sum)
}

func part2(input []string) {
	fmt.Println("Part 2")
}

func parse_bank(bank_str string) []int {
	slots := make([]int, len(bank_str))
	for i := 0; i < len(bank_str); i++ {
		value_int, err := strconv.Atoi(string(bank_str[i]))
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error converting bank_str[i] to int: %v\n", err)
			os.Exit(1)
		}
		slots[i] = value_int
	}
	return slots
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
