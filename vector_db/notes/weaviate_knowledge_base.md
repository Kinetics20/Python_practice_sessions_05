# Weaviate Knowledge Base for Voice Agent

## Purpose

This knowledge base summarizes the Weaviate topics practiced in local Docker notebooks and later migrated to Weaviate Cloud Cluster notebooks.

The assistant should use this file to answer questions about:

- Weaviate basics
- Weaviate Cloud connection
- Docker vs Cloud setup
- collections, objects, properties and UUIDs
- CRUD operations
- embeddings and vector length
- vector search
- BM25 keyword search
- hybrid search
- generative search
- text-to-image search with CLIP
- bring your own vectors
- RAG over project files
- focused RAG with notebooks and Markdown notes
- named vectors
- cross-references
- multi-tenancy

The assistant should answer in English by default. If the user asks in Polish, the assistant may answer in Polish.

---

# 1. Weaviate Overview

Weaviate is an AI-native vector database.

It stores objects, metadata, and vectors. It can be used for semantic search, keyword search, hybrid search, generative search, image search, and Retrieval-Augmented Generation.

Weaviate can run locally in Docker or remotely in Weaviate Cloud.

In the local Docker setup, Weaviate was used as a local database for experiments.

In the Weaviate Cloud setup, the same workflows were moved to a remote cluster.

---

# 2. Docker Weaviate vs Weaviate Cloud

## Local Docker setup

In the local setup, Weaviate was usually started in Docker and connected with:

```python
client = weaviate.connect_to_local(headers=headers)
```

This setup is useful for learning, testing, and running local modules such as `multi2vec_clip`.

## Weaviate Cloud setup

In Weaviate Cloud, the Python client connects to a remote cluster:

```python
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=Auth.api_key(os.environ["WEAVIATE_API_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"],
    },
)
```

The Weaviate API key authenticates the client to the Weaviate Cloud cluster.

The OpenAI API key is used by Weaviate modules such as:

- `text2vec_openai`
- `generative_openai`

The REST endpoint is used as the main cluster URL. The gRPC endpoint should not usually be used directly in beginner notebooks because the Python client can handle the connection details.

---

# 3. Basic Weaviate Data Model

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

Example collection:

```python
questions = client.collections.get("Question")
```

Example object:

```python
{
    "question": "This planet is known as the Red Planet.",
    "answer": "Mars",
    "category": "Science",
}
```

---

# 4. Client Lifecycle

`client.close()` only closes the active Python connection to the Weaviate cluster.

It does not delete collections, objects, tenants, vectors, or data.

After closing the client, the user can reconnect and continue working with the same collections.

Example:

```python
client.close()
```

Reconnect later:

```python
client = weaviate.connect_to_weaviate_cloud(...)
questions = client.collections.get("Question")
```

---

# 5. CRUD Operations

CRUD means:

- Create
- Read
- Update
- Delete

CRUD operations are performed on a collection.

## Create

```python
uuid = questions.data.insert({
    "question": "This planet is known as the Red Planet.",
    "answer": "Mars",
    "category": "Science",
})
```

## Read

```python
obj = questions.query.fetch_object_by_id(uuid=uuid)
```

## Update

```python
questions.data.update(
    uuid=uuid,
    properties={
        "category": "Astronomy",
    },
)
```

## Delete

```python
questions.data.delete_by_id(uuid)
```

To delete an object, first fetch or list objects to find the correct UUID, then call `delete_by_id`.

---

# 6. Collections Used in the Learning Notebooks

The user created or discussed collections such as:

- `Question`
- `Article`
- `QuestionVector`
- `QuestionHybrid`
- `QuestionGenerative`
- `HardwareArticle`
- `ClipImageCloud`
- `ProjectChunk`
- `WeaviateNotebookChunk`
- `WeaviateFocusedRagChunk`
- `HardwareNamedVector`
- `HardwareProduct`
- `HardwareReview`
- `TenantDocument`

Each collection was used to demonstrate a separate Weaviate concept.

---

# 7. Embeddings

An embedding is a numeric representation of text, image, or another data type.

For example, a text such as:

```text
GPU for machine learning
```

can be transformed into a vector:

```text
[0.012, -0.034, 0.088, ..., 0.004]
```

The numbers are not directly human-readable. They represent semantic features learned by the embedding model.

Texts with similar meaning should have similar vectors.

---

# 8. Vector Length

Vector length means the number of dimensions in an embedding.

