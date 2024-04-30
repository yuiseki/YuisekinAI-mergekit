# YuisekinAI-mergekit

## Setup

### Create Anaconda environment

```bash
conda create -n mergekit python=3.10
conda install -c conda-forge -c nvidia -c pytorch pytorch=2.1.2 cuda-toolkit=12.1 cuda-nvcc=12.1 cudnn=8.9
```

### Install mergekit

```bash
git clone https://github.com/arcee-ai/mergekit.git
cd mergekit
pip install -e .[evolve,vllm]
```

### Prepare dataset

```bash
python prepare_dataset.py
```

### Execute evolve

```bash
./evol.sh
```

### Execute merge

```bash
./merge.sh
```