"""Compatibility entrypoint.

Some users run `toy_chain_prompt_injection.py` by name.
This shim forwards to the real script: `toy_langchain_prompt_injection.py`.
"""

from toy_langchain_prompt_injection import main


if __name__ == "__main__":
    main()
