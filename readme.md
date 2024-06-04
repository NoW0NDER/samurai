# Samurai
This is a package that allows you to read the data once and store the data in the memory.
```
# In the server script:
from spirit import Samurai
data->Any
share = Samurai(name="A unique name", obj=data)


# In the second script:
from spirit import Samurai
data = Samurai(name='Same name as above')
```

Note that pickle is used in this package, and pickle is not safe. 

Only treat the data you trust as your spirit.