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

### Resources

To get an overview the monorepo architecture, check out Magenta Qins blog post [Monorepo vs. Multi-repo vs. Monolith](https://medium.com/@magenta2127/monorepo-vs-multi-repo-vs-monolith-7c4a5f476009).

### Acknowledgement

This repository is heavily inspired by [uv-monorepo](https://github.com/JasperHG90/uv-monorepo/tree/main).
