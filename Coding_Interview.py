"""Create a function to check if a candidate is qualified in an coding interview round of a tech startup.
The criteria for a candidate to be qualified in the coding interview
The candidate should have complete all the questions. The maximum time given to complete the interview is 120 minutes.
The maximum time given for very easy questions is 5 minutes each.
The maximum time given for easy questions is 10 minutes each.
The maximum time given for medium questions is 15 minutes each.
The maximum time given for hard questions is 20 minutes each
If all the above conditions are satisfied, return "qualified", else return "disqualified"
You will be given a list of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview
Given a list in a true condition will always be in the format [very easy very easy easy easy, medium, medium, hard hard].
The maximum time to complete the interview includes a buffer time of 20 minutes.
Examples:
interview([5, 5, 10, 10, 15, 15, 20, 20], 120) → 1.
1 means "qualified"
interview([5, 5, 10, 10, 15, 15, 20, 20], 130) → 0
0 means "disqualified"
Solved all the questions in their respected time limits but exceeded the total time limit of the interview.
Note:
Some of the candidates may solved the questions above the time limit given to each questions are disqualified and some candidates are not even attend all the questions are disqualified.
sample input:
5 5 10 10 15 15 20 20
120
sample output:
1"""

def interview(Q_times, total_time):
  Q_time_limits = [5,5,10,10,15,15,20,20]
  if len(Q_times) != 8:
    return 0
  for i in range(8):
    if Q_times[i] > Q_time_limits[i]:
      return 0
  time_taken = sum(Q_times):
  buffer_time = total_time - time_taken
  if time_taken <= 100 and buffer_time <= 20:
    return 1
  else:
    return 0

if __name__ == '__main__':
  Q_timing = list(map(int,input().split()))
  total_timing = int(input())
  print(interview(Q_timing,total_timing))
