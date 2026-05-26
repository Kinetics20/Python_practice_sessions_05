# Weaviate Cloud Concepts

## Overview

This note summarizes the Weaviate Cloud workflows implemented in the project notebooks.

The main goal of these notebooks is to move local Weaviate experiments from Docker to a Weaviate Cloud cluster.

The implemented topics include:

- CRUD operations
- vector search
- hybrid search
- generative search
- text-to-image search
- RAG over local project files

---

## Weaviate Cloud Connection

In local notebooks, Weaviate was started in Docker and connected with:

```python
weaviate.connect_to_local(...)
```

In Weaviate Cloud, the client connects to a remote cluster:

```python
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=Auth.api_key(os.environ["WEAVIATE_API_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"],
    },
)
```

The Weaviate API key authenticates the user to the cluster.

The OpenAI API key is used by Weaviate modules such as:

- `text2vec_openai`
- `generative_openai`

---

## Basic Weaviate Data Model

Weaviate stores data in collections.

A collection is similar to a SQL table.

An object is similar to a SQL row or record.

A property is similar to a SQL column.

A UUID is similar to a primary key.

Comparison:

| SQL | Weaviate |
|---|---|
| database / schema | cluster / Weaviate instance |
| table | collection |
| column | property |
| row / record | object |
| primary key | UUID |
| index | vector index / inverted index |

---

## CRUD Operations

CRUD means:

- Create
- Read
- Update
- Delete

In Weaviate, CRUD is performed on a collection.

Example:

```python
questions = client.collections.get("Question")
```

Create object:

```python
uuid = questions.data.insert({
    "question": "This planet is known as the Red Planet.",
    "answer": "Mars",
    "category": "Science",
})
```

Read object:

```python
obj = questions.query.fetch_object_by_id(uuid=uuid)
```

Update object:

```python
questions.data.update(
    uuid=uuid,
    properties={"category": "Astronomy"},
)
```

Delete object:

```python
questions.data.delete_by_id(uuid)
```

Closing the client with `client.close()` only closes the Python connection. It does not delete collections or objects from the cloud cluster.

---

## Embeddings and Vector Length

An embedding is a numeric representation of text, image, or another data type.

For example, OpenAI `text-embedding-3-small` can produce vectors with length `1536`.

This means that one text is represented as a list of 1536 floating-point numbers.

Example:

```text
"GPU for machine learning"
↓
[0.012, -0.034, 0.088, ..., 0.004]
```

The exact meaning of each number is not human-readable. The model learns to place semantically similar texts close to each other in vector space.

Texts with similar meaning should have similar vectors.

---

## Vector Search

Vector search is semantic search.

It searches by meaning, not only by exact keywords.

The query is converted into an embedding and compared with vectors stored in Weaviate.

Example:

```python
response = questions.query.near_text(
    query="animals",
    limit=5,
    return_metadata=MetadataQuery(distance=True),
)
```

A smaller distance usually means higher semantic similarity.

Vector search is useful when the user asks natural language questions or uses words different from the original document.

Example:

```text
query: hardware for machine learning
```

This can return documents about:

- GPU
- VRAM
- AI workloads
- parallel computations

even if the exact query words are not present in the document.

---

## BM25 Keyword Search

BM25 is a keyword-based search algorithm.

It searches for exact or close word matches in text fields.

Example:

```python
response = questions.query.bm25(
    query="GPU",
    query_properties=["title", "content", "component"],
    limit=3,
)
```

BM25 works well for:

- exact terms
- names
- IDs
- technical keywords
- categories
- acronyms

Example:

```text
query: GPU
```

BM25 prefers documents containing the word `GPU`.

---

## BM25 vs Vector Search

BM25 searches by keywords.

Vector search searches by meaning.

BM25 is best when exact words matter.

Vector search is best when semantic similarity matters.

Comparison:

| Search type | Main idea | Good for |
|---|---|---|
| BM25 | keyword matching | exact terms, names, categories |
| Vector search | semantic similarity | natural language, paraphrases, meaning |
| Hybrid search | BM25 + vector search | balanced search quality |

---

## Hybrid Search

Hybrid search combines BM25 and vector search.

It uses both:

- keyword matching
- semantic similarity

Example:

```python
response = questions.query.hybrid(
    query="animal",
    alpha=0.5,
    limit=5,
)
```

The `alpha` parameter controls the balance.

```text
alpha = 0.0 -> mostly BM25 / keyword search
alpha = 0.5 -> balanced BM25 + vector search
alpha = 1.0 -> mostly vector search
```

Hybrid search is often better than using only BM25 or only vector search because it combines exact keyword matching with semantic understanding.

---

## Generative Search

Generative search combines retrieval with LLM-based generation.

The flow is:

```text
user query
↓
Weaviate creates an embedding
↓
Weaviate retrieves similar objects
↓
retrieved objects are passed to an LLM
↓
LLM generates an answer
```

A collection used for generative search needs both:

```python
vector_config=wvc.config.Configure.Vectors.text2vec_openai(...)
```

and:

```python
generative_config=wvc.config.Configure.Generative.openai(...)
```

`vector_config` is responsible for embeddings and semantic search.

`generative_config` is responsible for generating answers using an LLM.

