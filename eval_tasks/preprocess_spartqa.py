def doc_to_text(doc) -> str:
    answer_chunks = []
    for idx, answer in enumerate(doc["candidate_answers"]):
        letter = "ABCD"[idx]
        answer_chunks.append(f"{letter}. {answer}")
    answers = "\n".join(answer_chunks)
    return f"Context:\n{doc['story']}\n\nQuestion: {doc['question']}\n{answers}\nAnswer:"
