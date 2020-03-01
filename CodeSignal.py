def almostIncreasingSequence(sequence):
	cnt = 0
	seq_len = len(sequence)
	for idx in range(1, seq_len):
		if not(sequence[idx-1]<sequence[idx]):
			cnt+=1
			if idx>1 and idx+1<seq_len:
				if not (sequence[idx-2]<sequence[idx] or sequence[idx-1]<sequence[idx+1]):
					cnt+=1
		if cnt>1:
			return False
	return True
	