For example, OpenAI `text-embedding-3-small` can produce a vector with length `1536`.

This means that one piece of text is represented by 1536 floating-point numbers.

Example:

```python
print(len(obj.vector["default"]))
```

Output:

```text
1536
```

All vectors inside the same vector space must have the same length.

It is not valid to mix vectors of different dimensions in the same named vector space, for example:

- 1536-dimensional OpenAI text embeddings
- 512-dimensional CLIP embeddings
- 3072-dimensional larger text embeddings

---

# 9. Vector Search

Vector search is semantic search.

It searches by meaning, not only by exact words.

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

Vector search is useful when the user asks natural language questions or uses words that differ from the original document.

Example query:

```text
hardware for machine learning
```

This may return documents about:

- GPU
- VRAM
- AI workloads
- CUDA
- parallel computations

even if the exact query words are not present.

---

# 10. BM25 Keyword Search

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
- product names
- technical keywords
- acronyms
- categories
- IDs

Example:

```text
query: GPU
```

BM25 will prefer documents that contain the word `GPU`.

---

# 11. BM25 vs Vector Search

BM25 searches by keywords.

Vector search searches by semantic meaning.

Comparison:

| Search type | Main idea | Good for |
|---|---|---|
| BM25 | keyword matching | exact terms, names, categories |
| Vector search | semantic similarity | natural language, paraphrases, meaning |
| Hybrid search | BM25 + vector search | balanced search quality |

BM25 is best when exact words matter.

Vector search is best when the user describes meaning in natural language.

---

# 12. Hybrid Search

Hybrid search combines BM25 keyword search and vector search.

It uses both:

- exact or close keyword matching
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

Hybrid search is often stronger than only BM25 or only vector search because it combines exact matching with semantic understanding.

---

# 13. Generative Search

Generative search combines retrieval with LLM generation.

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

`generative_config` is responsible for LLM-generated answers.

---

# 14. single_prompt

`single_prompt` generates a separate answer for each retrieved object.

Example:

```python
response = questions.generate.near_text(
    query="animals",
    single_prompt="Explain this answer in one simple sentence: {answer}",
    limit=3,
)
```

Placeholders are replaced with object properties.

Example placeholders:

```text
{question}
{answer}
{category}
```

This is useful when each search result should receive its own generated explanation.

---

# 15. grouped_task

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
- RAG-style answers
- answering based on several retrieved objects

---

# 16. Text-to-Image Search

The local Docker workflow used `multi2vec_clip`.

In Weaviate Cloud, the workflow used local CLIP embeddings instead.

The images remain local, while Weaviate Cloud stores metadata and vectors.

The flow is:

```text
local image
↓
local CLIP model creates image embedding
↓
filename and vector are stored in Weaviate Cloud
↓
text query is embedded locally
↓
Weaviate performs near_vector search
↓
notebook displays matching local images
```

The collection can use self-provided vectors:

```python
vector_config=[
    wvc.config.Configure.Vectors.self_provided(
        name="image_vector",
    )
]
```

Insert image vector:

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

Search with text-to-image vector:

```python
response = images.query.near_vector(
    near_vector=query_vector,
    target_vector="image_vector",
    limit=3,
)
```

This works because text and images are embedded into the same CLIP vector space.

---

# 17. Bring Your Own Vectors

Bring Your Own Vectors means that the application creates the vectors and sends them to Weaviate.

Weaviate does not create embeddings automatically in this mode.

This is useful for:

- image embeddings
- custom embedding models
- CLIP-based multimodal search
- local model experiments

Example:

```python
vector={
    "image_vector": vector,
}
```

---

# 18. RAG over Project Files

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

`content` stores the chunk text.

`source` stores the file path.

`file_type` stores the extension.

`chunk_index` stores the chunk number inside the source file.

---

# 19. Chunking

Chunking means splitting long text into smaller pieces.

This is needed because:

- embeddings work better on smaller fragments
- LLM context is limited
- retrieval should return focused information
- large files can contain many unrelated topics

Example:

```text
chunk_size = 1200
overlap = 200
```

Overlap preserves context between neighboring chunks.

---

# 20. RAG Retrieval Quality

Good RAG depends on good retrieval.

If the collection contains too many unrelated files, Weaviate may retrieve irrelevant chunks.

Example problem:

```text
question: Where is text-to-image search implemented?
retrieved context: unrelated output files or random README files
result: context is insufficient
```

This means the LLM did not receive the right context.

