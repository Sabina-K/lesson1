marks = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
{'school_class': '3b', 'scores': [5,3,4,3,3]},
{'school_class': '5a', 'scores': [3,3,3,5,2]}, 
{'school_class': '11b','scores': [5,4,5,5,4]}]

sum_per_school = 0
pupil_in_school = 0
for item in marks:
	sum_per_class = sum(item['scores'])
	sum_per_school = sum_per_school + sum_per_class
	pupil_per_class = len(item['scores'])
	pupil_in_school = pupil_in_school + pupil_per_class
	sr_ball_per_class = sum_per_class / pupil_per_class
	print(sr_ball_per_class)

sr_ball_per_school = sum_per_school/pupil_in_school
print(sr_ball_per_school)





#pupil_per_class = (len(marks[2]["scores"]))
    #sr_ball_per_class = pupil_per_class/sum_per_class
    #print(sr_ball_per_class)