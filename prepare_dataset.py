import datasets

ds = datasets.load_dataset("metaeval/spartqa-mchoice")["train"]
ds_p = ds.shuffle(seed=9163).select(range(1000))
ds_p.push_to_hub("yuiseki/spartqa-train-1k", private=True)

ds = datasets.load_dataset("shunk031/JGLUE", "JCommonsenseQA", trust_remote_code=True)["train"]
ds_p = ds.shuffle(seed=9163).select(range(1000))
ds_p.push_to_hub("yuiseki/jcommonsenseqa-train-1k", private=True)

ds = datasets.load_dataset("math_qa")["train"]
ds_p = ds.shuffle(seed=9163).select(range(1000))
ds_p.push_to_hub("yuiseki/math_qa-train-1k", private=True)

ds = datasets.load_dataset("b-mc2/sql-create-context")["train"]
ds_p = ds.shuffle(seed=9163).select(range(1000))
ds_p.push_to_hub("yuiseki/sql-create-context-train-1k", private=True)

ds = datasets.load_dataset("vicgalle/alpaca-gpt4")["train"]
df = ds.to_pandas()

no_input = df[df.input.map(len) < 1]
examples = no_input.sample(n=500, replace=False, random_state=749)
ds_p = datasets.Dataset.from_pandas(examples)
ds_p.push_to_hub("yuiseki/alpaca-gpt4-500", private=True)
