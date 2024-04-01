import os
from pathlib import Path

package_name = "mongodb_connect"

list_of_files = [
   ".github/workflows/ci.yaml",
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/mongo_crud.py", 
   "src/componets/__init__.py"
   "src/componets/data_ingestion.py",
   "src/componets/data_transformation.py",
   "src/componets/model_evaluation.py",
   "src/componets/data_ingestion.py",
   "src/componets/model_trainer.py",
   "src/exception/__init__.py",
   "src/exception/exception.py",
   "src/logging/__init__.py",
   "src/logging/logging.py",
   "src/pipeline/__init__.py",
   "src/pipeline/prediction_pipeline.py",
   "src/pipeline/training_pipeline.py",
   "src/utils/__init__.py",
   "src/utils/utils.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt", 
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file

#its updated