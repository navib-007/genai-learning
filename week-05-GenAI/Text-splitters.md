## 📌 What Are Text Splitters?
Text Splitters break long documents into smaller, manageable chunks, often with overlap, to ensure each piece:
- Fits within token limits of LLMs
- Retains enough context
- Is usable for embeddings or retrieval
*📦 Output: List of Document chunks, each with .page_content and inherited .metadata*

## ❓ Why Use Text Splitters?
| Challenge                         | Solution via Text Splitters                           |
| --------------------------------- | ----------------------------------------------------- |
| LLMs have token limits            | Split text into chunks that fit in the context window |
| Embedding quality drops with size | Smaller chunks are semantically dense                 |
| Retrieval misses context          | Overlapping chunks preserve continuity                |
| Need relevance + granularity      | Chunking improves accuracy in RAG pipelines           |

## 🔧 How They Work
flowchart LR
A[Full Document] --> B[TextSplitter]
B --> C[Chunk 1: text...]
B --> D[Chunk 2: overlap + next part...]
C & D --> E[Embedding Model or Vector Store]

## 🧰 Popular Text Splitters in LangChain
| Splitter Type                    | Description                                              | Best Use Case                        |
| -------------------------------- | -------------------------------------------------------- | ------------------------------------ |
| `CharacterTextSplitter`          | Splits text based on character count                     | Simple docs, fast splitting          |
| `RecursiveCharacterTextSplitter` | Recursive splitting on characters, paragraphs, sentences | PDFs, HTML, structured data          |
| `TokenTextSplitter`              | Splits based on token count (uses tokenizer)             | Exact token control for LLM input    |
| `SpacyTextSplitter`              | Uses spaCy's NLP parsing                                 | Sentence-aware splitting             |
| `MarkdownHeaderTextSplitter`     | Splits based on Markdown headers (`#`, `##`, etc.)       | Markdown knowledge bases, blog posts |
| `NLTKTextSplitter`               | Sentence-based splitting with NLTK                       | Academic or formal language docs     |
| `HTMLHeaderTextSplitter`         | Splits HTML using heading tags (`<h1>`, `<h2>`)          | Websites, blog pages                 |

## ✅ 1. Recursive Character Text Splitter
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)
```
### 📌 Why it’s powerful:
- Tries to split on paragraphs → sentences → words
- Produces natural-looking chunks
- Handles structured docs better than flat splitting

## ✅ 2. Token Text Splitter
```python
from langchain.text_splitter import TokenTextSplitter

splitter = TokenTextSplitter(
    chunk_size=300,
    chunk_overlap=20
)

chunks = splitter.split_documents(documents)
```
🔍 Ideal when:
- You want fine-grained control of token limits
- Your LLM has a strict context window (e.g., OpenAI models)

## ✅ 3. MarkdownHeaderTextSplitter
```python
from langchain.text_splitter import MarkdownHeaderTextSplitter

headers_to_split_on = [("#", "Header 1"), ("##", "Header 2")]
splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

chunks = splitter.split_text(markdown_text)
```
## 📌 Adds hierarchical metadata for tracing sections like:
- Chapter titles
- Blog sections
- Nested headers

| Use Case                     | Text Splitter Type                       |
| ---------------------------- | ---------------------------------------- |
| PDFs with mixed structure    | `RecursiveCharacterTextSplitter`         |
| Chat inputs for LLMs         | `TokenTextSplitter`                      |
| Blog/Docs/Markdown files     | `MarkdownHeaderTextSplitter`             |
| Scientific or sentence-heavy | `NLTKTextSplitter` / `SpacyTextSplitter` |
| HTML-based articles          | `HTMLHeaderTextSplitter`                 |

## 🧪 Example: Full Flow with Document Loader + Splitter
```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 1. Load
loader = PyPDFLoader("policy.pdf")
documents = loader.load()

# 2. Split
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(documents)

# 3. View
print(chunks[0].page_content)
print(chunks[0].metadata)
```

## 📌 Best Practices
| Practice                               | Why It Helps                             |
| -------------------------------------- | ---------------------------------------- |
| ✅ Use chunk overlap                    | Maintains context across boundaries      |
| ✅ Select splitter based on data format | Markdown ≠ PDF ≠ web ≠ code              |
| ✅ Normalize chunk sizes                | Improves embedding and retrieval quality |
| ✅ Always keep metadata intact          | Traceability in RAG and logging          |

## ✅ Summary Table
| Feature             | Description                                      |
| ------------------- | ------------------------------------------------ |
| `chunk_size`        | Max size of each chunk (in characters or tokens) |
| `chunk_overlap`     | Overlap between chunks to preserve context       |
| `split_documents()` | Split list of `Document` objects                 |
| `split_text()`      | Split plain string input                         |