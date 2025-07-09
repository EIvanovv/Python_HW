req_skills = {"Python", "Django", "SQL", "Git"}
candidate_skills = {"Python", "Flask", "Git", "JavaScript"}

matched_skills = req_skills.intersection(candidate_skills)
missing_skills = req_skills.difference(candidate_skills)
extra_skills = candidate_skills.difference(req_skills)

print(f"Matched Skills: {matched_skills}")
print(f"Missing Skills: {missing_skills}")
print(f"Extra Skills: {extra_skills}")