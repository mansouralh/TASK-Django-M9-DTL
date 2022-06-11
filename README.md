Let's make some ice cream!

## Setup

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Django-M9-DTL).
2. Install the `requirements` using `pip install -r requirements/dev.lock`.
3. Run the `migrations`, create a `superuser`, and create some ice cream using the admin site.

## Task

### Detail View

1. Go to `shops/views.py`, and add a `get_ice_cream` view function that takes in a `request`, `ice_cream_id` and `renders` a template named `ice_cream_detail.html` (you might find this [link](https://docs.djangoproject.com/en/4.0/intro/tutorial03/#a-shortcut-render) useful).
   - Fetch the `ice cream` object based on the `id` received in the parameter
   - Add the following context to be injected into your template:
     - `name`: the ice cream's name as a string
     - `shop`: the ice cream's shop name as a string
     - `stock`: the ice cream's current stock as an integer
2. Add your `get_ice_cream` view to `bareed/url.py`.
   - Name it `ice-cream-detail` and make sure to add `ice_cream_id` to the path.
3. Create a `templates` folder inside of `shops` and add an `ice_cream_detail.html`.
   - The template should render the entire context passed to it
4. Run the server and check out your beautiful ice creams.
5. Run the tests using `pytest -m detail` and pass all tests.
6. Commit your code and push.

### Detail View Bonus

1. In the detail view wrap your fetch in a `try-except` block and raise an `Http404` if the ice cream id does not exist.
2. Run the tests using `pytest -m detail-bonus` and pass all tests.
3. Commit your code and push.

### List View

1. Go to `shops/views.py`, and add a `get_ice_creams` view function that takes in a `request`, and `renders` a template named `ice_cream_list.html`.
   - Your context should include the `name`s, `flavors` (as a list of strings), and `shop` names of all ice creams
2. Add your `get_ice_creams` view to `bareed/url.py` and name it `ice-cream-list`.
3. Create a `templates` folder inside of `shops` and add an `ice_cream_list.html`.
   - The template should render the entire context passed to it
   - Use the following [link](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#cycle) to see how to loop over objects in `DTL`
4. Run the server and check out your beautiful ice creams.
5. Run the tests using `pytest -m list` and pass all tests.
6. Commit your code and push.
