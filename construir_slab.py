from ase.build import fcc111
from ase.io import write
slab = fcc111('Ag', size=(1,1,1), vacuum=10.0)
write('Ag_cn.vasp', slab)