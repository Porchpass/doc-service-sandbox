from src.models import doc

# from src.models import DocServiceArgs

docServiceArgs = doc.DocServiceArgs(
  slug="test",
  use_docraptor=False,
  test_mode=True
)

print(docServiceArgs)
