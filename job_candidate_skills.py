req_skills = {"Python", "Django", "SQL", "Git"}
candidate_skills = {"Python", "Flask", "Git", "JavaScript"}

matched_skills = req_skills.intersection(candidate_skills)
missing_skills = req_skills.difference(candidate_skills)
extra_skills = candidate_skills.difference(req_skills)

print("")
print(f"Matched Skills: {','.join(matched_skills)}")
print(f"Missing Skills: {','.join(missing_skills)}")
print(f"Extra Skills: {','.join(extra_skills)}")