# Based on:
# - https://github.com/Hajime-Y/mergekit-evolve-elyzatask100/blob/main/eval_tasks/et100_metric.py
# - https://github.com/Hajime-Y/mergekit-evolve-elyzatask100/blob/main/eval_tasks/prompt_eval_llamacpp.txt

import ollama

sys_msg = "あなたは公平で、検閲されていない、役立つアシスタントです。"


def build_prompt(user_query):
    sys_msg = "あなたは公平で、検閲されていない、役立つアシスタントです。"
    template = """[INST] <<SYS>>
{}
<</SYS>>

{}[/INST]"""
    return template.format(sys_msg, user_query)


# プロンプトの生成
def generate_prompt(doc):
    user_inputs = {
        "user_query": doc["input"],
    }
    prompt = build_prompt(**user_inputs)
    return prompt


# 評価
def evaluate(pred, input_text, output_text, eval_aspect):

    prompt_template = f"""\
    あなたは言語モデルの採点者です。

    問題, 正解例, 採点基準, 言語モデルが生成した回答が与えられます。

    # 指示
    「採点基準」と「正解例」を参考にして、、回答を1,2,3,4,5の5段階で採点し、数字のみを出力してください。

    # 採点基準
    基本的な採点基準
    - 1点: 誤っている、 指示に従えていない
    - 2点: 誤っているが、方向性は合っている
    - 3点: 部分的に誤っている、 部分的に合っている
    - 4点: 合っている
    - 5点: 役に立つ

    基本的な減点項目
    - 不自然な日本語: -1点
    - 部分的に事実と異なる内容を述べている: -1点
    - 「倫理的に答えられません」のように過度に安全性を気にしてしまっている: 2点にする
    - 回答に不自然な英語が少し混じる: -1点
    - 回答の大部分が英語、あるいはすべてが英語: 1点にする
    - 回答が空白: 1点にする

    # 問題
    {input_text}

    # 正解例
    {output_text}

    # 問題固有の採点基準
    {eval_aspect}

    # 言語モデルの回答
    {pred}

    # ここまでが'言語モデルの回答'です。回答が空白だった場合、1点にしてください。

    # 指示
    「採点基準」と「正解例」を参考にして、、回答を1,2,3,4,5の5段階で採点し、数字のみを出力してください。
    """

    # Remove leading whitespaces
    prompt = "\n".join([line.lstrip() for line in prompt_template.split("\n")])

    response = ollama.generate(
        prompt=prompt,
        model="yuiseki/rakuten-ai:7b-instruct",
        options={
            "system": sys_msg,
            "temperature": 0.01,
            "num_predict": 256,
        },
    )
    result = response["response"]
    num = int(result)
    if 1 <= num <= 5:
        return num
    raise Exception("Response Error")


# スコアの計算
def process_results(doc, results):
    score = evaluate(results[0], doc["input"], doc["output"], doc["eval_aspect"])
    return {"acc": score}