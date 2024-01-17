from src.models import doc, customer
from src.models.person import Person
def test_person_model():
  # arrange
  full_name = "josh test"
  json_args = {"full_name": "josh test"}
  # act
  p = Person(**json_args)
  # assert
  assert p.full_name == full_name
  assert p.model_dump() == json_args

# def test_customer_model():
#   # arrange
#   full_name            = "josh test"
#   customer_file_number = "123"
#   # act
#   c = customer.Customer(
#     full_name=full_name,
#     customer_file_number = customer_file_number
#   )
#   # assert
#   print(c.full_name)
#   print(c.customer_full_name)
#   assert c.customer_full_name == full_name
#   assert c.customer_file_number == customer_file_number

# def test_doc_service_args():
#   # arrange
#   slug          = "test"
#   use_docraptor = False
#   test_mode     = True
  
#   # act
#   docServiceArgs = doc.DocServiceArgs(
#     slug          = slug,
#     use_docraptor = use_docraptor,
#     test_mode     = test_mode 
#   )
  
#   # assert
#   assert docServiceArgs.slug == slug
#   assert docServiceArgs.use_docraptor == use_docraptor
#   # assert docServiceArgs.test_mode == test_mode