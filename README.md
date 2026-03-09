# Toy LangChain Prompt Injection Experiment

This repo contains a small, single-file experiment to study **direct prompt injection** against a **tool-calling LangChain agent**.

## Why `py_compile` appears to do "nothing"

If you run:

```bash
python -m py_compile toy_langchain_prompt_injection.py
```

that command only checks syntax and writes Python bytecode. It is expected to be silent on success.
No experiment is executed by `py_compile`.

## How to actually run the experiment

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Export your OpenAI key:

```bash
export OPENAI_API_KEY=your_key_here
```

3. Run the script:

```bash
python toy_langchain_prompt_injection.py
```

Compatibility filename (if you typed `toy_chain_prompt_injection.py`):

```bash
python toy_chain_prompt_injection.py
```

## Expected output

The script prints two experiment blocks:

- Experiment 1: Normal Query
- Experiment 2: Direct Prompt Injection

For each block it shows:

- tools called
- tool arguments
- final response
- whether `CANARY_SECRET_12345` leaked
