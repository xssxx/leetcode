// 2025.03.19

func containsDuplicate(nums []int) bool {
	m := make(map[int]struct{})

	for _, num := range nums {
		if _, exists := m[num]; exists {
			return true
		}

		m[num] = struct{}{}
	}

	return false
}