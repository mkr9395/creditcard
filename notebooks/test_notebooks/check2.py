import pathlib
from pathlib import Path

file_path = Path(__file__)
print("\n","file path is __file__ : ",file_path)

file_path = pathlib.Path(__file__)
print("\n","file pathlib.path is __file__ : ",file_path)

file_path2 = Path.cwd()
print("\n","file path is cwd : ",file_path2)


home_dir = file_path.parent.parent.parent
print("\n","home dir is : ",home_dir,"\n")



print()
model_path = (home_dir / "models")
print(model_path)
#print("modelpath as posix",model_path.as_posix())
print("model path: ",model_path)
model_path.mkdir(parents=True, exist_ok=True)