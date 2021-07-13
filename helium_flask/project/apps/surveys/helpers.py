def generate_questions_json(questions):
    ret = []
    for question in questions:
        ret.append(
            {
                "id": question.id,
                "label": question.label,
                "type": question.type.label,
                "choices": question.choices,
            }
        )
    return ret
