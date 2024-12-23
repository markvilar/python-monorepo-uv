# Python Monorepo

A template repository for Python monorepos with integration of the uv package manager.
The repository contains the following components:

- A shared package with utility functionality
- A package with core functionality
- A backend with an API based on `fastapi`
- A frontend based on `streamlit`


#### Building the project components

```shell
uv build src/core
uv build src/backend
uv build src/frontend
```

#### Running the backend

```shell
cd src/backend
uv run backend
```

#### Running the frontend

```shell
cd src/frontend
uv run streamlit run src/frontend/runner.py
```

### Acknowledgement

This repository is heavily inspired by [uv-monorepo](https://github.com/JasperHG90/uv-monorepo/tree/main).
