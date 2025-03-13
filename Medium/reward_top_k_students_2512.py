from typing import List


class Solution:

    def calculate_reward(self, report_, positive_feedback, negative_feedback):
        count = 0

        for r in report_.split(' '):
            if r in positive_feedback:
                count += 3

            if r in negative_feedback:
                count -= 1

        return count

    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        mp = {}
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)

        for report_, s_id in zip(report, student_id):
            reward = self.calculate_reward(
                report_, positive_feedback, negative_feedback)
            mp[s_id] = reward

        return sorted(mp.keys(), key=lambda x: (-mp[x], x))[:k]


obj = Solution()
positive_feedback = ["smart", "brilliant", "studious"]
negative_feedback = ["not"]
report = ["this student is not studious", "the student is smart"]
student_id = [1, 2]
k = 2
print(obj.topStudents(positive_feedback, negative_feedback, report, student_id, k))
