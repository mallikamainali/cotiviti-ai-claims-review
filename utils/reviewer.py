def review_claim(note, guideline):
    note = note.lower()

    missing = []

    for finding in guideline["required_findings"]:
        if finding.lower() not in note:
            missing.append(finding)

    if len(missing) == 0:
        decision = "APPROVE"
        explanation = (
            "The documentation contains all required clinical findings "
            "to support the billed procedure."
        )
    else:
        decision = "FLAG FOR REVIEW"
        explanation = (
            "Some required clinical findings are missing. "
            "A human reviewer should verify medical necessity."
        )

    return {
        "decision": decision,
        "missing": missing,
        "explanation": explanation,
    }