---

## single_prompt

`single_prompt` generates a separate answer for each retrieved object.

Example:

```python
response = questions.generate.near_text(
    query="animals",
    single_prompt="Explain this answer in one simple sentence: {answer}",
    limit=3,
)
```

The placeholders are replaced with object properties.

Example placeholders:

```text
{question}
{answer}
{category}
```

This is useful when each result should receive its own generated explanation.

---

## grouped_task

`grouped_task` generates one shared answer based on multiple retrieved objects.

Example:

```python
response = questions.generate.near_text(
    query="history and politics",
    grouped_task="Summarize what common topic connects these questions.",
    limit=5,
)
```

This is useful for:

- summarization
- comparison
- answering based on several objects
- simple RAG-style answers

---

## Text-to-Image Search

The local Docker version used the `multi2vec_clip` module.

In Weaviate Cloud, this module may not be available in the same way, so the cloud workflow uses local CLIP embeddings.

The flow is:

```text
local image
↓
local CLIP model creates image embedding
↓
image filename and vector are stored in Weaviate Cloud
↓
text query is embedded locally
↓
Weaviate performs near_vector search
↓
notebook displays matching local images
```

The images themselves remain local in the `images/` directory.

Weaviate Cloud stores:

- filename
- local path
- image vector

The collection uses self-provided vectors:

```python
vector_config=[
    wvc.config.Configure.Vectors.self_provided(
        name="image_vector",
    )
]
```

Text-to-image search uses:

```python
response = images.query.near_vector(
    near_vector=query_vector,
    target_vector="image_vector",
    limit=3,
)
```

This means that the text query and the images are embedded into the same CLIP vector space.

---

## Bring Your Own Vectors

Bring Your Own Vectors means that Weaviate does not create embeddings automatically.

Instead, the application creates vectors and sends them to Weaviate.

This is useful for:

- image embeddings
- custom embedding models
- CLIP-based multimodal search
- local model experiments

Example:

```python
uuid = images.data.insert(
    properties={
        "filename": path.name,
        "local_path": str(path),
    },
    vector={
        "image_vector": vector,
    },
)
```

---

## RAG over Project Files

RAG means Retrieval-Augmented Generation.

The basic flow is:

```text
local files
↓
text extraction
↓
chunking
↓
embedding creation
↓
storage in Weaviate Cloud
↓
retrieval
↓
LLM-generated answer
```

A RAG collection can store chunks of local files.

Example properties:

```text
content
source
file_type
chunk_index
```

The `content` property stores the chunk text.

The `source` property stores the file path.

The `file_type` property stores the file extension.

The `chunk_index` property stores the chunk number inside the source file.

---

## Chunking

Chunking means splitting long text into smaller parts.

This is needed because:

- embeddings work better on smaller text fragments
- LLM context is limited
- retrieval should return focused pieces of information
- large files can contain many unrelated topics

Example chunk parameters:

```text
chunk_size = 1200
overlap = 200
```

Overlap helps preserve context between neighboring chunks.

---

## RAG Retrieval Quality

Good RAG depends on good retrieval.

If the collection contains too many unrelated files, the system may retrieve irrelevant chunks.

Example problem:

```text
question: Where is text-to-image search implemented?
retrieved context: random README files, output files, unrelated scripts
result: context is insufficient
```

This means that the LLM did not receive the right context.

A better approach is to create a focused collection for a specific domain.

Example:

```text
WeaviateNotebookChunk
```

This collection should contain only:

- Weaviate notebooks
- Weaviate notes
- related markdown explanations

Focused context usually gives better RAG answers than one huge collection containing the whole repository.

---

## Code vs Conceptual Notes in RAG

Notebook code is good for implementation questions.

Example:

```text
Where is text-to-image search implemented?
Which notebook uses CLIP embeddings?
Which collection is created?
Which model is used?
```

Markdown notes are better for conceptual questions.

Example:

```text
What is the difference between BM25 and vector search?
What is hybrid search?
What is RAG?
Why use chunking?
What does alpha mean?
```

For a good RAG system, it is useful to index both:

- `.ipynb` files for implementation details
- `.md` files for conceptual explanations

---

## Recommended Weaviate RAG Collection Design

For a focused Weaviate learning assistant, create a collection that contains only Weaviate-related files.

Suggested collection:

```text
WeaviateNotebookChunk
```

Suggested indexed paths:

```text
vector_db/*.ipynb
vector_db/notes/*.md
```

This allows the assistant to answer both implementation and concept questions.

The notebooks provide code context.

The markdown notes provide conceptual knowledge.

---

## Summary

The project demonstrates how to use Weaviate Cloud for:

- CRUD operations
- semantic vector search
- BM25 keyword search
- hybrid search
- generative search
- text-to-image search with CLIP embeddings
- RAG over project files

The main idea is:

```text
Weaviate Cloud stores objects, metadata, and vectors.
Embedding models convert text or images into vectors.
Search methods retrieve relevant objects.
Generative models can produce answers from retrieved context.
```

For reliable RAG, use clean and focused collections.

A good Weaviate RAG setup should combine:

```text
implementation context from notebooks
+
conceptual knowledge from markdown notes
```