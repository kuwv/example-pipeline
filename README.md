# Example Pipeline
[![License](https://img.shields.io/badge/License-Unlicensed-blue.svg)](https://spdx.org/licenses/Unlicensed)
![Build Status](https://github.com/kuwv/example-pipeline/actions/workflows/main.yml/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/kuwv/example-pipeline/branch/master/graph/badge.svg)](https://codecov.io/gh/kuwv/example-pipeline)

## Overview

Provide example pipelines to prototype github actions.

## Install

```
pip install example_pipeline
```

## Development

```
pip install --user virtualenv
virtualenv .env
source .env/bin/activate
pip install '.[build,test,sca,style]'
```

