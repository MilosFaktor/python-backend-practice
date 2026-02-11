import logging
import time
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


# print(Path.cwd())

# for p in Path().iterdir():
#     print(p)

my_dir = Path("Directory_1")
my_file = Path("file_1.txt")

new_file = my_dir / "new_file.txt"

# print(my_dir.resolve())
# print(my_file.parent)
# print(new_file.parent.parent)

# p = Path(__file__).resolve()

# print(p)

# p = Path("~/dotfiles").expanduser()
# p = Path.home() / "dotfiles"

# p = Path(".")
# for item in p.glob("*file*"):
#     with open(item, "r") as f:
#         print(f.read())

# p = Path("Tempdir/Subdir")
# p.mkdir(exist_ok=True, parents=True)
# time.sleep(2)
# p.rmdir()
# p.parent.rmdir()

p = Path("Tempfile.txt")
print(p)
p.touch()
time.sleep(2)

pp = p.rename("Tempfile2.txt")
print(pp)
pp.unlink()
logger.info("deleted")
