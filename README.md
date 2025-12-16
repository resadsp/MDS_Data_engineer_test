# MDS Data Engineer Test (Dec 2025)

This repository contains a solution for the **MDS Data Engineer Test (Dec 2025)**.  
It demonstrates **parallel processing of streaming messages** and **batch file processing**, following **OOP principles**, **SOLID design**, and Python concurrency using **ThreadPoolExecutor**. The project is fully modular, includes unit tests, and is **Docker-ready**.

---

## Project Overview

The project consists of 3 main modules plus a bonus module:

1. **Core**: Provides fundamental abstractions.
   - `Task` — Base class for units of work.
   - `WorkerPool` — Executes tasks in parallel using threads.
   - `Clock` — Time abstraction, useful for scheduling and testing.

2. **Stream**: Handles real-time message processing.
   - `Message` — Represents a single message.
   - `MessageSource` — Emits messages following a Poisson distribution.
   - `MiniBatch` — Collects messages into batches.
   - `MiniBatchBuilder` — Builds batches over fixed windows and submits them to WorkerPool.
   - `MiniBatchTask` — Processes a minibatch concurrently.

3. **Files**: Handles nightly batch file processing.
   - `File` — Represents a file with size metadata.
   - `FileSource` — Generates files with exponentially distributed sizes.
   - `Bucket` — Groups files into buckets for batch processing.
   - `BucketingStrategy` — Strategy pattern for bucketing logic.
   - `BucketManager` — Handles bucket creation and submission to WorkerPool.
   - `BucketTask` — Processes a bucket concurrently.

4. **Bonus (Tournament)**: Simulates a round-robin game tournament.
   - `Player` — Represents a player.
   - `Table` — Represents a game table.
   - `Tournament` — Implements round-robin scheduling, determining an overall winner and tracking opponents.

---

## Project Structure

```
src/
├── bonus/
│   ├── run_tournament_demo.py
│   ├── tournament.py
│   └── __init__.py
├── core/
│   ├── clock.py
│   ├── task.py
│   ├── worker_pool.py
│   └── __init__.py
├── files/
│   ├── bucket.py
│   ├── bucketing_strategy.py
│   ├── bucket_manager.py
│   ├── file.py
│   ├── source.py
│   └── __init__.py
├── orchestration/
│   ├── run_files_demo.py
│   ├── run_stream_demo.py
│   └── __init__.py
├── stream/
│   ├── message.py
│   ├── message_source.py
│   ├── minibatch.py
│   ├── minibatch_builder.py
│   ├── minibatch_task.py
│   └── __init__.py
├── entrypoint.sh
└── main.py

tests/
├── test_bonus.py
├── test_bucketing.py
├── test_bucketing_property.py
├── test_bucketing_strategies.py
├── test_bucket_manager.py
├── test_core_clock.py
├── test_files_module.py
├── test_minibatch.py
├── test_stream.py
├── test_worker_pool.py
└── __init__.py
```

---

## Usage

### Run Stream Demo

```bash
export PYTHONPATH="$PWD/src"
python -m orchestration.run_stream_demo
```

### Run Files Demo

```bash
export PYTHONPATH="$PWD/src"
python -m orchestration.run_files_demo
```

### Run Tournament Demo

```bash
export PYTHONPATH="$PWD/src"
python -m bonus.run_tournament_demo
```

---

### Running Tests

```bash
pytest tests/
```

To generate a coverage report:

```bash
pytest --cov --cov-config=.coveragerc --cov-report=term-missing --cov-report html:/app/htmlcov
```

---

### Docker Usage

**Build the image:**

```bash
docker build -t mds_data_engineer_test .
```

**Run Stream Demo:**

```bash
docker run --rm mds_data_engineer_test stream
```

**Run Files Demo:**

```bash
docker run --rm mds_data_engineer_test files
```

**Run Tournament Demo:**

```bash
docker run --rm mds_data_engineer_test bonus
```

The `entrypoint.sh` automatically sets `PYTHONPATH` and runs the selected demo.

---

### Design Notes

- **OOP & SOLID principles** applied throughout.
- **Modular design** — each module can be extended independently.
- **WorkerPool** ensures all tasks execute in parallel.
- State is in-memory; a production system could persist data in a database.
- Tests and mocks demonstrate correctness without external dependencies.

---

### Requirements

- Python 3.11+
- Dependencies listed in `requirements.txt`

---

### Contributing

1. Fork the repository  
2. Create a feature branch  
```bash
git checkout -b feature/my-feature
```  
3. Implement changes and run tests  
4. Commit and push  
```bash
git add .
git commit -m "feat(module): brief description"
git push origin feature/my-feature
```  
5. Open a Pull Request

---

### Author

**Resad Spahovic** – MDS Data Engineer Test (Dec 2025)
