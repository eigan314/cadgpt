    .PHONY: setup notebook gpu

    setup:
    	python -m pip install --upgrade pip
    	pip install -r requirements.txt
    	python -m ipykernel install --user --name paramcad --display-name "Python (parametric_cad)"

    notebook:
    	jupyter lab --no-browser --port 8888

    gpu:
    	python - << 'PY'
import torch;print('torch:',getattr(torch,'__version__',None),'cuda:',getattr(torch.version,'cuda',None),'is_cuda:',torch.cuda.is_available())
PY
