meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]


sorted_meetings = sorted(meetings)
merged_meetings = [sorted_meetings[0]]

for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
	last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

	if (current_meeting_start <= last_merged_meeting_end):
		merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
	else:
		merged_meetings.append((current_meeting_start, current_meeting_end))

print(merged_meetings) 