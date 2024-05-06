mergekit-evolve ./configs/evolve/YuisekinAIEvol-mistral-ja-sql.yaml\
    --storage-path ./evol_merge_storage \
    --task-search-path ./eval_tasks \
    --trust-remote-code \
    --in-memory \
    --merge-cuda \
    --max-fevals 1000 \
    --wandb
