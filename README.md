# Supository

A collection of experimental AI/runtime research files.

## Files

### Python Scripts

- **`nottingham_runtime.py`** – Sends a runtime state payload (gradient state, logic result, phase) to a local FastAPI endpoint at `http://127.0.0.1:8000/compute` and prints the API response.
- **`observer_wheel_engine.py`** – A Word document (`.docx`) containing engine/observer wheel design notes (despite the `.py` extension).

### Documents

- **`api_configuration.docx`** – API configuration documentation.
- **`gpt4freejsonmulti.json.pdf`** – GPT-4 free JSON multi-request reference document.
- **`The Logic of Oscillating Field States 12334 png- NotebookLM.pdf`** – Research notes on oscillating field state logic, generated via NotebookLM.

### Images

- **`279_diagonal_key.png`** – Diagonal key diagram.
- **`file-TmuEQYqx9eL1K3xMREcAMz.png`** – Generated image file.
- **`file_000000001ec861f58e1db017a49d5417.png`** – Generated image file.

## Usage

To run the Nottingham runtime loop (requires a local FastAPI server running on port 8000):

```bash
pip install requests
python nottingham_runtime.py
```

## Security Note

An OpenAI API key was accidentally included in a filename in an earlier commit. That key has since been **revoked** and the file has been renamed to `api_configuration.docx`. No action is needed.

To avoid this in future, never put API keys or secrets in filenames or file contents. Use environment variables or a secrets manager instead. The `.gitignore` in this repo includes patterns (e.g. `sk-*`) to help block accidental commits of credential files.
