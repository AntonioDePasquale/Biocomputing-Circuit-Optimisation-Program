import re
import random

from itertools import product
from quine_mccluskey.qm import QuineMcCluskey
from .transformations import associativity_law
from .transformations import commutativity_law
from .transformations import majority_law
from .transformations import distributivity_law