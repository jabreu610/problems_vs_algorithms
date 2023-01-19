import os

def create_project_files(base: str, suffix: str) -> None:
    project_dir = os.path.join(base, f"problem_{suffix}")
    os.mkdir(project_dir)
    problem, explanation = [f"problem_{suffix}.py", f"explanation_{suffix}.md"]
    with open(os.path.join(project_dir, problem), 'w') as handle:
        template = "if __name__ == \"__main__\":\n    pass"
        handle.write(template)
    with open(os.path.join(project_dir, explanation), 'x') as handle:
        template = f"# Explanation {suffix}\n\n## Rationale\n\n## Runtime Analysis"
        handle.write(template)


if __name__ == "__main__":
    base = os.getcwd()
    for problem_number in range(1, 8):
        create_project_files(base, str(problem_number))