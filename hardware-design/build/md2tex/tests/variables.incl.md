foo: variable *string* with inline `formatting` and **also a link** see http://instagram.com
bar: 
- list entry within the yaml variable
- another one
spaghetti:
- this is a list within a yaml variable
    - nested lists are not rendered! get a hold of yourself
- we also have some **inline** formatting
---

@@foo@@

and we can also do @@foo@@ within a line

it even works inside literal blocks, though we might want to change that in the future:
```arm
@@foo@@
```

@@bar@@

@@spaghetti@@