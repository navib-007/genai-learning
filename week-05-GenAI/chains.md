# Chains
## 📌 What Are Chains in LangChain?
* Chains are a way to combine multiple components (like prompts, LLMs, tools, retrievers) into a logical sequence or workflow.
* A chain takes an input, processes it through one or more steps (e.g., prompt → LLM → output), and returns a result.
 
💡 Think of it as pipelines or composable blocks for building intelligent workflows.

## ❓ Why Do Chains Exist?
LLMs alone can:
- Respond to a prompt
- Answer simple questions
But real-world use cases require:
- Prompt creation + LLM call + post-processing
- Memory/context management
- Document retrieval + answering
- Multi-step reasoning or tool use
**Chains enable you to orchestrate these steps seamlessly and reusably.**

## 🧰 How Chains Help Developers
| Benefit             | Description                                                                |
| ------------------- | -------------------------------------------------------------------------- |
| ✅ Modularity        | Reuse components like prompts, LLMs, and retrievers in different workflows |
| ✅ Maintainability   | Clean separation between logic, input, and execution                       |
| ✅ Flexibility       | Easily compose custom workflows or plug-and-play with built-ins            |
| ✅ Integration-ready | Connect with FastAPI, React, Streamlit, etc.                               |
| ✅ Debuggability     | LangSmith and `run`/`invoke` APIs help trace execution flow                |

## 🔧 Types of Chains in LangChain
| Chain Type                | Description                                              | Use Case Example                       |
| ------------------------- | -------------------------------------------------------- | -------------------------------------- |
| `LLMChain`                | Basic chain: prompt → LLM → output                       | Text generation, content rewriting     |
| `SequentialChain`         | Runs multiple chains step-by-step, passing outputs       | Multi-step reasoning, translation → QA |
| `SimpleSequentialChain`   | Simplified version of sequential chain                   | Basic chaining                         |
| `RetrievalQA`             | Combines retriever (vector DB) + LLM to answer questions | RAG over PDFs, docs, websites          |
| `ConversationChain`       | Chat + memory (chat history) + LLM                       | Stateful assistants                    |
| `MapReduceDocumentsChain` | Summarize large docs in chunks + combine results         | Long document summarization            |

1. Basic LLM chain
```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short article about {topic}."
)

llm = OpenAI(temperature=0.7)
chain = LLMChain(prompt=prompt, llm=llm)

response = chain.run(topic="LangChain in AI")
print(response)
```
* 💡 Use Case: Single-step generation with dynamic input.

2. RetrievalQA Chain (RAG)
```python
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI

# Vector DB with embedded documents
retriever = Chroma.from_documents(docs, embedding=OpenAIEmbeddings()).as_retriever()

qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retriever)
response = qa_chain.run("What is LangChain?")
```
* 💡 Use Case: Query unstructured documents using retrieval + generation.

3. Simple Sequential Chain
```python
from langchain.chains import SimpleSequentialChain

# Step 1: Generate a title
title_chain = LLMChain(prompt=PromptTemplate.from_template("Write a blog title about {topic}."), llm=llm)

# Step 2: Generate blog based on title
blog_chain = LLMChain(prompt=PromptTemplate.from_template("Write a blog post titled '{title}'."), llm=llm)

# Combine
overall_chain = SimpleSequentialChain(chains=[title_chain, blog_chain], verbose=True)

result = overall_chain.run("AI in education")
print(result)
```
* 💡 Use Case: Multi-step workflows with intermediate transformations.

4. Custom Chain (Using LangChain Expression Language – LCEL)
```python
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

prompt = PromptTemplate.from_template("Explain {concept} in simple terms.")
llm = ChatOpenAI()
parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | llm | parser
chain.invoke({"concept": "retrieval-augmented generation"})
```
* 💡 Use Case: Lightweight and flexible chaining without boilerplate.

| Feature               | Description                                                      |
| --------------------- | ---------------------------------------------------------------- |
| **Chain**             | Sequence of steps to process input and produce structured output |
| **LLMChain**          | Prompt + LLM → Output                                            |
| **RetrievalQAChain**  | Retriever + Prompt + LLM → Answer                                |
| **SequentialChain**   | Multi-step pipeline passing outputs between steps                |
| **ConversationChain** | Adds memory to chatbot conversations                             |

| Scenario                     | Recommended Chain   |                         |
| ---------------------------- | ------------------- | ----------------------- |
| Static prompt → generation   | `LLMChain`          |                         |
| Chatbot with memory          | `ConversationChain` |                         |
| RAG with document embeddings | `RetrievalQA`       |                         |
| Step-by-step generation      | `SequentialChain`   |                         |
| Custom logic with LCEL       | \`                  | ` composition (`pipe\`) |