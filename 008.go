// String to Integer (atoi) ASCII to Integer

package main

const (
	// MAX is the restrictions of 32-bit signed integer of leetcode.
	MAX int = 1<<31 - 1
	// MIN is the restrictions of 32-bit signed integer of leetcode.
	MIN int = -MAX - 1
)

func myAtoi(str string) int {
	if len(str) == 0 {
		return 0
	}

	str_list := []rune(str)
	rtrn := 0
	sign := 1

	for i := 0; i < len(str); i++ {
		if str_list[i] == rune(' ') {
			// Do nothing
		} else if str_list[i] == rune('+') {
			sign = 1
		} else if str_list[i] == rune('-') {
			sign = -1
		} else {
			val, isInt := toInt(str_list[i])
			if !isInt {
				break
			} else {
				if rtrn > (MAX-val)/10 {
					return MAX
				} else if -rtrn < (MIN+val)/10 {
					return MIN
				}
				rtrn = 10*rtrn + val
			}
		}
	}

	return sign * rtrn
}

func toInt(r rune) (int, bool) {
	rtrn := int(r - rune('0'))
	if rtrn >= 0 && rtrn <= 9 {
		return rtrn, true
	}
	return 0, false
}
