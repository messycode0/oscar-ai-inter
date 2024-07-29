# Oscar AI Interface

This repository contains a simple AI interface using [Ollama](https://ollama.com/)'s llama3 model, implemented in Python. The interface allows for local and remote AI processing.

## Repository Structure

- `main.py`: The main script to interact with the AI.
- `server.py`: The Flask server to handle remote AI requests.

## Setup

### Prerequisites

- Python 3.8+
- [Ollama AI Wrapper](https://ollama.com/)
- Ollama Python package
- Flask
- Requests

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/messycode0/oscar-ai-inter.git
    cd oscar-ai-interface
    ```

2. Install the required packages:

    2A (Client): 

    ```bash
    pip install ollama requests
    ```

    2B (Server):

    ```bash 
    pip install flask ollama
    ```

## Usage

### Local Mode

Run `main.py` without any arguments to use the AI locally:

```bash
python main.py
```

### Remote Mode

1. (on server) Start the Flask server by running server.py:

```bash
python server.py
```

2. (on client) Run main.py with the --remote flag to use the AI remotely:

```bash 
python main.py --remote
```

### License 

This Project uses the ***GNU General Public License v3.0***


