// Reverse Integer

package main

const (
	// MAX is the restrictions of 32-bit signed integer of leetcode.
	MAX int = 1<<31 - 1
	// MIN is the restrictions of 32-bit signed integer of leetcode.
	MIN int = -MAX - 1
)

func reverse(x int) int {
	temp := x
	val := 0
	sign := 1
	var list = []int{}
	if x < 0 {
		sign = -1
		temp = x * -1
	}

	for temp > 9 {
		list = append(list, int(temp%10))
		temp = temp / 10
	}

	list = append(list, int(temp))

	for i := 0; i < len(list); i++ {
		if val > (MAX-list[i])/10 || -val < (MIN+list[i])/10 {
			return 0
		}
		val = 10*val + list[i]
	}

	return sign * val
}