A better approach is to create focused collections for specific domains.

Example:

```text
WeaviateNotebookChunk
```

This collection should contain only:

- Weaviate notebooks
- Weaviate notes
- related Markdown explanations

Focused context usually gives better RAG answers than one huge collection with the entire repository.

---

# 21. Code vs Concept Notes in RAG

Notebook code is good for implementation questions.

Example questions:

```text
Where is text-to-image search implemented?
Which notebook uses CLIP?
Which collection is created?
Which model is used?
```

Markdown notes are better for conceptual questions.

Example questions:

```text
What is the difference between BM25 and vector search?
What is hybrid search?
What is RAG?
Why use chunking?
What does alpha mean?
```

For a good RAG system, index both:

- `.ipynb` files for implementation details
- `.md` files for conceptual explanations

---

# 22. Focused Weaviate RAG

A focused Weaviate RAG setup indexes only Weaviate-related materials.

Suggested collection:

```text
WeaviateFocusedRagChunk
```

Suggested indexed paths:

```text
vector_db/*.ipynb
vector_db/notes/*.md
```

The notebooks provide code implementation.

The Markdown notes provide explanations and definitions.

This combination improves answers because the model can use both implementation context and conceptual knowledge.

---

# 23. Named Vectors

Named vectors allow one object to have multiple vectors.

Example:

```text
title_vector
description_vector
```

This allows semantic search against a specific part of an object.

Example collection:

```python
hardware = client.collections.create(
    name="HardwareNamedVector",
    vector_config=[
        wvc.config.Configure.Vectors.text2vec_openai(
            name="title_vector",
            source_properties=["title"],
            model="text-embedding-3-small",
        ),
        wvc.config.Configure.Vectors.text2vec_openai(
            name="description_vector",
            source_properties=["description"],
            model="text-embedding-3-small",
        ),
    ],
)
```

Search by title vector:

```python
response = hardware.query.near_text(
    query="NVIDIA graphics card",
    target_vector="title_vector",
    limit=3,
)
```

Search by description vector:

```python
response = hardware.query.near_text(
    query="hardware useful for running machine learning models",
    target_vector="description_vector",
    limit=3,
)
```

Named vectors are useful when different properties represent different meanings.

---

# 24. Cross-References

Cross-references connect objects between collections.

Example:

```text
HardwareReview --forProduct--> HardwareProduct
```

This is similar to a relationship between SQL tables, such as:

```text
Review.product_id -> Product.id
```

However, in Weaviate, references should be used carefully. In many large-scale cases, denormalized data can be simpler and faster.

Create a reference property:

```python
reviews = client.collections.create(
    name="HardwareReview",
    properties=[
        wvc.config.Property(
            name="review_text",
            data_type=wvc.config.DataType.TEXT,
        ),
        wvc.config.Property(
            name="rating",
            data_type=wvc.config.DataType.INT,
        ),
        wvc.config.Property(
            name="reviewer",
            data_type=wvc.config.DataType.TEXT,
        ),
    ],
    references=[
        wvc.config.ReferenceProperty(
            name="forProduct",
            target_collection="HardwareProduct",
        ),
    ],
)
```

Add a reference:

```python
reviews.data.reference_add(
    from_uuid=review_uuid,
    from_property="forProduct",
    to=product_uuid,
)
```

Read references:

```python
response = reviews.query.fetch_objects(
    return_references=[
        QueryReference(
            link_on="forProduct",
            return_properties=["name", "component"],
        )
    ],
)
```

Cross-references do not automatically change the vector of the source or target object. The review has its own embedding, and the product has its own embedding.

---

# 25. Multi-Tenancy

Multi-tenancy allows one collection to store isolated data for multiple tenants.

A tenant can represent:

- client
- company
- organization
- user
- workspace

Example collection:

```text
TenantDocument
```

Example tenants:

```text
company_ai
company_dev
company_office
```

The schema is shared, but each tenant has a separate data space.

Create a multi-tenant collection:

```python
tenant_documents = client.collections.create(
    name="TenantDocument",
    vector_config=wvc.config.Configure.Vectors.text2vec_openai(
        model="text-embedding-3-small",
    ),
    generative_config=wvc.config.Configure.Generative.openai(
        model="gpt-4o-mini",
    ),
    multi_tenancy_config=wvc.config.Configure.multi_tenancy(
        enabled=True,
    ),
    properties=[
        wvc.config.Property(name="title", data_type=wvc.config.DataType.TEXT),
        wvc.config.Property(name="content", data_type=wvc.config.DataType.TEXT),
        wvc.config.Property(name="category", data_type=wvc.config.DataType.TEXT),
        wvc.config.Property(name="department", data_type=wvc.config.DataType.TEXT),
    ],
)
```

