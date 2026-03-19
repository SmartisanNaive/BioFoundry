from contextvars import ContextVar

from biofoundry_os import FoundryOS
from biofoundry_os.local import local_foundry_os

current_foundry_os = ContextVar[FoundryOS]("current_foundry_os", default=local_foundry_os)
