from typing import Optional
from pydantic import BaseModel

class DocServiceArgs(BaseModel):

    slug: str
    use_docraptor: Optional[bool] = True
    test_mode: Optional[bool] = False
    # TODO: variables: dict
