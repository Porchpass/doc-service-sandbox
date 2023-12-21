from typing import Optional, List, TypedDict, Required, Union
from pydantic import BaseModel

class DocServiceArgs(BaseModel):
  slug: str
  use_docraptor: Optional[bool] = True
  test_mode: Optional[bool] = False
  # variables: dict