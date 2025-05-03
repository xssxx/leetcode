func strStr(n string, m string) int {
	ln := len(n)
	lm := len(m)

	for i := 0; i <= ln-lm; i++ {
		same := false
		if n[i] == m[0] {
			same = true
			for j := 0; j < lm; j++ {
				if n[i+j] != m[j] {
					same = false
					break
				}
			}
		}

		if same {
			return i
		}
	}

	return -1
}