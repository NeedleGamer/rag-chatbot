# PROJECT STATUS SNAPSHOT — RAG Chatbot

## Completed Checkpoints
- C0: Repo, venv, Git baseline ✅
- C1: Scaffold + central config ✅
- CP1.2: Groq API integration ✅
- CP1.3: Core dependencies installation + smoke tests ✅

## Repo Structure
- src/config/settings.py → central config, env var loading, defaults, dir creation (cross-platform, pathlib, pydantic-settings)
- src/config/__init__.py → package marker
- src/indexing/__init__.py → placeholder
- src/retrieval/__init__.py → placeholder
- src/ui/__init__.py → placeholder
- src/evaluation/__init__.py → placeholder
- src/utils/logging.py → logging defaults using LOG_LEVEL from config
- scripts/test_config.py → config smoke test (prints settings, confirms dirs)
- scripts/test_imports.py → dependency import test
- scripts/test_langchain.py → minimal langchain import check
- scripts/test_chroma_persist.py → verifies chromadb PersistentClient, persist to data/chroma
- scripts/download_sbert.py → downloads sentence-transformers model into data/hf_home
- scripts/diagnose_my_setup.py → diagnostics script for sys.path, env, packages, config snapshot
- app/app_hello.py → Streamlit hello-world app, displays config values
- .env.example → template env vars
- requirements.txt → pinned core deps
- requirements.lock.txt → frozen exact dep graph
- README.md → setup + conventions (env var naming, config usage, smoke tests)
- .gitignore → ignores venv, logs, data, cache, secrets

## Environment / Dependencies
- Python 3.12 (venv active)
- langchain==0.3.27
- chromadb==1.0.20
- streamlit==1.48.1
- sentence-transformers==5.1.0
- groq==0.31.0
- langchain-groq==0.3.7
- pydantic==2.11.1
- pydantic-settings==2.10.1
- python-dotenv==1.1.1
- tqdm==4.66.5

## Known Fixes / Immediate Workarounds
- sys.path injection added in scripts and app for imports (short-term)
- Pydantic v2 fix: moved to pydantic-settings; helper uses model_dump if available
- Hugging Face cache relocated to data/hf_home (via HF_HOME or cache_folder param)
- Streamlit import issue fixed by sys.path injection or editable install
- Config `settings_to_dict` avoids `.dict()` deprecation warning

## Smoke Test Results (all passing)
- python -m scripts.test_config → prints settings summary, creates dirs ✅
- python -m scripts.test_imports → all imports OK ✅
- python -m scripts.download_sbert → downloads model to data/hf_home ✅
- python -m scripts.test_chroma_persist → Chroma persistent DB created ✅
- streamlit run app/app_hello.py → hello-world loads ✅ (after path fix)
- python -m scripts.test_langchain → confirms langchain core import ✅

## Current Status
- Repo is scaffolded and reproducible.
- Config resilient, cross-platform, default-safe.
- Dependencies installed, pinned, verified with smoke tests.
- All immediate issues resolved with either sys.path injection or env var setup.
- Project is ready to move forward to next checkpoint (C2).