Add tenants:

```python
tenant_documents.tenants.create(
    tenants=[
        Tenant(name="company_ai"),
        Tenant(name="company_dev"),
        Tenant(name="company_office"),
    ]
)
```

Insert data for a tenant:

```python
tenant_collection = tenant_documents.with_tenant("company_ai")
tenant_collection.data.insert({...})
```

Search inside a tenant:

```python
tenant_collection = tenant_documents.with_tenant("company_ai")

response = tenant_collection.query.near_text(
    query="hardware for AI models",
    limit=3,
)
```

The same query can return different results for different tenants because each tenant has separate data.

Multi-tenancy is useful for SaaS applications where many clients share one schema but must have isolated data.

---

# 26. Common Errors and Fixes

## Incorrect OpenAI API key

If Weaviate returns a 401 error from OpenAI, the OpenAI API key is wrong.

Example error:

```text
OpenAI API failed with status: 401
Incorrect API key provided
```

Fix:

```python
os.environ.pop("OPENAI_API_KEY", None)
os.environ["OPENAI_API_KEY"] = getpass("OPENAI_API_KEY: ")
```

Then reconnect:

```python
client.close()

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WEAVIATE_URL"],
    auth_credentials=Auth.api_key(os.environ["WEAVIATE_API_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"],
    },
)
```

## Wrong package installation

The correct Python package is:

```text
weaviate-client
```

not only:

```text
weaviate
```

If the import is broken, reinstall:

```bash
uv pip uninstall weaviate weaviate-client
uv sync --reinstall-package weaviate-client
```

## ReferenceProperty error

`ReferenceProperty` should not be placed inside `properties`.

Wrong:

```python
properties=[
    wvc.config.Property(...),
    wvc.config.ReferenceProperty(...),
]
```

Correct:

```python
properties=[
    wvc.config.Property(...),
],
references=[
    wvc.config.ReferenceProperty(...),
]
```

---

# 27. Recommended Learning Order

A good learning path for Weaviate is:

1. Connect to local Weaviate in Docker
2. Connect to Weaviate Cloud
3. Create collections
4. Insert, read, update and delete objects
5. Inspect generated vectors
6. Run vector search
7. Run BM25 keyword search
8. Run hybrid search
9. Add generative search
10. Build text-to-image search with CLIP and self-provided vectors
11. Build RAG over project files
12. Improve RAG with Markdown concept notes
13. Add named vectors
14. Add cross-references
15. Add multi-tenancy

---

# 28. Summary

The project demonstrates how to use Weaviate locally and in Weaviate Cloud for:

- CRUD operations
- semantic vector search
- BM25 keyword search
- hybrid search
- generative search
- text-to-image search
- bring your own vectors
- RAG over local files
- focused RAG with notes and notebooks
- named vectors
- cross-references
- multi-tenancy

The main idea is:

```text
Weaviate stores objects, metadata, and vectors.
Embedding models convert text or images into vectors.
Search methods retrieve relevant objects.
Generative models can produce answers from retrieved context.
```

For reliable RAG, use clean and focused collections.

A good Weaviate knowledge system should combine:

```text
implementation context from notebooks
+
conceptual knowledge from Markdown notes
```

---

# 29. Polish-English Glossary

| English | Polish |
|---|---|
| collection | kolekcja |
| object | obiekt |
| property | właściwość / pole |
| UUID | identyfikator obiektu |
| vector | wektor |
| embedding | embedding / reprezentacja wektorowa |
| vector search | wyszukiwanie wektorowe |
| semantic search | wyszukiwanie semantyczne |
| keyword search | wyszukiwanie po słowach kluczowych |
| BM25 | algorytm keyword search |
| hybrid search | wyszukiwanie hybrydowe |
| generative search | wyszukiwanie generatywne |
| RAG | Retrieval-Augmented Generation |
| chunk | fragment tekstu |
| chunking | dzielenie tekstu na fragmenty |
| tenant | tenant / klient / organizacja |
| multi-tenancy | wielodostępność / izolacja tenantów |
| cross-reference | referencja między obiektami |
| named vector | nazwany wektor |
| bring your own vectors | dostarczanie własnych wektorów |
