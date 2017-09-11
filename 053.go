// Maximum Subarray

package main

import "fmt"

func main() {
	test := [2]int{-2, -1}
	fmt.Println(maxSubArray(test[:]))
}

func maxSubArray(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	checkSum, mxm := nums[0], nums[0]

	for i := 1; i < len(nums); i++ {
		current := 0
		if checkSum < 0 {
			current = nums[i]
		} else {
			current = nums[i] + checkSum
		}

		if current > mxm {
			mxm = current
		}
		checkSum = current
	}
	return mxm
}
