def doc_to_text(doc) -> str:
    answer_chunks = []
    answer_fields = ["choice0", "choice1", "choice2", "choice3", "choice4"]
    for idx, field in enumerate(answer_fields):
        letter = "01234"[idx]
        answer_chunks.append(f"{letter}. {doc[field]}")
    answers = "\n".join(answer_chunks)
    return f"Question: {doc['question']}\n{answers}\nAnswer:"
