# CAD-LLM

A machine learning project for training language models on CAD (Computer-Aided Design) data, specifically focused on air motor components.

## Project Overview

This repository contains code for training GPT-2 models on CAD-related text data. The project includes data preprocessing, model training, and evaluation pipelines for understanding and generating CAD descriptions.

## Getting Started

### Prerequisites
- Python 3.8+
- CUDA-compatible GPU (recommended for training)
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/eigan314/cad-llm.git
cd cad-llm
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Set up Jupyter kernel (optional):
```bash
python -m ipykernel install --user --name cad-llm --display-name "Python (CAD-LLM)"
```

### Usage

#### Training a Model
```bash
# Run the training notebook
jupyter notebook notebooks/train_gpt2_airmotor.ipynb
```

#### Using the Source Code
```bash
# Run training scripts directly
python src/train.py --config config.yaml
```

## Project Structure

```
cad-llm/
├── notebooks/           # Jupyter notebooks for experimentation
│   └── train_gpt2_airmotor.ipynb
├── src/                 # Source code modules
├── datasets/            # Training and evaluation datasets
├── requirements.txt     # Python dependencies
├── Makefile            # Build and utility commands
└── README.md           # This file
```

## Configuration

- **Datasets**: Place your training data in the `datasets/` directory
- **Models**: Trained models are saved in the `models/` directory (git-ignored)
- **Logs**: Training logs and metrics are stored in `logs/` (git-ignored)

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test them
4. Commit your changes: `git commit -m "Add feature"`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or issues, please open an issue on GitHub or contact the maintainers.
