```bash

git clone https://github.com/time1527/langchain-academy.git
cd langchain-academy
conda create -n py311 python=3.11 --
y
conda activate py311
pip install -r requirements.txt
```

```bash
touch .env
echo "DASHSCOPE_API_KEY=sk-1234567890abcdef1234567890abcdef" >> .env
echo "LANGSMITH_API_KEY=lsv2_sk_1234567890abcdef1234567890abcdef" >> .env
echo "LANGSMITH_TRACING_V2=true" >> .env
echo "LANGSMITH_PROJECT=langchain-academy" >> .env
echo "TAVILY_API_KEY=tvly-1234567890abcdef1234567890abcdef" >> .env
```

```bash
cd cn-module-x/studio
touch .env
echo "DASHSCOPE_API_KEY=sk-1234567890abcdef1234567890abcdef" >> .env
langgraph dev
```

模型：Qwen-plus

ipynb翻译：codex

注释：Trae

视频资源：https://academy.langchain.com/courses/intro-to-langgraph